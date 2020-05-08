# viewtools

Viewtools provides "view" objects which can be manipulated with slices without introducing copies.

## SequenceView

```python
>>> import viewtools
>>> view = viewtools.SequenceView([2, 1, 4, 7, 4, 8, 3, 6, 4, 7])
>>> view
SequenceView([2, 1, 4, 7, 4, 8, ...])[0:10:1]
```

The usual [sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence) methods works on views:

```python
>>> view[3::2]
SequenceView([2, 1, 4, 7, 4, 8, ...])[3:10:2]
>>> list(view[3::2])
[7, 8, 6, 7]
>>> view[3::2][1]
8
>>> 6 in view[3::2]
True
>>> view[3::2].count(7)
2
>>> view[3::2].index(8)
1
>>> view[3::2].index(3)
ValueError: 3 is not in view
```

Slicing a view doesn't copy the underlying sequence unless requested:

```python
>>> view[3::2][::-1]
SequenceView([2, 1, 4, 7, 4, 8, ...])[9:1:-2]
>>> list(view[3::2][::-1])
[7, 6, 8, 7]
```

## Planning

* `StringView` which supports the usual string methods
* `ZipView`
