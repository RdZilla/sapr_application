# -*- coding: UTF-8 -*
from PIL import Image, ImageDraw, ImageFont


def draw_picture(input_list_of_length: list, input_list_of_width: list, input_list_of_loads: list,
                 input_list_of_young_modulus: list, input_dict_powers: dict, input_left_sealing: bool,
                 input_right_sealing: bool, bg_color: str = '#fff0ee', window_length: int = 800,
                 window_width: int = 600, flag_labels: bool = True) -> Image.Image:

    """
    The function of drawing a picture in png format (for the preprocessor tab)
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_loads: List of loads on rods
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_dict_powers: List of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
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
    # копия массивов длины и ширины для подписей характеристик стержней
    list_length_for_label = []
    list_width_for_label = []
    if flag_labels:
        list_length_for_label = input_list_of_length.copy()
        list_length_for_label.reverse()
        list_width_for_label = input_list_of_width.copy()
        list_width_for_label.reverse()
        input_list_of_young_modulus.reverse()

    win_wth_ctr = window_width / 2

    # решение проблемы: излишне низкая ширина стержня
    if win_wth_ctr / min(input_list_of_width) > 15:
        input_list_of_width = [y * 40 for y in input_list_of_width]

    # решение проблемы: отрисовка эпюры за пределами экрана по ширине
    if max(input_list_of_width) >= window_width - 150:
        decrease_y = (window_width - 150) / max(input_list_of_width)
        input_list_of_width = [y * decrease_y for y in input_list_of_width]

    # решение проблемы: излишняя разница ширины стержней
    if max(input_list_of_width) / min(input_list_of_width) > 5:
        list_of_y_common = []
        for y in input_list_of_width:
            if y == max(input_list_of_width):
                pass
            else:
                if max(input_list_of_width) / y > 5:
                    zoom_y = (max(input_list_of_width) / y) / 10
                    y *= zoom_y
            list_of_y_common.append(y)
        input_list_of_width = list_of_y_common

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

    # центральная горизонтальная линия
    pencil.line((0, win_wth_ctr, window_length, win_wth_ctr), fill='#A9A9A9', width=1)

    input_list_of_length.reverse()
    input_list_of_width.reverse()

    # координаты x 1 стержня
    pos_x = 50
    length = input_list_of_length.pop() + pos_x
    # координаты y 1 стержня
    width = input_list_of_width.pop()
    pos_y = win_wth_ctr - width / 2
    new_width = pos_y + width
    # отрисовка стержня
    pencil.rectangle((pos_x, pos_y, length, new_width), outline='#000000', width=3)

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

        pencil.line((pos_x + 1.5, new_width, pos_x + 1.5, new_width + 15), fill='#000000', width=1)
        pencil.line((length - 1.5, new_width, length - 1.5, new_width + 15), fill='#000000', width=1)
        pencil.line((pos_x + 1.5, new_width + 12, length - 1.5, new_width + 12), fill='#000000', width=1)

        pencil.line((pos_x + 2, new_width + 12, pos_x + 5, new_width + 9), fill='#000000', width=1)
        pencil.line((pos_x + 2, new_width + 12, pos_x + 5, new_width + 15), fill='#000000', width=1)
        pencil.line((length - 2, new_width + 12, length - 5, new_width + 9), fill='#000000', width=1)
        pencil.line((length - 2, new_width + 12, length - 5, new_width + 15), fill='#000000', width=1)

        pencil.text(((length + pos_x) / 2, new_width + 11), text_label[0], anchor='ms', fill='#000000', font=font)
        pencil.text(((length + pos_x) / 2, pos_y - 16), text_label[1], anchor='ms', fill='#000000', font=font)
        pencil.text(((length + pos_x) / 2, pos_y - 4), text_label[2], anchor='ms', fill='#000000', font=font)

        # подпись номеров стержней
        pencil.ellipse(((length + pos_x) / 2 - 9, new_width + 17, (length + pos_x) / 2 + 7, new_width + 33),
                       outline='#000000', width=1)
        pencil.text(((length + pos_x) / 2 - 1.5, new_width + 30), f'1', anchor='ms', fill='#000000', font=font)

        # отрисовка сил 1 узла
        power = input_dict_powers['1']
        if power == 1 or power == -1:
            text_label_power = 'F'
        else:
            text_label_power = f'{abs(power)}F'

        if power == 0:
            pass
        elif power > 0:
            pencil.line((pos_x + 3, win_wth_ctr - 1, pos_x + 45, win_wth_ctr - 1),
                        fill=f'#800000', width=2)
            pencil.line((pos_x + 45, win_wth_ctr, pos_x + 45 - 5, win_wth_ctr - 5),
                        fill=f'#800000', width=2)
            pencil.line((pos_x + 45 - 1, win_wth_ctr, pos_x + 45 - 6, win_wth_ctr + 5),
                        fill=f'#800000', width=2)
            pencil.text(((pos_x + 45 + pos_x) / 2, win_wth_ctr + 15), text_label_power, anchor='ms',
                        fill=f'#800000', font=font)
        elif power < 0:
            pencil.line((pos_x - 3, win_wth_ctr, 5, win_wth_ctr), fill=f'#00008B', width=2)
            pencil.line((6, win_wth_ctr - 1, 11, win_wth_ctr - 6), fill=f'#00008B', width=2)
            pencil.line((5, win_wth_ctr - 1, 10, win_wth_ctr + 4), fill=f'#00008B', width=2)
            pencil.text(((5 + pos_x) / 2, win_wth_ctr + 15), text_label_power, anchor='ms', fill=f'#00008B', font=font)

        # подпись номера 1 узла
        pencil.rectangle((pos_x + 5, new_width + 17, pos_x + 16, new_width + 29), outline='#000000', width=1)
        pencil.text((pos_x + 8, new_width + 17), f'1', fill='#000000', font=font)

        # отрисовка нагрузок 1 стержня
        interval = int((length - pos_x + 4) / 10)
        pos_x_for_arrows = int(pos_x + 4)
        length_for_arrows = int(length)

        value_loads = input_list_of_loads[0]

        if value_loads == 1 or value_loads == -1:
            text_label_loads = 'q'
        else:
            text_label_loads = f'{abs(value_loads)}q'

        if value_loads == 0:
            pass
        elif value_loads > 0:
            for arrow in range(pos_x_for_arrows, length_for_arrows - interval, 2 * interval):
                pencil.line((arrow, win_wth_ctr, arrow + interval, win_wth_ctr),
                            fill='#E0851F', width=2)
                pencil.line((arrow + interval - 1, win_wth_ctr, arrow + interval - 4, win_wth_ctr - 3),
                            fill='#E0851F', width=2)
                pencil.line((arrow + interval - 2, win_wth_ctr + 2, arrow + interval - 5, win_wth_ctr + 5),
                            fill='#E0851F', width=2)
            pencil.text(((length + pos_x) / 2, win_wth_ctr - 7), text_label_loads, anchor='ms',
                        fill='#E0851F', font=font)
        elif value_loads < 0:
            for arrow in range(pos_x_for_arrows, length_for_arrows - interval, 2 * interval):
                pencil.line((arrow, win_wth_ctr, arrow + interval, win_wth_ctr),
                            fill='#008000', width=2)
                pencil.line((arrow + 2, win_wth_ctr - 1, arrow + 5, win_wth_ctr - 4),
                            fill='#008000', width=2)
                pencil.line((arrow + 1, win_wth_ctr + 1, arrow + 4, win_wth_ctr + 4),
                            fill='#008000', width=2)
                pencil.text(((length + pos_x) / 2, win_wth_ctr - 7), text_label_loads, anchor='ms',
                            fill='#008000', font=font)

    # заделка слева
    if input_left_sealing:
        pencil.line((pos_x + 1.5, pos_y - 7, pos_x + 1.5, new_width + 7), fill='#000000', width=3)
        for y in range(int(pos_y - 7), int(new_width + 7), 8):
            pencil.line((pos_x + 1.5, y, pos_x - 6.5, y + 8), fill='#000000', width=2)

    # отрисовка стержней №2...N, нагрузок 2...N, отрисовка сил узлов №2...N-1
    y = 0
    for y in range(1, count_rods):
        # координаты x
        pos_x = length - 1.5
        length = input_list_of_length.pop() + pos_x
        # координаты y
        width = input_list_of_width.pop()
        pos_y = win_wth_ctr - width / 2
        new_width = pos_y + width
        # отрисовка стержня № y (начиная с 2-ого)
        pencil.rectangle((pos_x, pos_y, length, new_width), outline='#000000', width=3)
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

            pencil.line((pos_x + 1.5, new_width, pos_x + 1.5, new_width + 15), fill='#000000', width=1)
            pencil.line((length - 1.5, new_width, length - 1.5, new_width + 15), fill='#000000', width=1)
            pencil.line((pos_x + 1.5, new_width + 12, length - 1.5, new_width + 12), fill='#000000', width=1)

            pencil.line((pos_x + 2, new_width + 12, pos_x + 5, new_width + 9), fill='#000000', width=1)
            pencil.line((pos_x + 2, new_width + 12, pos_x + 5, new_width + 15), fill='#000000', width=1)
            pencil.line((length - 2, new_width + 12, length - 5, new_width + 9), fill='#000000', width=1)
            pencil.line((length - 2, new_width + 12, length - 5, new_width + 15), fill='#000000', width=1)

            pencil.text(((length + pos_x) / 2, new_width + 11), text_label[0], anchor='ms', fill='#000000', font=font)
            pencil.text(((length + pos_x) / 2, pos_y - 16), text_label[1], anchor='ms', fill='#000000', font=font)
            pencil.text(((length + pos_x) / 2, pos_y - 4), text_label[2], anchor='ms', fill='#000000', font=font)

            # подпись номеров стержней 2...N
            pencil.ellipse(((length + pos_x) / 2 - 9, new_width + 17, (length + pos_x) / 2 + 7, new_width + 23 + 10),
                           outline='#000000', width=1)
            pencil.text(((length + pos_x) / 2 - 1, new_width + 20 + 10), f'{y + 1}', anchor='ms',
                        fill='#000000', font=font)

            # Отрисовка сил узла № y + 1 (начиная с 2-ого) ... N - 1
            power = input_dict_powers[str(y + 1)]

            if power == 1 or power == -1:
                text_label_power = 'F'
            else:
                text_label_power = f'{abs(power)}F'

            if power == 0:
                pass
            elif power > 0:
                pencil.line((pos_x + 3, win_wth_ctr - 1, pos_x + 45, win_wth_ctr - 1),
                            fill=f'#800000', width=2)
                pencil.line((pos_x + 45, win_wth_ctr, pos_x + 45 - 5, win_wth_ctr - 5),
                            fill=f'#800000', width=2)
                pencil.line((pos_x + 45 - 1, win_wth_ctr, pos_x + 45 - 6, win_wth_ctr + 5),
                            fill=f'#800000', width=2)
                pencil.text(((pos_x + 45 + pos_x) / 2, win_wth_ctr + 15), text_label_power, anchor='ms',
                            fill=f'#800000', font=font)
            elif power < 0:
                pencil.line((pos_x - 3, win_wth_ctr, pos_x - 45, win_wth_ctr),
                            fill=f'#00008B', width=2)
                pencil.line((pos_x - 45 + 1, win_wth_ctr - 1, pos_x - 45 + 6, win_wth_ctr - 6),
                            fill=f'#00008B', width=2)
                pencil.line((pos_x - 45, win_wth_ctr - 1, pos_x - 45 + 5, win_wth_ctr + 4),
                            fill=f'#00008B', width=2)
                pencil.text(((pos_x - 45 + pos_x) / 2, win_wth_ctr + 15), text_label_power, anchor='ms',
                            fill=f'#00008B', font=font)

            # подпись номеров узлов 2... N - 1
            pencil.rectangle((pos_x + 5, new_width + 5 + 12, pos_x + 16, new_width + 17 + 12), outline='#000000',
                             width=1)
            pencil.text((pos_x + 7, new_width + 5 + 12), f'{y + 1}', fill='#000000', font=font)

            # отрисовка нагрузок стержней 2...N
            interval = int((length - pos_x + 4) / 10)
            pos_x_for_arrows = int(pos_x + 4)
            length_for_arrows = int(length)

            value_loads = input_list_of_loads[y]

            if value_loads == 1 or value_loads == -1:
                text_label_loads = 'q'
            else:
                text_label_loads = f'{abs(value_loads)}q'

            if value_loads == 0:
                pass
            elif value_loads > 0:
                for arrow in range(pos_x_for_arrows, length_for_arrows - interval, 2 * interval):
                    pencil.line((arrow, win_wth_ctr, arrow + interval, win_wth_ctr),
                                fill='#E0851F', width=2)
                    pencil.line((arrow + interval - 1, win_wth_ctr, arrow + interval - 4, win_wth_ctr - 3),
                                fill='#E0851F', width=2)
                    pencil.line((arrow + interval - 2, win_wth_ctr + 2, arrow + interval - 5, win_wth_ctr + 5),
                                fill='#E0851F', width=2)
                pencil.text(((length + pos_x) / 2, win_wth_ctr - 7), text_label_loads, anchor='ms',
                            fill='#E0851F', font=font)
            elif value_loads < 0:
                for arrow in range(pos_x_for_arrows, length_for_arrows - interval, 2 * interval):
                    pencil.line((arrow, win_wth_ctr, arrow + interval, win_wth_ctr),
                                fill='#008000', width=2)
                    pencil.line((arrow + 2, win_wth_ctr - 1, arrow + 5, win_wth_ctr - 4),
                                fill='#008000', width=2)
                    pencil.line((arrow + 1, win_wth_ctr + 1, arrow + 4, win_wth_ctr + 4),
                                fill='#008000', width=2)
                pencil.text(((length + pos_x) / 2, win_wth_ctr - 7), text_label_loads, anchor='ms',
                            fill='#008000', font=font)

    # отрисовка сил N (последнего) узла
    if flag_labels:
        power = input_dict_powers[str(len(input_dict_powers))]
        if power == 1 or power == -1:
            text_label_power = 'F'
        else:
            text_label_power = f'{abs(power)}F'

        if power == 0:
            pass
        elif power > 0:
            pencil.line((length + 3, win_wth_ctr - 1, length + 45, win_wth_ctr - 1),
                        fill=f'#800000', width=2)
            pencil.line((length + 45, win_wth_ctr, length + 45 - 5, win_wth_ctr - 5),
                        fill=f'#800000', width=2)
            pencil.line((length + 45 - 1, win_wth_ctr, length + 45 - 6, win_wth_ctr + 5),
                        fill=f'#800000', width=2)
            pencil.text(((length + 45 + length) / 2, win_wth_ctr + 15), text_label_power, anchor='ms',
                        fill=f'#800000', font=font)
        elif power < 0:
            pencil.line((length - 3, win_wth_ctr, length - 45, win_wth_ctr),
                        fill=f'#00008B', width=2)
            pencil.line((length - 45 + 1, win_wth_ctr - 1, length - 45 + 6, win_wth_ctr - 6),
                        fill=f'#00008B', width=2)
            pencil.line((length - 45, win_wth_ctr - 1, length - 45 + 5, win_wth_ctr + 4),
                        fill=f'#00008B', width=2)
            pencil.text(((length - 45 + length) / 2, win_wth_ctr + 15), text_label_power, anchor='ms',
                        fill=f'#00008B', font=font)

        # подпись номера N узла
        pencil.rectangle((length - 15, new_width + 17, length - 4, new_width + 29), outline='#000000', width=1)
        pencil.text((length - 12, new_width + 5 + 12), f'{y + 2}', fill='#000000', font=font)

    # заделка справа
    if input_right_sealing:
        pencil.line((length - 0.5, pos_y - 7, length - 0.5, new_width + 7), fill='#000000', width=3)
        for i in range(int(pos_y - 7), int(new_width + 7), 8):
            pencil.line((length - 0.5, i, length + 7.5, i - 8), fill='#000000', width=2)

    # Блок: описание обозначений на чертеже
    if flag_labels:
        pencil.line((0, window_width - 45 + 6, window_length, window_width - 45 + 6), fill='#000000', width=1)
        pencil.line((0, window_width - 42 + 6, window_length, window_width - 42 + 6), fill='#000000', width=1)

        # описание нумерации узлов
        step_div_lines = window_length / 4

        pencil.rectangle(((step_div_lines / 2) - 58,
                          window_width - 22,
                          (step_div_lines / 2) - 47,
                          window_width - 10),
                         outline='#000000', width=1)
        pencil.text(((step_div_lines / 2) - 55, window_width - 22), '1',
                    fill='#000000', font=font)
        pencil.text(((step_div_lines / 2) - 43, window_width - 22), '- нумерация узлов',
                    fill='#000000', font=font)

        # разделительная линия
        pencil.line((step_div_lines, window_width - 39, step_div_lines, window_width), fill='#000000', width=1)

        # описание нумерации стержней
        step_div_lines_2 = step_div_lines * 2

        pencil.ellipse(((step_div_lines_2 + step_div_lines) / 2 - 72,
                        window_width - 24,
                        (step_div_lines_2 + step_div_lines) / 2 - 56,
                        window_width - 8), outline='#000000', width=1)
        pencil.text(((step_div_lines_2 + step_div_lines) / 2 - 66, window_width - 22), '1',
                    fill='#000000', font=font)
        pencil.text(((step_div_lines_2 + step_div_lines) / 2 - 52, window_width - 22), '- нумерация стержней',
                    fill='#000000', font=font)

        # разделительная линия
        pencil.line((step_div_lines_2, window_width - 39, step_div_lines_2, window_width), fill='#000000', width=1)

        # описание сосредоточенных нагрузок
        step_div_lines_3 = step_div_lines * 3

        pencil.line(((step_div_lines_3 + step_div_lines_2) / 2 - 95,
                     window_width - 15,
                     (step_div_lines_3 + step_div_lines_2) / 2 - 53,
                     window_width - 15),
                    fill=f'#800000', width=2)
        pencil.line(((step_div_lines_3 + step_div_lines_2) / 2 - 54,
                     window_width - 15,
                     (step_div_lines_3 + step_div_lines_2) / 2 - 57,
                     window_width - 18),
                    fill=f'#800000', width=2)
        pencil.line(((step_div_lines_3 + step_div_lines_2) / 2 - 55,
                     window_width - 13,
                     (step_div_lines_3 + step_div_lines_2) / 2 - 58,
                     window_width - 10),
                    fill=f'#800000', width=2)
        pencil.text(((step_div_lines_3 + step_div_lines_2 + 42) / 2 - 95,
                     window_width - 19),
                    '2F', anchor='ms', fill=f'#800000', font=font)
        pencil.text(((step_div_lines_3 + step_div_lines_2) / 2 - 49,
                     window_width - 22),
                    '- сосредоточенные нагрузки', fill='#000000', font=font)

        # разделительная линия
        pencil.line((step_div_lines_3, window_width - 39, step_div_lines_3, window_width), fill='#000000', width=1)

        # описание распределённых нагрузок
        pencil.line(((step_div_lines_3 + window_length) / 2 - 92,
                     window_width - 15,
                     (step_div_lines_3 + window_length) / 2 - 50,
                     window_width - 15),
                    fill='#E0851F', width=2)
        pencil.line(((step_div_lines_3 + window_length) / 2 - 51,
                     window_width - 15,
                     (step_div_lines_3 + window_length) / 2 - 54,
                     window_width - 18),
                    fill='#E0851F', width=2)
        pencil.line(((step_div_lines_3 + window_length) / 2 - 52,
                     window_width - 13,
                     (step_div_lines_3 + window_length) / 2 - 55,
                     window_width - 10),
                    fill='#E0851F', width=2)
        pencil.text(((step_div_lines_3 + window_length + 42) / 2 - 92,
                     window_width - 20),
                    '2q', anchor='ms', fill='#E0851F', font=font)
        pencil.text(((step_div_lines_3 + window_length) / 2 - 46,
                     window_width - 22),
                    '- распределённые нагрузки', fill='#000000', font=font)

    return new_img


if __name__ == '__main__':

    list_of_length = [2, 3, 3]
    list_of_width = [1, 300, 2]
    list_of_young_modulus = [1, 1, 1]
    list_of_sigma = [10, 10, 10]
    list_of_loads = [-3, 0, 3]
    powers = {'1': 0, '2': 3, '3': -3, '4': 0}
    left_sealing = True
    right_sealing = True

    img = draw_picture(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, True, True, '#fff0ee', 1600,
                       900, True)
    img.save('resources/pictures/image.png')
