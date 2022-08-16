# Notes

```python
>>> bc1
<BookColl: []>
>>> bc1.add(b1, b2, b3, (b4,b5), [b5,b6], {b6,bA})
<BookColl: [<Book: '1'>, <Book: '2'>, <Book: '2'>, <Book: '838224'>, <Book: '2c0bbf'>, <Book: '2c0bbf'>, <Book: 'a96d4f'>, <Book: 'A'>, <Book: 'a96d4f'>]>
>>> iter_coll(bc1)
<Book: '1'>
<Book: '2'>
<Book: '2'>
<Book: '838224'>
<Book: '2c0bbf'>
<Book: '2c0bbf'>
<Book: 'a96d4f'>
<Book: 'A'>
<Book: 'a96d4f'>
>>> b2 == b3
True
>>> b4 != b5
True
```
