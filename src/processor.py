# -*- coding: UTF-8 -*
import numpy as np


def create_matrix_a(input_number_of_knots: int, list_length: list, list_width: list, list_young_modulus: list,
                    value_left_sealing: bool, value_right_sealing: bool) -> np.core.ndarray:
    """
    A function for creating a global reaction matrix
    :param input_number_of_knots: matrix size based on the number of knots
    :param list_length: List of rods' lengths
    :param list_width: List of rods' areas
    :param list_young_modulus: List of Young's modules
    :param value_left_sealing: True/False the presence of a seal on the left
    :param value_right_sealing: True/False the presence of a seal on the right
    Returns:
    :return: matrix_a - Array of matrix A (numpy.ndarray)
    """
    matrix_a = np.zeros((input_number_of_knots, input_number_of_knots))

    for index in range(0, input_number_of_knots - 2):
        value_1 = list_young_modulus[index] * list_width[index] / list_length[index]
        value_2 = list_young_modulus[index + 1] * list_width[index + 1] / list_length[index + 1]
        value = value_1 + value_2
        position = index + 1
        matrix_a[position, position] = value
        matrix_a[position, position + 1] = matrix_a[position + 1, position] = - value_2

    if value_left_sealing:
        matrix_a[0, 0] = 1
        matrix_a[0, 1] = matrix_a[1, 0] = 0
    else:
        value_0_0 = list_young_modulus[0] * list_width[0] / list_length[0]
        matrix_a[0, 0] = value_0_0
        matrix_a[0, 1] = matrix_a[1, 0] = - value_0_0

    if value_right_sealing:
        matrix_a[input_number_of_knots - 1, input_number_of_knots - 1] = 1
        matrix_a[input_number_of_knots - 2, input_number_of_knots - 1] = 0
        matrix_a[input_number_of_knots - 1, input_number_of_knots - 2] = 0
    else:
        value_end_end = list_young_modulus[-1] * list_width[-1] / list_length[-1]
        matrix_a[input_number_of_knots - 1, input_number_of_knots - 1] = value_end_end
    return matrix_a  # type(matrix_a) = np.ndarray


def create_vector_b(input_number_of_knots: int, list_length: list, list_loads: list, dict_powers: dict,
                    value_left_sealing: bool, value_right_sealing: bool) -> np.ndarray:
    """
    A function for creating a global reaction vector
    :param input_number_of_knots: vector size based on the number of knots
    :param list_length: List of rods' lengths
    :param list_loads: List of loads on rods
    :param dict_powers: Dict of powers on knots
    :param value_left_sealing: True/False the presence of a seal on the left
    :param value_right_sealing: True/False the presence of a seal on the right
    :return: vector_b - Array of vector B (numpy.ndarray)
    """
    vector_b = np.zeros((input_number_of_knots, 1))

    for index in range(1, input_number_of_knots - 1):
        length_begin = list_length[index - 1]
        value_distributed_begin = list_loads[index - 1]
        length_end = list_length[index]
        value_distributed_end = list_loads[index]

        value_begin = length_begin * value_distributed_begin / 2
        value_end = length_end * value_distributed_end / 2
        value_concentrated = dict_powers[str(index + 1)]
        vector_b[index] = value_concentrated + value_begin + value_end

    if value_left_sealing:
        vector_b[0] = 0
    else:
        length_begin = list_length[0]
        value_load_begin = list_loads[0]
        value_power_begin = dict_powers['1']
        vector_b[0] = value_power_begin + value_load_begin * length_begin / 2

    if value_right_sealing:
        vector_b[input_number_of_knots - 1] = 0
    else:
        length_end = list_length[-1]
        value_load_end = list_loads[-1]
        value_power_end = dict_powers[str(input_number_of_knots)]
        vector_b[input_number_of_knots - 1] = value_power_end + value_load_end * length_end / 2
    return vector_b  # type(vector_b) = np.ndarray


def calc_delta(input_list_of_length: list, input_list_of_width: list, input_list_of_loads: list,
               input_list_of_young_modulus: list, input_dict_powers: dict,
               input_left_sealing: bool, input_right_sealing: bool) -> np.core.ndarray:
    """
    A function for creating a global displacement vector
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_loads: List of loads on rods
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_dict_powers: Dict of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
    :return: delta - Array of vector delta (numpy.ndarray)
    """
    number_of_knots = len(input_dict_powers)
    matrix_a = create_matrix_a(number_of_knots, input_list_of_length, input_list_of_width, input_list_of_young_modulus,
                               input_left_sealing, input_right_sealing)

    vector_b = create_vector_b(number_of_knots, input_list_of_length, input_list_of_loads, input_dict_powers,
                               input_left_sealing, input_right_sealing)

    try:
        matrix_a = np.linalg.inv(matrix_a)
    except:
        np.linalg.lstsq(matrix_a, matrix_a)
    delta = np.dot(matrix_a, vector_b)
    return delta  # type(delta) = np.ndarray


