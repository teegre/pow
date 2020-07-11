# [PowerText] version 0.0.2 (08-2017)

[PowerText] is a LISP-like functionnal programming language written in Python 3.6.

**This repository is read-only.**

## 1. Syntax

> Similar to LISP, but parentheses have been replaced by square brackets. So for adding 2 and 2, just type: `[+ 2 2]`  which should return 4.

> Comments are preceded by `;;` or `#`.

## 2. Types

> There are seven types in [PowerText]:

* **string**: "Abc" or 'Abc'
* **int**: `123`
* **real**: `123.45`
* **frac**: `22/7 [1+ [sqrt 5]]/2`
* **list**: `(1 2 3) ("a" "b" "c")`
* **bool**: `true false`
* **null**

> Types can be checked using the `[type]` function.
`[tostr]` converts a **number** into a **string**.
`[tonum]` converts a **string** into a **number**.

## 3. Operators
* **\+** addition
* **\++** increment variable
* **\-** substraction
* **\--** decrement variable
* \* multiplication
* ** power of two
* *** power
* **/** division
* **//** integer division
* **%** modulo
* **<<** bitwise left shift
* **\>>** bitwise right shift
* **=** equal
* **<** less
* **<=** less or equal
* **\>** greater
* **\>=** greater or equal
* **!=** not equal
* **and**
* **or**
* **xor**
* **not**

## 4. Variable assignment

`[set b "Hello, World!"]`

Note that every function returns a value so it is possible to nest functions inside functions. For example, let's say you also need a variable "a" equal to "b", you would write:

`[set a [set b "Hello, World!"]]`

The string "Hello, World" is first assigned to variable "b" and then, the result of the «set» function is assigned to variable "a".

To assign a list to a variable:

`[set L (0 1 2 3 4 5 6 7 8 9)]`

`[set L ()] #to assign an empty list`

It is also possible to create global variables with `[setg]`.

*For more information about lists, see chapter 6.*

## 4 ?, for and while loops.

### 4.1 ?

In [PowerText], "?" is equivalent to if, and its syntax is as follow:

[? condition: dothis]

[? condition: dothis; dothat]

Example: `[? [= a 0]: [++ a]; [-- a]]`

Note that "dothis" and "dothat" can be one or more statements:

[? condition:

dothis

and-this

and-also-this;

do-that

and-that-too]

### 4.2 For loop:

[for variable start end: dothis]

[for variable start end step: dothis]

Example: `[for i 1 10: [echo i "\n"]]`

### 4.3 While loop:

[while condition: dothis]

Example: `[while [< a 10]: [echo a "\n"] [++ a]]`

Note: since ?, for and while are functions, they will return a value.

Examples:
```
[set x [rndr 1 100]]
[set a [? [< x 50]: "yes"; "no"]]

x
25

a
"yes"
```

To exit a loop, use the `[exit]` function.

```
[set a 0]
[set b [while true:
  [++ a]
  [? [= a 100]: [exit a]]]]

[= a b]

true
```
To skip statements in a loop, use the `[skip]` function.

```
[set i 0]
[while [< i 30]:
  [++ i]
  [? [= [% i 2] 0]: [skip]]
  [echo i " "]]

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
```
## 5. Functions

### 5.1 Function definition

[def name [parameters]: body]

The last statement is returned by the function

```
[def double [x]: [+ x x]]
```

To call a function:

```
[set x 4]
[double x]

8
```

### 5.2 Lambda function

Lambda functions have to be assigned to a variable:

[set variable [lambda [parameters]: expression]]

Example:

`[set square [lambda [x]: [* x x]]]`

To call a lambda:

```
[@square 2]

4
```

## 6. Lists

### 6.1 List access

To access an element in a list the following syntax is used:

`(my-list:0)`

where 0 is the index.

For lists contained in a list:

`((my-list:0):0)`

### 6.2 Standard list functions

`[set my-list ()]`

* **push**: append an item to a list and return the list: `[push my-list 1 2 3 4 5]`
* **pop**: remove an item from a list and return the removed item: `[pop my-list 1]`
* **head**: return the first element of a list:

    `[head my-list]`

    `1`

* **tail**: return the rest of a list:

    `[tail my-list]`

    `(2 3 4 5)`

* **filter**: used with a lambda function to filter a list:

    `[set odd [lambda [x]: [= [% x 2] 1]]]`
    
    `[filter @odd my-list]`
    
    `(1 3 5)`
    
* **map**: apply a lambda function to a list:

    `[set cube [lambda [x]: [*** x 3]]]`

    `[map @cube my-list]`

    `(1 8 27 64 125)`

### 6.2 Other list functions

* **sort**: sort a list (in place).
* **reverse**: reverse list order (in place).
* **rndl**: return randomized list.
* **index**: return index of an element in a list

    `[index my-list 3]`

    `2`

* **set-single-value**: modify an item in a list:

    `[set-single-value my-list 4 6]`

    `6`

    `my-list`

    `(1 2 3 4 6)`

* **count**: count the number of occurrences of **x** in a list:

    `[set my-list2 (2 3 3 4 4 4 5 5 5 5)]`

    `[count 4 my-list2]`

    `3`

* **sum**: return the sum of the elements in a list:

    `[sum my-list]`

    `15`

### 6.3 Hashtable

```
[set my-hashtable (("A" 65) ("B" 66) ("a" 97) ("b" 98))]
```

Special functions are provided to access or modify values in a hashtable:

* **set-value**: append or modify a value:
    `[set-value my-hashtable "Z" 90]`

    `90`

    `my-hashtable`

    `( ("A" 65) ("B" 66) ("a" 97) ("b" 98) ("Z" 90) )`
    
* **get-value**: get value from a given key: `[get-value my-hashtable "A"]`
* **push-value**: when pairs are key/list, append an element to the list:

```
[set my-hashtable2 (("peter" ("AH" "10S" "3C")) ("jane" ("KD" "2H" "7C")))]
[push-value my-hashtable2 "peter" "9S"]
[push-value my-hashtable2 "jane" "4S"]

my-hashtable2

( ( "peter" ( "AH" "10S" "3C" "9S" ) ) ( "jane" ( "KD" "2H" "7C" "4S" ) ) )
```

## 7. Fractions

Any expression can be used for numerator and denominator

`1/2`

`-5/12`

```
[+ 1/2 3/4]

5/4
```

Example with variables:

```
[set f a/b]

f

a/b

[set a 3]
[set b 2]

f

a/b

[cal f]

3/2

[tonum f]

1.5
```

Example with an expression:
```
[set f 1/[** x]]
[for x 2 10 2: [echo [cal f] "\n"]]

1/4
1/16
1/36
1/64
1/100
```
