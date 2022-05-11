import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.items = LinkedList()

    def test_add_get_item(self):
        check_list = [1, 34, 'f', [231, 324, 1]]
        for element in check_list:
            self.items.add(element)

        for i in range(len(check_list)):
            self.assertEqual(self.items[i], check_list[i])

        with self.assertRaises(IndexError):
            self.items[-2]
        with self.assertRaises(IndexError):
            self.items[100]

    def test_first_element(self):
        with self.assertRaises(IndexError):
            self.items.first()
        check_list = [124, 436, 123, 54, [325, 1],
                      [325, ['f', '325'], (3, 1)], 35.4]
        first_value = (235, 'er')
        self.items.add(first_value)
        for value in check_list:
            self.items.add(value)
            self.assertEqual(self.items.first(), first_value)

    def test_last_element(self):
        with self.assertRaises(IndexError):
            self.items.last()
        check_list = [[325, 1], [325, ['f', '325'], (3, 1)], 35.4, 325]
        for value in check_list:
            self.items.add(value)
            self.assertEqual(self.items.last(), value)

    def test_extend(self):
        check_list = [[1, 2, 3, 4], [12, 3245, 235, 'fr'],
                      [35, 654, 2367, 12745678]]
        j = 0
        for list_element in check_list:
            self.items.extend(list_element)
            for i in range(len(list_element)):
                self.assertEqual(self.items[i + j], list_element[i])
            j += len(list_element)

    def test_search_in(self):
        check_list = [124, 325564, 'super', [231, '2', 1], [231, '2', 1],
                      [[124, 346], (124, 1), '325ls/'], [731, '2', 1]]
        for element in check_list:
            self.items.add(element)
        i = 0
        for element in self.items:
            self.assertEqual(element, check_list[i])
            i += 1

    def test_pop_int(self):
        check_list = [1, 2, 346, 5474, '235', 12523,
                      'dshghdak', '3246', [32545, [325], []], 326]
        self.items.extend(check_list)
        indices = [0, 5, 2, 3]
        for index in indices:
            self.assertEqual(self.items.pop(index), check_list.pop(index))
        with self.assertRaises(IndexError):
            self.items.pop(6)

    def test_add_with_position(self):

        mini_check_list = [1, 2, 3, 4]
        check_add = [2364, 43, 215]
        self.items.extend(check_add)
        position = 0
        for element in mini_check_list:
            check_add.insert(position, element)
            self.items.add(element, position)
            self.assertEqual(self.items[position], check_add[position])
            position += 1

    def test_add_with_position_left_boundary(self):
        with self.assertRaises(IndexError):
            self.items.add(325, -1)

    def test_add_with_position_right_boundary(self):
        self.items.extend([12, 346, 214, 346542])
        with self.assertRaises(IndexError):
            self.items.add(325, 5)

    def test_extend_with_position(self):
        check_list = [12, 3245, 235, 'fr', 235, 543,
                      35, 654, 2367, 12745678, 236]
        mini_check_list = [[2, 3], [4, 5], [124, 'df', 346]]
        position = 0
        self.items.extend(check_list)
        for element in mini_check_list:
            for sub_element in element:
                check_list.insert(position, sub_element)
            self.items.extend(element, position)
            self.assertEqual(self.items[position], check_list[position])
            position += 1

    def test_extend_with_position_left_boundary(self):
        with self.assertRaises(IndexError):
            self.items.extend([32532, 3521, '43'], -1)

    def test_extend_with_position_right_boundary(self):
        self.items.extend(['23564', 'ewr', '23455', 324567, [325, 235]])
        with self.assertRaises(IndexError):
            self.items.add(325, 6)

    def test_first_last_check_with_pop(self):
        check_list = [1, 2, 3, 4, 5, 234, 46, 123, 10]
        indices = [0, 1, 5]
        self.items.extend(check_list)
        self.assertEqual(self.items.first(), check_list[0])
        self.assertEqual(self.items.last(), check_list[-1])
        for index in indices:
            self.items.pop(index)
            check_list.pop(index)
            self.assertEqual(self.items.first(), check_list[0])
            self.assertEqual(self.items.last(), check_list[-1])

    def test_remove_last_occurrence(self):
        check_list = [10, 12, 'x', 34, 10, 'x', 35, 'x']
        self.items.extend(check_list)
        check_list.reverse()
        check_list.remove('x')
        check_list.reverse()
        self.items.remove_last_occurrence('x')
        for i in range(len(check_list)):
            self.assertEqual(self.items[i], check_list[i])


if __name__ == '__main__':
    unittest.main()

