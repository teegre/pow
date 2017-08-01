[PowerText] version 0.0.1 (07-2017)

[PowerText] is a LISP-like functionnal programming language written in Python 3.6. My first intention was to write a scripting language to create simple text 
animations in a terminal. Basically the language needed to have functions to move the cursor on the screen and to print some text. Even though the focus is on lists, strings, and functions, [PowerText] has the basic features of any programming language and can be used for other purposes (I guess...). It also can be extended if needed.

# 1. SYNTAX

Similar to LISP, but parentheses have been replaced by square brackets. So for adding 2 and 2, just type: [+ 2 2]  which should return 4.

## 1.1 Types

There are five different types in [PowerText]:

- string: "Abc" or 'Abc'
- number: 123, 123.456 (integer or float)
- list: (1 2 3)
- boolean: true, false
- null

## 1.2 Variable assignment

Function «set».

  [set b "Hello, World!"]

Note that every function returns a value so it is possible to nest functions inside functions.
For example, let's say you also need a variable "a" equal to "b", you would write:

  [set a [set b "Hello, World!"]]

The string "Hello, World" is first assigned to variable "b" and then, the result of the «set» function is assigned to variable "a".
To assign a list to a variable:

  [set l (0 1 2 3 4 5 6 7 8 9)]
  [set l ()] (to assign an empty list)

For more information about lists, see chapter LISTCHAPTER.

## 1.3 ?, for and while.

In [PowerText], "?" is equivalent to if, and its syntax is as follow:

  [? [condition]: [dothis]; [dothat]]

Note that [dothis] can be one or more statements:

  [? [condition]:
  [dothis]
  [andthis]
  [andalsothis]]

For loop:

  [for [variable start end]: [dothis]]
  [for [variable start end step]: [dothis]]

While loop:

  [while [condition]: [dothis]]

## 1.4
