from solution import get_print_str_equal_sum_unique_pairs


def input_int_ar():
    """
    take a line input from console
    :return: list of int
    """
    input_string = input()
    integer_list = [int(x) for x in input_string.split()]
    return integer_list


if __name__ == '__main__':
    while True:
        try:
            A = input_int_ar()
            print(get_print_str_equal_sum_unique_pairs(arr=A))
        except Exception as e:
            print("The input is invalid. Please give a valid input. "
                  "Exception: ", e)
