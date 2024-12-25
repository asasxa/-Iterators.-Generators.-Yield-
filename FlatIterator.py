class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_index = list()
        self.list_index.append((0, iter(self.list_of_list)))       
        print(self.list_index)
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.list_index:
            index_now, iter_now = self.list_index[-1] 
            try:
                next_el = next(iter_now)
                if isinstance(next_el, list):
                    self.list_index.append((0, iter(next_el)))
                else:
                    return next_el
            except:
                self.list_index.pop()
                if self.list_index:
                    self.list_index[-1] = (self.list_index[-1][0] + 1, self.list_index[-1][1])

        raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_1()
    test_3()
    