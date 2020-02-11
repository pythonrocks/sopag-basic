
class Queue:
    '''
    Queue implements queue FIFO interface

    >>> q = Queue()
    >>> q.add(1)
    >>> q.add(2)
    >>> q.add(3)
    >>> print(len(q))
    3
    >>> print(q.get())
    1
    >>> print(len(q))
    2
    >>> print(q.get())
    2
    >>> print(q.get())
    3
    >>> print(q.get())
    Traceback (most recent call last):
        ...
    Exception: Queue is empty
    '''

    _length = None
    _queue = None
    _max_size = None

    def __init__(self, max_size=None):
        self._max_size = max_size
        self._queue = []
        self._length = 0

    def add(self, element):
        if self._max_size is not None and self._length+1>self._max_size:
            raise Exception("Queue size limit exceeded")

        self._queue.append(element)
        self._length += 1

    def get(self):
        if self._length == 0:
            raise Exception("Queue is empty")

        self._length -= 1
        element = self._queue[0]
        del(self._queue[0])

        return element

    def __len__(self):
        return self._length


if __name__ == "__main__":
    import doctest

    doctest.testmod()

