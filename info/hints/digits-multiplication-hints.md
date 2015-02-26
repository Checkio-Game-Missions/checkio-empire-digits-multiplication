## I have no idea how to start solving this mission
You will need to separate digits from the number.
You can easily do this if convert a number in the string and work with it as with a sequence.

```python
str(20123) == "20123"
s = str(102)
s[0] == "1"
s[2] == "2"
for x in str(number):
    something
```

## I need some help to proceed with the mission
You can convert each string digit in a number with "int(s)"

```python
for s in str(number):
    n = int(s)
```
## I am gone half way through. Need help!
   
Multiply digits and accumulate the result

```python
result = 1
for s in str(number):
    n = int(s)
    ...
    result *= n # result = result * n
```

## I am stuck. I need a small hint.

In the last hint I "forgot" about zeroes. Of course you should skip them.

```python
if not n:  # if n == 0:
    continue
```
