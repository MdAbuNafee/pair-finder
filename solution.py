from collections import defaultdict
import copy


def get_print_str_equal_sum_unique_pairs(arr):
    """

    :param arr: array of int
    :return: string
    """
    dict_sum_to_list_of_pairs = _get_dict_sum_to_list_of_pairs(
        arr=arr,
    )
    print_str = _get_print_str(
        dict_sum_to_list_of_pairs=dict_sum_to_list_of_pairs,
    )
    return print_str


def _get_str_for_pair(pair):
    """

    :param pair: any pair like (1,2)
    :return: string
    """
    return "( " + str(pair[0]) + ", " + str(pair[1]) + ")"


def _get_print_str(dict_sum_to_list_of_pairs):
    """

    :param dict_sum_to_list_of_pairs: dictionary of int to list of pairs
    :return: string
    """
    ret_str_list = []
    sorted_list_of_sum = sorted(list(dict_sum_to_list_of_pairs.keys()))
    for current_sum in sorted_list_of_sum:
        list_of_pairs = copy.deepcopy(dict_sum_to_list_of_pairs[current_sum])
        if len(list_of_pairs) > 1:
            list_of_pairs.sort()
            cur_str = f"Pairs : " \
                      f"{' '.join(_get_str_for_pair(p) for p in list_of_pairs)} " \
                      f"have sum : {current_sum}"
            ret_str_list.append(cur_str)
    return "\n".join(ret_str_list)


def _get_dict_sum_to_list_of_pairs(arr):
    """

    :param arr: array of int
    :return: dictionary of int to list of pairs
    """
    dict_sum_to_list_of_pairs = defaultdict(list)
    sorted_pair_set = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            _populate_dict_of_sum_to_list_of_pairs(
                val1=arr[i],
                val2=arr[j],
                dict_sum_to_list_of_pairs=dict_sum_to_list_of_pairs,
                sorted_pair_set=sorted_pair_set,
            )
    return dict_sum_to_list_of_pairs


def _populate_dict_of_sum_to_list_of_pairs(
        val1,
        val2,
        dict_sum_to_list_of_pairs,
        sorted_pair_set,
):
    """

    :param val1: int
    :param val2: int
    :param dict_sum_to_list_of_pairs: dictionary of int to list of pairs
    :param sorted_pair_set: set of sorted pairs

    This method doesn't return anything. Just do some in place modification of
    the given parameters : dict_sum_to_list_of_pairs and sorted_pair_set
    """
    sum_of_value = val1 + val2
    sorted_pair = tuple(sorted((val1, val2)))
    if sorted_pair in sorted_pair_set:
        return
    sorted_pair_set.add(sorted_pair)
    dict_sum_to_list_of_pairs[sum_of_value].append((val1, val2))
