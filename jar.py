class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('capacity is not a non-negative int')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        total = self._size + n
        if total > self._capacity:
            raise ValueError('too much cookie')
        self._size = total

    def withdraw(self, n):
        total = self._size - n
        if total < 0:
            raise ValueError('no cookie')
        self._size = total

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
