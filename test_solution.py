from unittest import TestCase
from solution import get_print_str_equal_sum_unique_pairs, \
    _get_str_for_pair, \
    _get_print_str, \
    _get_dict_sum_to_list_of_pairs


class TestCaseCommon:
    def __init__(self, input, expected_output, msg):
        self.input = input
        self.expected_output = expected_output
        self.msg = msg


class Test(TestCase):
    def test_get_print_str_equal_sum_unique_pairs(self):
        test_case_list = [
            TestCaseCommon(
                input=[6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
                expected_output=(
                    "Pairs : ( 4, 12) ( 6, 10) have sum : 16\n"
                    "Pairs : ( 10, 22) ( 21, 11) have sum : 32\n"
                    "Pairs : ( 12, 21) ( 22, 11) have sum : 33\n"
                    "Pairs : ( 22, 21) ( 32, 11) have sum : 43\n"
                    "Pairs : ( 32, 21) ( 42, 11) have sum : 53\n"
                    "Pairs : ( 12, 42) ( 22, 32) have sum : 54\n"
                    "Pairs : ( 10, 54) ( 22, 42) have sum : 64"
                ),
                msg="First given input",
            ),
            TestCaseCommon(
                input=[4, 23, 65, 67, 24, 12, 86],
                expected_output=(
                    "Pairs : ( 4, 86) ( 23, 67) have sum : 90"
                ),
                msg="Second given input",
            ),
            TestCaseCommon(
                input=[1, 1, 1, 1, 1, 1, 1],
                expected_output=(
                    ""
                ),
                msg="All 1",
            ),
            TestCaseCommon(
                input=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                expected_output=(
                    "Pairs : ( 1, 1) ( 2, 0) have sum : 2"
                ),
                msg="Multiple 1. Another pair with sum 2",
            ),
            TestCaseCommon(
                input=[],
                expected_output=(
                    ""
                ),
                msg="Empty array",
            ),
            TestCaseCommon(
                input=[1, 2, 1],
                expected_output=(
                    ""
                ),
                msg="3 elements in array",
            ),
        ]
        for idx, test_case in enumerate(test_case_list):
            with self.subTest(idx=idx):
                actual_output = get_print_str_equal_sum_unique_pairs(
                    arr=test_case.input,
                )
                self.assertEqual(
                    actual_output,
                    test_case.expected_output,
                    msg=test_case.msg,
                )

    def test__get_str_for_pair(self):
        test_case_list = [
            TestCaseCommon(
                input=(1, 2),
                expected_output="( 1, 2)",
                msg="pair ( 1, 2)",
            ),
            TestCaseCommon(
                input=(0, 11),
                expected_output="( 0, 11)",
                msg="pair ( 0, 11)",
            )
        ]
        for idx, test_case in enumerate(test_case_list):
            with self.subTest(idx=idx):
                actual_output = _get_str_for_pair(test_case.input)
                self.assertEqual(
                    actual_output,
                    test_case.expected_output,
                    msg=test_case.msg,
                )

    def test__get_print_str(self):
        test_case_list = [
            TestCaseCommon(
                input={
                    21: [(10, 11), (5, 16)],
                    11: [(4, 7), (3, 8)],
                },
                expected_output=(
                    "Pairs : ( 3, 8) ( 4, 7) have sum : 11\n"
                    "Pairs : ( 5, 16) ( 10, 11) have sum : 21"
                ),
                msg="Sum should be in correct order. Pairs also should be in correct order"
            )
        ]
        for idx, test_case in enumerate(test_case_list):
            with self.subTest(idx=idx):
                actual_output = _get_print_str(test_case.input)
                self.assertEqual(
                    actual_output,
                    test_case.expected_output,
                    msg=test_case.msg,
                )

    def test__get_dict_sum_to_list_of_pairs(self):
        test_case_list = [
            TestCaseCommon(
                input=[1, 1, 1, 1, 1, 1, 1, 1, 1],
                expected_output={
                    2: [(1, 1)]
                },
                msg="all 1"
            ),
            TestCaseCommon(
                input=[1, 3, 2, 2, 4, 0],
                expected_output={
                    1: [(1, 0)],
                    2: [(2, 0)],
                    3: [(1, 2), (3, 0)],
                    4: [(1, 3), (2, 2), (4, 0)],
                    5: [(1, 4), (3, 2)],
                    6: [(2, 4)],
                    7: [(3, 4)]
                },
                msg="a long list"
            ),
            TestCaseCommon(
                input=[1, 2, 1],
                expected_output={
                    2: [(1, 1)],
                    3: [(1, 2)],
                },
                msg="input: [1 2 1]"
            )
        ]
        for idx, test_case in enumerate(test_case_list):
            with self.subTest(idx=idx):
                actual_output = _get_dict_sum_to_list_of_pairs(
                    arr=test_case.input,
                )
                self.assertEqual(
                    actual_output,
                    test_case.expected_output,
                    test_case.msg,
                )
