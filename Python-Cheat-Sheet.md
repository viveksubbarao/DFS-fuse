### Head first Python

####Introduction

```python
ChendeMacBook-Pro:~ chen$ python --version
Python 2.7.10
```

##### Comments: starts with hash character "#"  
```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```
##### Basic calculation  
```python
print(2 + 2)    # 4
print(50 - 5*6)     # 20
print((50 - 5.0*6) / 4)     # 5.0
print(8 / 5.0)  # 1.6   int / float -> float
print(8 / 5)    # 1   int / int -> int
print(8 // 5.0)  # 1.0  explicitly floor division, discards the fractional part
print(8 % 5)    # 3
print(5 * 3 + 2)
print(5 ** 2)   # 5^2
print(2 ** 7)   # 2^7 = 128

width = 20
height = 5 * 9
print(width * height)
```

In interactive mode, the last printed expression is assigned to the variable _. This variable is read-only to users.
```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

##### String
```python
print("'spam eggs'")
print('don\'t')   # don't       use \' to escape the single quote...
print("doesn't")    # doesn't   or use double quotes instead
print('"Yes," he said.')    # "Yes," he said.
print("\"Yes,\" he said.")  # "Yes," he said.
print('"Isn\'t," she said.')    # "Isn't," she said.
```

print can inteprete backslashes, but interactive mode cannot.
```python
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print '"Isn\'t," she said.'
"Isn't," she said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print, \n is included in the output
'First line.\nSecond line.'
>>> print s  # with print, \n produces a new line
First line.
Second line.
```
use *r* before string to make it raw string  
```python
print 'C:\some\name'    # print in 2 lines    here \n means newline!
print r'C:\some\name'   # C:\some\name    note the r before the quote
```

print multiple lines
```python
# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
```

String operations
```python
# String can be concatenated together(glued).
print 3 * 'un' + 'ium'  # unununium
# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
# This only works with two literals, not work with variables 
print 'Py' 'thon'   # Python
# If you want to concatenate variables or a variable and a literal, use +
a = 'py'
print a + 'thon'    # python

text = ('Put several strings within parentheses '
            'to have them joined together.')
print text  # Put several strings within parentheses to have them joined together.
```

Operate string as an array
```python
# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one
word = 'Python'
print word[0]  # 'P'    character in position 0
print word[5]  # 'n'    character in position 5
# Indices may also be negative numbers, to start counting from the right
print word[-1]  # 'n'    last character
print word[-2]  # 'o'   second-last character
print word[-6]  # 'P'
# slicing is also supported
print word[0:2]  # 'Py'    characters from position 0 (included) to 2 (excluded)
print word[2:5]  # 'tho'    characters from position 2 (included) to 5 (excluded)
print word[:2]  # 'Py'    character from the beginning to position 2 (excluded)
print word[4:]  # 'on'    characters from position 4 (included) to the end
print word[-2:] # 'on'    characters from the second-last (included) to the end
print word[:2] + word[2:]   # 'Python'
print word[4:42]    # 'on'
print word[42:]     # ''

# Python strings cannot be changed - they are immutable. Assign to string will cause error
s = 'supercalifragilisticexpialidocious'
print len(s)    # 34
```

##### List
```python
squares = [1, 4, 9, 16, 25]
print squares       # [1, 4, 9, 16, 25]
print squares[0]    # 1    indexing returns the item
print squares[-1]   # 25
print squares[-3:]  # [9, 16, 25]   slicing returns a new list
print squares[:]    # [1, 4, 9, 16, 25]
print squares + [36, 49, 64, 81, 100]   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Some list operations
```python
# Unlike strings, which are immutable, lists are a mutable
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 4 ** 3   # replace the wrong value
print cubes         # [1, 8, 27, 64, 125]
# add new items at the end of the list, by using the append() method
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print cubes     # [1, 8, 27, 64, 125, 216, 343]
# operation to slices (subarray)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print letters       # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print letters       # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print letters       # []
```

array length
```python
letters = ['a', 'b', 'c', 'd']
print len(letters)
```

2d lists
```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x     # [['a', 'b', 'c'], [1, 2, 3]]
print x[0]  # ['a', 'b', 'c']
print x[0][1]   # 'b'
```



indentation is Python’s way of grouping statements.