def nx_equation(input_list_of_length: list, input_list_of_width: list, input_list_of_loads: list,
                input_list_of_young_modulus: list, input_dict_powers: dict,
                input_left_sealing: bool, input_right_sealing: bool,
                input_rod_number: int = None, input_value_x: float = None) -> (list, np.float64):
    """
    A function for calculating longitudinal forces at nodes and at certain points of x
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_loads: List of loads on rods
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_dict_powers: Dict of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
    :param input_rod_number: Number rod (value should be > 0) for output nx value
    :param input_value_x: X value to count N value
    :return: If input_value_x is None: answer_list - list of N(x) values;
             If input_value_x is int: answer_list - float (numpy.float64) value
    """
    delta = calc_delta(input_list_of_length, input_list_of_width, input_list_of_loads,
                       input_list_of_young_modulus, input_dict_powers, input_left_sealing, input_right_sealing)
    size_vector_delta = len(delta)
    answer_list = []
    for rod in range(size_vector_delta - 1):

        # EA/L
        value_1 = input_list_of_young_modulus[rod] * input_list_of_width[rod] / input_list_of_length[rod]
        # (delta(i+1) - delta(i)
        value_2 = delta[rod + 1] - delta[rod]
        # q*L/2
        value_3 = input_list_of_loads[rod] * input_list_of_length[rod] / 2

        if input_value_x >= 0:
            # 1 - 2x/L
            value_4 = 1 - 2 * input_value_x / input_list_of_length[rod]

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n = value_1 * value_2 + value_3 * value_4
            value_n = round(value_n[0], 3)

            answer_list.append(value_n)
            '''
            answer_list = [nx_value_in_x_in_1_rod, nx_value_in_x_in_2_rod, ..., nx_value_in_x_in_N_rod]
            '''
        else:
            # 1 - 2x/L, when x = 0: 1 - 0 = 1
            value_4_1 = 1

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n_begin = value_1 * value_2 + value_3 * value_4_1
            value_n_begin = round(value_n_begin[0], 3)

            # 1 - 2x/L, when x = L: 1 - 2 = -1
            value_4_2 = -1

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n_end = value_1 * value_2 + value_3 * value_4_2
            value_n_end = round(value_n_end[0], 3)

            answer_list.append([value_n_begin, value_n_end])
            '''
            nx_list is two-dimensional array:
            nx_list = [[nx_begin_1_rod, nx_end_1_rod], [nx_begin_2_rod, nx_end_2_rod]...,[nx_begin_n_rod, nx_end_n_rod]]
            '''
    if input_value_x >= 0:
        return answer_list[input_rod_number - 1]  # type(answer_list[input_rod_number - 1]) = numpy.float64
    else:
        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


def ux_equation(input_list_of_length: list, input_list_of_width: list, input_list_of_loads: list,
                input_list_of_young_modulus: list, input_dict_powers: dict,
                input_left_sealing: bool, input_right_sealing: bool,
                input_rod_number: int = None, input_value_x: float = None) -> (list, np.float64):
    """
    A function for calculating movements at nodes and at certain points x
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_loads: List of loads on rods
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_dict_powers: Dict of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
    :param input_rod_number: Number rod (value should be > 0) for output nx value
    :param input_value_x: X value to count N value
    :return: If input_value_x is None: answer_list - list of U(x) values;
             If input_value_x is int: answer_list - float (numpy.float64) value
    """
    delta = calc_delta(input_list_of_length, input_list_of_width, input_list_of_loads,
                       input_list_of_young_modulus, input_dict_powers, input_left_sealing, input_right_sealing)
    size_vector_delta = len(delta)

    answer_list = []
    for rod in range(size_vector_delta - 1):
        # delta(i+1) - delta(i)
        value_2 = delta[rod + 1] - delta[rod]
        # (q*L^2) / (2*E*A)
        value_3 = (input_list_of_loads[rod] * (input_list_of_length[rod] ** 2)) / (
                2 * input_list_of_young_modulus[rod] * input_list_of_width[rod])

        if input_value_x >= 0:
            # x/L
            value_1 = input_value_x / input_list_of_length[rod]
            # 1 - x/L
            value_4 = 1 - input_value_x / input_list_of_length[rod]

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n = delta[rod] + value_1 * value_2 + value_3 * value_1 * value_4
            value_n = round(value_n[0], 3)

            answer_list.append(value_n)
            '''
            answer_list = [ux_value_in_x_in_1_rod, ux_value_in_x_in_2_rod, ..., ux_value_in_x_in_N_rod]
            '''
        else:
            # x/L, when x = 0: 0/L = 0
            value_1_begin = 0
            # 1 - x/L, when x = 0: 1 - 0/L = 1
            value_4_begin = 1

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n_begin = delta[rod] + value_1_begin * value_2 + value_3 * value_1_begin * value_4_begin
            value_n_begin = round(value_n_begin[0], 3)

            # x/L, when x = L: L/L = 1
            value_1_end = 1
            # 1 - x/L, when x = L: 1 - L/L = 0
            value_4_end = 0

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n_end = delta[rod] + value_1_end * value_2 + value_3 * value_1_end * value_4_end
            value_n_end = round(value_n_end[0], 3)

            answer_list.append([value_n_begin, value_n_end])
            '''
            nx_list is two-dimensional array:
            nx_list = [[ux_begin_1_rod, ux_end_1_rod], [ux_begin_2_rod, ux_end_2_rod]...,[ux_begin_n_rod, ux_end_n_rod]]
            '''
    if input_value_x >= 0:
        return answer_list[input_rod_number - 1]  # type(answer_list[input_rod_number - 1]) = numpy.float64
    else:
        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


