# -*- coding: UTF-8 -*
from PIL import Image, ImageDraw, ImageFont
from src.processor import nx_equation, ux_equation, sgx_equation


def draw_epure(input_list_of_length: list, input_list_of_width: list, input_list_of_young_modulus: list,
               input_list_of_loads: list, input_powers: dict, input_left_sealing: bool, input_right_sealing: bool,
               bg_color: str = '#fff0ee', window_length: int = 800, window_width: int = 600,
               flag_labels: bool = True) -> Image.Image:
    """
    The function of drawing a epure in png format (for the postprocessor tab)
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_list_of_loads: List of loads on rods
    :param input_powers: Dict of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
    :param input_list_of_width: List of rods' areas
    :param bg_color: Background color of the future image (set in RGB format)
    :param window_length: Length of future picture
    :param window_width: Width of future picture
    :param flag_labels: True/False visible signatures
    :return: new_img - Pillow.Image.Image
    """

    count_rods = len(input_list_of_length)

    if window_length < 800:
        window_length = 800
    if window_width < 600:
        window_width = 600

    font = ImageFont.truetype('arial.ttf', size=11, encoding='UTF-8')
    font_text_epure = ImageFont.truetype('arial.ttf', size=15, encoding='UTF-8')

    # копия массивов длины и ширины для расчётов
    list_of_length_for_calc = input_list_of_length.copy()
    list_of_width_for_calc = input_list_of_width.copy()
    list_of_young_modulus_for_calc = input_list_of_young_modulus.copy()

    # копия массивов длины и ширины для подписей характеристик стержней
    list_length_for_label = []
    list_width_for_label = []
    if flag_labels:
        list_length_for_label = input_list_of_length.copy()
        list_length_for_label.reverse()
        list_width_for_label = input_list_of_width.copy()
        list_width_for_label.reverse()
        input_list_of_young_modulus.reverse()

    # решение проблемы: излишняя разница длины стержней
    if max(input_list_of_length) / min(input_list_of_length) > 5:
        list_of_x_common = []
        for x in input_list_of_length:
            if x == max(input_list_of_length):
                pass
            else:
                if max(input_list_of_length) / x > 5:
                    zoom_x = (max(input_list_of_length) / x) / 5
                    x *= zoom_x
            list_of_x_common.append(x)
        input_list_of_length = list_of_x_common

    # решение проблемы: отрисовка эпюры за пределами экрана по длине
    if sum(input_list_of_length) != window_length:
        decrease_x = (window_length - 100) / sum(input_list_of_length)
        input_list_of_length = [x * decrease_x for x in input_list_of_length]

    new_img = Image.new('RGB', (window_length, window_width), f'{bg_color}')
    pencil = ImageDraw.Draw(new_img)

    input_list_of_length.reverse()
    input_list_of_width.reverse()

    # координаты x 1 стержня
    pos_x = 50
    length = input_list_of_length.pop() + pos_x
    # координаты y 1 стержня
    pos_y = 40
    # отрисовка стержня
    pencil.line((pos_x, pos_y, length, pos_y), fill='#000000', width=3)

    # подпись характеристик 1 стержня
    if flag_labels:
        label_length = list_length_for_label.pop()
        label_square = list_width_for_label.pop()
        label_young_modulus = input_list_of_young_modulus.pop()

        text_label = ['L', 'A;', 'E']

        if label_length != 1:
            text_label[0] = f'{label_length}L'

        if label_square != 1:
            text_label[1] = f'{label_square}A;'

        if label_young_modulus != 1:
            text_label[2] = f'{label_young_modulus}E'

        pencil.line((pos_x + 1.5, pos_y, pos_x + 1.5, pos_y + 15), fill='#000000', width=1)
        pencil.line((length - 1.5, pos_y, length - 1.5, pos_y + 15), fill='#000000', width=1)
        pencil.line((pos_x + 1.5, pos_y + 12, length - 1.5, pos_y + 12), fill='#000000', width=1)

        pencil.line((pos_x + 2, pos_y + 12, pos_x + 5, pos_y + 9), fill='#000000', width=1)
        pencil.line((pos_x + 2, pos_y + 12, pos_x + 5, pos_y + 15), fill='#000000', width=1)
        pencil.line((length - 2, pos_y + 12, length - 5, pos_y + 9), fill='#000000', width=1)
        pencil.line((length - 2, pos_y + 12, length - 5, pos_y + 15), fill='#000000', width=1)

        pencil.text(((length + pos_x) / 2, pos_y + 11), text_label[0], anchor='ms', fill='#000000', font=font)
        pencil.text(((length + pos_x) / 2, pos_y - 16), text_label[1], anchor='ms', fill='#000000', font=font)
        pencil.text(((length + pos_x) / 2, pos_y - 4), text_label[2], anchor='ms', fill='#000000', font=font)

        # подпись номеров стержней
        pencil.ellipse(((length + pos_x) / 2 - 9, pos_y + 17, (length + pos_x) / 2 + 7, pos_y + 33),
                       outline='#000000', width=1)
        pencil.text(((length + pos_x) / 2 - 1.5, pos_y + 30), f'1', anchor='ms', fill='#000000', font=font)

        # подпись номера 1 узла
        pencil.rectangle((pos_x + 5, pos_y + 17, pos_x + 16, pos_y + 29), outline='#000000', width=1)
        pencil.text((pos_x + 8, pos_y + 17), f'1', fill='#000000', font=font)

    # расчёт длины эпюры
    length_lines_epure = window_width - 20 - (pos_y + 15)
    horizontal_lines = length_lines_epure / 3.3

    # черчение эпюры

    pencil.line((pos_x + 1.5, pos_y - 2, pos_x + 1.5, window_width - 20), fill='#000000', width=3)
    pencil.line((length, pos_y - 2, length, window_width - 20), fill='#000000', width=3)

    zoom_graph = (length - pos_x - 1.5) / list_of_length_for_calc[0]
    value_x_end = list_of_length_for_calc[0]

    # N[x]
    pencil.line((pos_x + 1.5, horizontal_lines, length, horizontal_lines), fill='#000000', width=3)

    value_x_nx = 0
    nx_value_in_x = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                  list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                  input_right_sealing, 1, value_x_nx) * 20

    if flag_labels:
        pencil.text((pos_x - 20, horizontal_lines - 10), 'Nx', fill='#000000', font=font_text_epure)
        # ------------------------------------------------------------------------------------------------------
        value_for_label = str(round(- nx_value_in_x / 20, 3))
        pencil.text((pos_x + 12, horizontal_lines + nx_value_in_x + 8),
                    value_for_label, fill='#000000', font=font)
        pencil.line((pos_x + 9,
                     horizontal_lines + nx_value_in_x + 8,
                     pos_x + 1.5,
                     horizontal_lines + nx_value_in_x), fill='#000000', width=1)
        # ------------------------------------------------------------------------------------------------------
        nx_value_in_x_end = nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                        list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                        input_right_sealing, 1, value_x_end)
        pencil.text((length - 35, horizontal_lines - nx_value_in_x_end * 20 - 22),
                    str(round(nx_value_in_x_end, 3)), fill='#000000', font=font)
        pencil.line((length - 20,
                     horizontal_lines - nx_value_in_x_end * 20 - 12,
                     length - 1.5,
                     horizontal_lines - nx_value_in_x_end * 20), fill='#000000', width=1)

    value_x_nx_2 = 0.001
    # nx_value_in_x_2 = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
    #                                 list_of_young_modulus_for_calc, input_powers, input_left_sealing,
    #                                 input_right_sealing, 1, value_x_nx_2) * 20
    #
    # pencil.line((pos_x + 1.5 + value_x_nx * zoom_graph, horizontal_lines + nx_value_in_x,
    #              pos_x + 1.5 + value_x_nx_2 * zoom_graph, horizontal_lines + nx_value_in_x_2),
    #             fill='#FF4500', width=3)
    # value_x_nx = value_x_nx_2
    # nx_value_in_x = nx_value_in_x_2

    while round(value_x_nx_2, 3) <= list_of_length_for_calc[0]:
        # value_x_nx_2 = value_x_nx_2 + 0.001
        nx_value_in_x_2 = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                        list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                        input_right_sealing, 1, value_x_nx_2) * 20

        pencil.line((pos_x + 1.5 + value_x_nx * zoom_graph, horizontal_lines + nx_value_in_x,
                     pos_x + 1.5 + value_x_nx_2 * zoom_graph, horizontal_lines + nx_value_in_x_2),
                    fill='#FF4500', width=3)
        value_x_nx = value_x_nx_2
        nx_value_in_x = nx_value_in_x_2
        value_x_nx_2 = value_x_nx_2 + 0.001
    #
    # ========================================================================================================
    # U[x]
    pencil.line((pos_x + 1.5, horizontal_lines * 2, length, horizontal_lines * 2), fill='#000000', width=3)

    value_x_ux = 0
    ux_value_in_x = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                  list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                  input_right_sealing, 1, value_x_ux) * 20

    if flag_labels:
        pencil.text((pos_x - 20, horizontal_lines * 2 - 10), 'Ux', fill='#000000', font=font_text_epure)

        # ------------------------------------------------------------------------------------------------------
        value_for_label = str(round(- ux_value_in_x / 20, 3))
        pencil.text((pos_x + 12, horizontal_lines * 2 + ux_value_in_x + 8),
                    value_for_label, fill='#000000', font=font)
        pencil.line((pos_x + 9,
                     horizontal_lines * 2 + ux_value_in_x + 8,
                     pos_x + 1.5,
                     horizontal_lines * 2 + ux_value_in_x), fill='#000000', width=1)
        # ------------------------------------------------------------------------------------------------------
        ux_value_in_x_end = ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                        list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                        input_right_sealing, 1, value_x_end)
        pencil.text((length - 35, horizontal_lines * 2 - ux_value_in_x_end * 20 - 22),
                    str(round(ux_value_in_x_end, 3)), fill='#000000', font=font)
        pencil.line((length - 20,
                     horizontal_lines * 2 - ux_value_in_x_end * 20 - 12,
                     length - 1.5,
                     horizontal_lines * 2 - ux_value_in_x_end * 20), fill='#000000', width=1)

    value_x_ux_2 = 0.001
    # ux_value_in_x_2 = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
    #                                 list_of_young_modulus_for_calc, input_powers, input_left_sealing,
    #                                 input_right_sealing, 1, value_x_ux_2) * 20
    # pencil.line((pos_x + 1.5 + value_x_ux * zoom_graph, horizontal_lines * 2 + ux_value_in_x,
    #              pos_x + 1.5 + value_x_ux_2 * zoom_graph, horizontal_lines * 2 + ux_value_in_x_2),
    #             fill='#FF4500', width=3)
    #
    # value_x_ux = value_x_ux_2
    # ux_value_in_x = ux_value_in_x_2

    while value_x_ux_2 < list_of_length_for_calc[0]:
        # value_x_ux_2 += 0.001
        ux_value_in_x_2 = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                        list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                        input_right_sealing, 1, value_x_ux_2) * 20

        pencil.line((pos_x + 1.5 + value_x_ux * zoom_graph, horizontal_lines * 2 + ux_value_in_x,
                     pos_x + 1.5 + value_x_ux_2 * zoom_graph, horizontal_lines * 2 + ux_value_in_x_2),
                    fill='#FF4500', width=3)
        value_x_ux = value_x_ux_2
        ux_value_in_x = ux_value_in_x_2
        value_x_ux_2 += 0.001
    #
    # ========================================================================================================
    # Sg[x]
    pencil.line((pos_x + 1.5, horizontal_lines * 3, length, horizontal_lines * 3), fill='#000000', width=3)

    value_x_sgx = 0
    sgx_value_in_x = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                    list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                    input_right_sealing, 1, value_x_sgx) * 20

    if flag_labels:
        pencil.text((pos_x - 20, horizontal_lines * 3 - 10), 'σx', fill='#000000', font=font_text_epure)
        # ------------------------------------------------------------------------------------------------------
        value_for_label = str(round(- sgx_value_in_x / 20, 3))
        pencil.text((pos_x + 12, horizontal_lines * 3 + sgx_value_in_x + 8),
                    value_for_label, fill='#000000', font=font)
        pencil.line((pos_x + 9,
                     horizontal_lines * 3 + sgx_value_in_x + 8,
                     pos_x + 1.5,
                     horizontal_lines * 3 + sgx_value_in_x), fill='#000000', width=1)
        # ------------------------------------------------------------------------------------------------------
        sgx_value_in_x_end = sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                          list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                          input_right_sealing, 1, value_x_end)
        pencil.text((length - 35, horizontal_lines * 3 - sgx_value_in_x_end * 20 - 22),
                    str(round(sgx_value_in_x_end, 3)), fill='#000000', font=font)
        pencil.line((length - 20,
                     horizontal_lines * 3 - sgx_value_in_x_end * 20 - 12,
                     length - 1.5,
                     horizontal_lines * 3 - sgx_value_in_x_end * 20), fill='#000000', width=1)

    value_x_sgx_2 = 0.001
    # sgx_value_in_x_2 = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
    #                                   list_of_young_modulus_for_calc, input_powers, input_left_sealing,
    #                                   input_right_sealing, 1, value_x_sgx_2) * 20
    # pencil.line((pos_x + 1.5 + value_x_sgx * zoom_graph, horizontal_lines * 3 + sgx_value_in_x,
    #              pos_x + 1.5 + value_x_sgx_2 * zoom_graph, horizontal_lines * 3 + sgx_value_in_x_2),
    #             fill='#FF4500', width=3)
    #
    # value_x_sgx = value_x_sgx_2
    # sgx_value_in_x = sgx_value_in_x_2

    while value_x_sgx_2 < list_of_length_for_calc[0]:
        # value_x_sgx_2 += 0.001
        sgx_value_in_x_2 = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                          list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                          input_right_sealing, 1, value_x_sgx_2) * 20

        pencil.line((pos_x + 1.5 + value_x_sgx * zoom_graph, horizontal_lines * 3 + sgx_value_in_x,
                     pos_x + 1.5 + value_x_sgx_2 * zoom_graph, horizontal_lines * 3 + sgx_value_in_x_2),
                    fill='#FF4500', width=3)
        value_x_sgx = value_x_sgx_2
        sgx_value_in_x = sgx_value_in_x_2
        value_x_sgx_2 += 0.001
    #
    # ========================================================================================================
    # заделка слева
    if input_left_sealing:
        pencil.line((pos_x + 1.5, pos_y - 7, pos_x + 1.5, pos_y + 7), fill='#000000', width=3)
        for y in range(int(pos_y - 7), int(pos_y + 7), 8):
            pencil.line((pos_x + 1.5, y, pos_x - 6.5, y + 8), fill='#000000', width=2)

    # отрисовка стержней №2...N
    y = 1
    for y in range(1, count_rods):

        # координаты x
        pos_x = length - 1.5
        length = input_list_of_length.pop() + pos_x
        # координаты y
        pos_y = 40
        # отрисовка стержня № y (начиная с 2-ого)
        pencil.line((pos_x + 0.5, pos_y - 4, pos_x + 0.5, pos_y + 4), fill='#000000', width=2)
        pencil.line((pos_x, pos_y, length, pos_y), fill='#000000', width=3)

        # черчение эпюры
        pencil.line((pos_x + 1.5, pos_y - 2, pos_x + 1.5, window_width - 20), fill='#000000', width=3)
        pencil.line((length, pos_y - 2, length, window_width - 20), fill='#000000', width=3)

        zoom_graph = (length - pos_x - 1.5) / list_of_length_for_calc[y]
        value_x_end = list_of_length_for_calc[y]

        # N[x]
        pencil.line((pos_x + 1.5, horizontal_lines, length, horizontal_lines), fill='#000000', width=3)

        value_x_nx = 0
        nx_value_in_x = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                      list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                      input_right_sealing, y + 1, value_x_nx) * 20

        if flag_labels:
            # ------------------------------------------------------------------------------------------------------
            value_for_label = str(round(- nx_value_in_x / 20, 3))
            pencil.text((pos_x + 12, horizontal_lines + nx_value_in_x + 8),
                        value_for_label, fill='#000000', font=font)
            pencil.line((pos_x + 9,
                         horizontal_lines + nx_value_in_x + 8,
                         pos_x + 1.5,
                         horizontal_lines + nx_value_in_x), fill='#000000', width=1)
            # ------------------------------------------------------------------------------------------------------
            nx_value_in_x_end = nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                            list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                            input_right_sealing, y + 1, value_x_end)
            pencil.text((length - 35, horizontal_lines - nx_value_in_x_end * 20 - 22),
                        str(round(nx_value_in_x_end, 3)), fill='#000000', font=font)
            pencil.line((length - 20,
                         horizontal_lines - nx_value_in_x_end * 20 - 12,
                         length - 1.5,
                         horizontal_lines - nx_value_in_x_end * 20), fill='#000000', width=1)

        value_x_nx_2 = 0.001
        # nx_value_in_x_2 = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
        #                                 list_of_young_modulus_for_calc, input_powers, input_left_sealing,
        #                                 input_right_sealing, y + 1, value_x_nx_2) * 20
        # pencil.line((pos_x + 1.5 + value_x_nx * zoom_graph, horizontal_lines + nx_value_in_x,
        #              pos_x + 1.5 + value_x_nx_2 * zoom_graph, horizontal_lines + nx_value_in_x_2),
        #             fill='#FF4500', width=3)
        #
        # value_x_nx = value_x_nx_2
        # nx_value_in_x = nx_value_in_x_2

        while value_x_nx_2 < list_of_length_for_calc[y]:
            # value_x_nx_2 += 0.001
            nx_value_in_x_2 = - nx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                            list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                            input_right_sealing, y + 1, value_x_nx_2) * 20

            pencil.line((pos_x + 1.5 + value_x_nx * zoom_graph, horizontal_lines + nx_value_in_x,
                         pos_x + 1.5 + value_x_nx_2 * zoom_graph, horizontal_lines + nx_value_in_x_2),
                        fill='#FF4500', width=3)
            value_x_nx = value_x_nx_2
            nx_value_in_x = nx_value_in_x_2
            value_x_nx_2 += 0.001
        #
        # ====================================================================================================
        # U[x]
        pencil.line((pos_x + 1.5, horizontal_lines * 2, length, horizontal_lines * 2), fill='#000000', width=3)

        value_x_ux = 0
        ux_value_in_x = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                      list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                      input_right_sealing, y + 1, value_x_ux) * 20
        if flag_labels:
            # ------------------------------------------------------------------------------------------------------
            value_for_label = str(round(- ux_value_in_x / 20, 3))
            pencil.text((pos_x + 12, horizontal_lines * 2 + ux_value_in_x + 8),
                        value_for_label, fill='#000000', font=font)
            pencil.line((pos_x + 9,
                         horizontal_lines * 2 + ux_value_in_x + 8,
                         pos_x + 1.5,
                         horizontal_lines * 2 + ux_value_in_x), fill='#000000', width=1)
            # ------------------------------------------------------------------------------------------------------
            ux_value_in_x_end = ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                            list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                            input_right_sealing, y + 1, value_x_end)
            pencil.text((length - 35, horizontal_lines * 2 - ux_value_in_x_end * 20 - 22),
                        str(round(ux_value_in_x_end, 3)), fill='#000000', font=font)
            pencil.line((length - 20,
                         horizontal_lines * 2 - ux_value_in_x_end * 20 - 12,
                         length - 1.5,
                         horizontal_lines * 2 - ux_value_in_x_end * 20), fill='#000000', width=1)
        value_x_ux_2 = 0.001
        # ux_value_in_x_2 = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
        #                                 list_of_young_modulus_for_calc, input_powers, input_left_sealing,
        #                                 input_right_sealing, y + 1, value_x_ux_2) * 20
        # pencil.line((pos_x + 1.5 + value_x_ux * zoom_graph, horizontal_lines * 2 + ux_value_in_x,
        #              pos_x + 1.5 + value_x_ux_2 * zoom_graph, horizontal_lines * 2 + ux_value_in_x_2),
        #             fill='#FF4500', width=3)
        #
        # value_x_ux = value_x_ux_2
        # ux_value_in_x = ux_value_in_x_2

        while value_x_ux_2 < list_of_length_for_calc[y]:
            # value_x_ux_2 += 0.001
            ux_value_in_x_2 = - ux_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                            list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                            input_right_sealing, y + 1, value_x_ux_2) * 20

            pencil.line((pos_x + 1.5 + value_x_ux * zoom_graph, horizontal_lines * 2 + ux_value_in_x,
                         pos_x + 1.5 + value_x_ux_2 * zoom_graph, horizontal_lines * 2 + ux_value_in_x_2),
                        fill='#FF4500', width=3)
            value_x_ux = value_x_ux_2
            ux_value_in_x = ux_value_in_x_2
            value_x_ux_2 += 0.001
        #
        # ====================================================================================================
        # Sg[x]
        pencil.line((pos_x + 1.5, horizontal_lines * 3, length, horizontal_lines * 3), fill='#000000', width=3)

        value_x_sgx = 0
        sgx_value_in_x = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                        list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                        input_right_sealing, y + 1, value_x_sgx) * 20

        if flag_labels:
            # ------------------------------------------------------------------------------------------------------
            value_for_label = str(round(- sgx_value_in_x / 20, 3))
            pencil.text((pos_x + 12, horizontal_lines * 3 + sgx_value_in_x + 8),
                        value_for_label, fill='#000000', font=font)
            pencil.line((pos_x + 9,
                         horizontal_lines * 3 + sgx_value_in_x + 8,
                         pos_x + 1.5,
                         horizontal_lines * 3 + sgx_value_in_x), fill='#000000', width=1)
            # ------------------------------------------------------------------------------------------------------
            sgx_value_in_x_end = sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                              list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                              input_right_sealing, y + 1, value_x_end)
            pencil.text((length - 35, horizontal_lines * 3 - sgx_value_in_x_end * 20 - 22),
                        str(round(sgx_value_in_x_end, 3)), fill='#000000', font=font)
            pencil.line((length - 20,
                         horizontal_lines * 3 - sgx_value_in_x_end * 20 - 12,
                         length - 1.5,
                         horizontal_lines * 3 - sgx_value_in_x_end * 20), fill='#000000', width=1)

        value_x_sgx_2 = 0.001
        # sgx_value_in_x_2 = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
        #                                   list_of_young_modulus_for_calc, input_powers, input_left_sealing,
        #                                   input_right_sealing, y + 1, value_x_sgx_2) * 20
        # pencil.line((pos_x + 1.5 + value_x_sgx * zoom_graph, horizontal_lines * 3 + sgx_value_in_x,
        #              pos_x + 1.5 + value_x_sgx_2 * zoom_graph, horizontal_lines * 3 + sgx_value_in_x_2),
        #             fill='#FF4500', width=3)
        #
        # value_x_sgx = value_x_sgx_2
        # sgx_value_in_x = sgx_value_in_x_2

        while value_x_sgx_2 < list_of_length_for_calc[y]:
            # value_x_sgx_2 += 0.001
            sgx_value_in_x_2 = - sgx_equation(list_of_length_for_calc, list_of_width_for_calc, input_list_of_loads,
                                              list_of_young_modulus_for_calc, input_powers, input_left_sealing,
                                              input_right_sealing, y + 1, value_x_sgx_2) * 20

            pencil.line((pos_x + 1.5 + value_x_sgx * zoom_graph, horizontal_lines * 3 + sgx_value_in_x,
                         pos_x + 1.5 + value_x_sgx_2 * zoom_graph, horizontal_lines * 3 + sgx_value_in_x_2),
                        fill='#FF4500', width=3)
            value_x_sgx = value_x_sgx_2
            sgx_value_in_x = sgx_value_in_x_2
            value_x_sgx_2 += 0.001
        #
        # ====================================================================================================
        if flag_labels:
            # подпись характеристик стержня
            label_length = list_length_for_label.pop()
            label_square = list_width_for_label.pop()
            label_young_modulus = input_list_of_young_modulus.pop()

            text_label = ['L', 'A;', 'E']

            if label_length != 1:
                text_label[0] = f'{label_length}L'

            if label_square != 1:
                text_label[1] = f'{label_square}A;'

            if label_young_modulus != 1:
                text_label[2] = f'{label_young_modulus}E'

            pencil.line((pos_x + 1.5, pos_y, pos_x + 1.5, pos_y + 15), fill='#000000', width=1)
            pencil.line((length - 1.5, pos_y, length - 1.5, pos_y + 15), fill='#000000', width=1)
            pencil.line((pos_x + 1.5, pos_y + 12, length - 1.5, pos_y + 12), fill='#000000', width=1)

            pencil.line((pos_x + 2, pos_y + 12, pos_x + 5, pos_y + 9), fill='#000000', width=1)
            pencil.line((pos_x + 2, pos_y + 12, pos_x + 5, pos_y + 15), fill='#000000', width=1)
            pencil.line((length - 2, pos_y + 12, length - 5, pos_y + 9), fill='#000000', width=1)
            pencil.line((length - 2, pos_y + 12, length - 5, pos_y + 15), fill='#000000', width=1)

            pencil.text(((length + pos_x) / 2, pos_y + 11), text_label[0], anchor='ms', fill='#000000', font=font)
            pencil.text(((length + pos_x) / 2, pos_y - 16), text_label[1], anchor='ms', fill='#000000', font=font)
            pencil.text(((length + pos_x) / 2, pos_y - 4), text_label[2], anchor='ms', fill='#000000', font=font)

            # подпись номеров стержней 2...N
            pencil.ellipse(((length + pos_x) / 2 - 9, pos_y + 17, (length + pos_x) / 2 + 7, pos_y + 23 + 10),
                           outline='#000000', width=1)
            pencil.text(((length + pos_x) / 2 - 1, pos_y + 20 + 10), f'{y + 1}', anchor='ms',
                        fill='#000000', font=font)

            # подпись номеров узлов 2... N - 1
            pencil.rectangle((pos_x + 5, pos_y + 5 + 12, pos_x + 16, pos_y + 17 + 12), outline='#000000',
                             width=1)
            pencil.text((pos_x + 7, pos_y + 5 + 12), f'{y + 1}', fill='#000000', font=font)
    # подпись номера N узла
    if flag_labels:
        pencil.rectangle((length - 15, pos_y + 17, length - 4, pos_y + 29), outline='#000000', width=1)
        pencil.text((length - 12, pos_y + 5 + 12), f'{y + 2}', fill='#000000', font=font)

    # заделка справа
    if input_right_sealing:
        pencil.line((length - 0.5, pos_y - 7, length - 0.5, pos_y + 7), fill='#000000', width=3)
        for i in range(int(pos_y - 7), int(pos_y + 7), 8):
            pencil.line((length - 0.5, i, length + 7.5, i - 8), fill='#000000', width=2)

    return new_img


if __name__ == '__main__':
    list_of_length = [2, 3, 3]
    list_of_width = [1, 3, 2]
    list_of_young_modulus = [1, 1, 1]
    list_of_sigma = [10, 10, 10]
    list_of_loads = [-3, 0, 3]
    powers = {'1': 0, '2': 3, '3': -3, '4': 0}
    left_sealing = True
    right_sealing = True

    img = draw_epure(list_of_length, list_of_width, list_of_young_modulus, list_of_loads, powers, left_sealing,
                     right_sealing, '#fff0ee', 1600, 900, True)
    img.show()
