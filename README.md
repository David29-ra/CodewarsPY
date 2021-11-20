# Codewars Kata on Python

## Find the lucky numbers

Write a function filterLucky/filter_lucky() that accepts a list of integers and filters the list to only include the elements that contain the digit 7.

For example,
```python
filterLucky [1,2,3,4,5,6,7,68,69,70,15,17]
[7,70,17]
```

>*My Solution on lucky.py file*

<br>

## Evil or Odious

The number n is Evil if it has an even number of 1's in its binary representation.
The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary representation.
The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

>*My Solution on odious.py file*

<br>

## Pyramid Slide Down

### Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

```python
   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
```

Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function longestSlideDown (in ruby/crystal/julia: longest_slide_down) that takes a pyramid representation as argument and returns its' largest 'slide down'. For example,

```python
longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```

>*My Solution on pyramid.py file*

<br>

## Are they square?

Write a function that checks whether all elements in an array are square numbers. The function should be able to take any number of array elements.

Your function should return true if all elements in the array are square numbers and false if not.

An empty array should return undefined / None / nil /false (for C). You can assume that all array elements will be positive integers.

Examples:

```python
is_square([1, 4, 9, 16]) --> True

is_square([3, 4, 7, 9]) --> False

is_square([]) --> None
```

>*My Solution on square.py file*

<br>

### I love solving katas!

<br/><br/>

*Made by Monito Inc. 🙊*