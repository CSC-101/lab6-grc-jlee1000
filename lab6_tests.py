import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
        def test_selection_sort_books_1(self):
            books = [
                data.Book(['Author A'], 'C Book'),
                data.Book(['Author B'], 'A Book'),
                data.Book(['Author C'], 'B Book')
            ]
            lab6.selection_sort_books(books)
            expected_titles = ['A Book', 'B Book', 'C Book']
            actual_titles = [book.title for book in books]
            self.assertEqual(expected_titles, actual_titles)

        def test_selection_sort_books_empty(self):
            books = []
            lab6.selection_sort_books(books)
            self.assertEqual(books, [])

    if __name__ == '__main__':
        unittest.main()

    # Part 2
        # Unit Test for swap_case
        def test_swap_case_numbers_and_symbols(self):
            input_str = "123 ABC def! @#$"
            expected = "123 abc DEF! @#$"
            actual = lab6.swap_case(input_str)
            self.assertEqual(expected, actual)

        def test_swap_case_all_uppercase(self):
            input_str = "ALL UPPERCASE LETTERS"
            expected = "all uppercase letters"
            actual = lab6.swap_case(input_str)
            self.assertEqual(expected, actual)

    # Part 3
        # Unit Test for str_translate
        def test_str_translate_basic(self):
            input_str = "abcdcba"
            expected = "xbcdcbx"
            actual = lab6.str_translate(input_str, 'a', 'x')
            self.assertEqual(expected, actual)

        def test_str_translate_no_occurrences(self):
            input_str = "hello world"
            expected = "hello world"
            actual = lab6.str_translate(input_str, 'x', 'y')  # 'x' does not exist
            self.assertEqual(expected, actual)

    # Part 4
    # Unit Test for histogram
    def test_histogram_basic(self):
        input_str = "apple banana apple"
        expected = {'apple': 2, 'banana': 1}
        actual = lab6.histogram(input_str)
        self.assertEqual(expected, actual)

    def test_histogram_with_punctuation(self):
        input_str = "Hello world! Hello, hello."
        expected = {'hello': 3, 'world!': 1, 'hello,': 1}
        actual = lab6.histogram(input_str)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