def sgx_equation(input_list_of_length: list, input_list_of_width: list, input_list_of_loads: list,
                 input_list_of_young_modulus: list, input_dict_powers: dict,
                 input_left_sealing: bool, input_right_sealing: bool,
                 input_rod_number: int = None, input_value_x: float = None) -> (list, np.float64):
    """
    A function for calculating normal tensions at nodes and at certain points of x
    :param input_list_of_length: List of rods' lengths
    :param input_list_of_width: List of rods' areas
    :param input_list_of_loads: List of loads on rods
    :param input_list_of_young_modulus: List of rods' young modulus values
    :param input_dict_powers: Dict of powers on knots
    :param input_left_sealing: True/False the presence of a seal on the left
    :param input_right_sealing: True/False the presence of a seal on the right
    :param input_rod_number: Number rod (value should be > 0) for output nx value
    :param input_value_x: X value to count N value
    :return: If input_value_x is None: answer_list - list of sigma(x) values;
             If input_value_x is int: answer_list - float (numpy.float64) value
    """
    if input_value_x >= 0:
        nx_value = nx_equation(input_list_of_length, input_list_of_width, input_list_of_loads,
                               input_list_of_young_modulus, input_dict_powers, input_left_sealing, input_right_sealing,
                               input_rod_number, input_value_x)
        '''
        type(nx_value) = numpy.float64
        '''
        area_value = input_list_of_width[input_rod_number - 1]
        answer_value = nx_value / area_value
        return answer_value  # type(answer_value) = numpy.float64

    else:
        nx_list = nx_equation(input_list_of_length, input_list_of_width, input_list_of_loads, input_list_of_young_modulus,
                              input_dict_powers, input_left_sealing, input_right_sealing, None, -1)
        '''
        nx_list is two-dimensional array:
        nx_list = [[nx_begin_1_rod, nx_end_1_rod], [nx_begin_2_rod, nx_end_2_rod]...,[nx_begin_n_rod, nx_end_n_rod]]
        '''
        answer_list = []
        for nx_index in range(len(nx_list)):  # for nx_index in range (N rods):
            nx_list_indexed = nx_list[nx_index]  # nx_list_indexed = [nx_begin_(nx_index)_rod, nx_end_(nx_index)_rod]
            width = input_list_of_width[nx_index]
            result_list = [round(value / width, 3) for value in nx_list_indexed]

            answer_list.append(result_list)
            '''
            answer_list = [sgx_value_in_x_in_1_rod, sgx_value_in_x_in_2_rod, ..., sgx_value_in_x_in_N_rod]
            '''
        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


if __name__ == '__main__':
    # list_of_length = [L-№1, L-№2, ..., L-№ N]
    list_of_length = [2, 3, 3]
    # list_of_width = [A-№1, A-№2, ..., A-№ N]
    list_of_width = [1, 3, 2]
    # list_of_young_modulus = [E-№1, E-№2, ..., E-№ N]
    list_of_young_modulus = [1, 1, 1]
    # list_of_sigma = [E-№1, E-№2, ..., E-№ N]
    list_of_sigma = [10, 10, 10]
    # list_of_loads = [q-№1, q-№2, ..., q-№ N]
    list_of_loads = [-3, 0, 3]
    # powers = {'1': F-№1, '2': F-№2, ..., 'N': F-№ N, 'N+1': F-№ N+1}
    powers = {'1': 0, '2': 3, '3': -3, '4': 0}
    # left_sealing = True/False
    left_sealing = True
    # right_sealing = True/False
    right_sealing = True
    # value_x = X or None
    value_x = -1
    # rod_number = N or None
    rod_number = 1

    nx = nx_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                     right_sealing, rod_number, value_x)
    print('nx_list:', nx)

    ux = ux_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                     right_sealing, rod_number, value_x)
    print('ux_list:', ux)

    sgx = sgx_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                       right_sealing, rod_number, value_x)
    print('sgx_list:', sgx)

    # values nx, ux, sgx in a certain value of x
    nx_in_x = nx_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                          right_sealing, input_rod_number=1, input_value_x=2)
    print('nx_value in x=2 in 1 rod :', nx_in_x)

    ux_in_x = ux_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                          right_sealing, input_rod_number=1, input_value_x=2)
    print('ux_value in x=2 in 1 rod :', ux_in_x)

    sgx_in_x = sgx_equation(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers, left_sealing,
                            right_sealing, input_rod_number=1, input_value_x=2)
    print('sgx_value in x=2 in 1 rod :', sgx_in_x)
