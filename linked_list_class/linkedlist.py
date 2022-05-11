class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        if index < 0:
            raise IndexError
        for _ in range(index):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def __contains__(self, item):
        for index in range(self.__len):
            current = self.__getitem__(index)
            if item == current:
                return True
        return False

    def __repr__(self):
        representative_list = []
        current = self.__head
        representative_list.append(current.value)
        for _ in range(self.__len - 1):
            current = current.get_next()
            representative_list.append(current.value)
        return repr(representative_list)

    def add(self, value, position=None):
        if position is None:
            self.__len += 1
            new_item = LinkedListItem(value)
            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item
        else:
            if position > self.__len:
                raise IndexError(f"Desired position {position}, "
                                 f"but list's length is {self.__len}.")
            elif position < 0:
                raise IndexError
            if position == 0:
                self.__len += 1
                new_item = LinkedListItem(value)
                if not self.__head:
                    self.__head = new_item
                    self.__tail = new_item
                else:
                    new_item.set_next(self.__head)
                    self.__head = new_item
            elif position == self.__len:
                self.__len += 1
                new_item = LinkedListItem(value)
                self.__tail.set_next(new_item)
                self.__tail = new_item
            else:
                self.__len += 1
                new_item = LinkedListItem(value)
                current = self.__head
                for i in range(position - 1):
                    current = current.get_next()
                next_item = current.get_next()
                current.set_next(new_item)
                new_item.set_next(next_item)
        return self

    def extend(self, arg_list: list, position=None):
        for element in arg_list:
            self.add(element, position)
        return self

    def first(self):
        if self.__len == 0:
            raise IndexError('Linked list is empty')
        return self.__head.value

    def last(self):
        if self.__len == 0:
            raise IndexError('Linked list is empty')
        return self.__tail.value

    def pop(self, index=None):
        if index is None or index == self.__len - 1:
            current = self.__head
            while current.get_next().has_next():
                current = current.get_next()
            popped_element = current.get_next()
            self.__tail = current
            current.set_next(None)
            self.__len -= 1
        elif index > self.__len - 1:
            raise IndexError(f"Desired index is {index},"
                             f" but last element index is {self.__len - 1}.")
        elif index == 0:
            popped_element = self.__head
            new_next_element = popped_element.get_next()
            self.__head = new_next_element
            self.__len -= 1
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.get_next()
            popped_element = current.get_next()
            new_next_element = popped_element.get_next()
            current.set_next(new_next_element)
            self.__len -= 1
        return popped_element.value

    def remove_last_occurrence(self, element):
        if element not in self:
            raise ValueError(f'No such element in LinkedList: {element}')
        current = self.__head
        index = 0
        last_element_index = 0
        for _ in range(self.__len):
            if current.value == element:
                last_element_index = index
            current = current.get_next()
            index += 1
        self.pop(last_element_index)

        return self
