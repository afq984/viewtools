import reprlib
import collections.abc
from typing import Sequence, Any


class SequenceView:
    __slots__ = ('_seq', '_range')

    def __init__(self, seq: Sequence[Any], *, _range=None):
        if not isinstance(seq, collections.abc.Sequence):
            raise TypeError(f'seq must be a sequence, not {type(seq).__name__}')
        self._seq = seq
        if _range is None:
            self._range = range(len(seq))
        else:
            self._range = _range

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._seq[self._range[item]]
        if isinstance(item, slice):
            return self.__class__(self._seq, _range=self._range[item])
        raise TypeError(
            f'{self.__class__.__name__} indices must be integers or slices, '
            f'not {type(item).__name__}')

    def __len__(self):
        return len(self._range)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}({reprlib.repr(self._seq)})'
            f'[{self.slice.start}:{self.slice.stop}:{self.slice.step}]'
        )

    @property
    def slice(self):
        return slice(self._range.start, self._range.stop, self._range.step)

    def index(self, value, start=0, stop=None):
        obj = self
        if start != 0 or stop is not None:
            obj = self[start:stop]
        for i, v in enumerate(obj):
            if v is value or v == value:
                return i
        raise ValueError(f'{value!r} is not in view')

    def count(self, value):
        return sum(v is value or v == value for v in self)
