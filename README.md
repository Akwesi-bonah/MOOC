# INTRODUCTION TO PROGRAMMING, SPRING 2023, ONLINE EXAM 2

MOOC.fi is an online platform that provides a comprehensive and free-of-charge introduction to computer science and programming, especially designed for beginners. The platform offers a set of courses that cover various topics in computer science, from the basics of programming and algorithms to more advanced topics such as machine learning and data structures. MOOC.fi is primarily used by students and teachers in Finland, but the courses are available to anyone around the world who wants to learn programming or improve their programming skills. The courses are self-paced and contain a combination of video lectures, exercises, and programming assignments. The platform is known for its hands-on approach, where students can apply the concepts they learn through programming exercises and real-world projects.
You can visit here [mooc webpage](https://www.mooc.fi/en/)
## Exercise 1
Write a program, which asks user to type in strings one by one. When the user inputs an empty string, program outputs number of strings typed in, the length of the longest string and the most common character.

Sample execution of the program, where thickened words are inputs from the user:

![](C:\Users\arhin\Downloads\ex1.png)

The most common character in the sample execution of the program is a, because it occurs four times in strings given as input. You can make an assumption, that there is only one suitable candidate for the most common character, and that user inputs at least one string

## Exercise 2

In this exercise, two functions are written to the exercise template. The functions are defined as follows:

a) def separate(string: str)

Returns a list of tuples based on the string given as a parameter. Tuples in list consist of two elements. Strings are in format "string1a;string1b,string2a;string2b,string3a; ...". Tuples are separated from the string by a comma and the elements of the tuple by a semicolon, so that the string to the left of the semicolon is the left element of the tuple.

Use the example below to test the function.
![](C:\Users\arhin\Downloads\ex2.png)

b) def to_dictionary(my_list: list)

Returns a dictionary based on the list given as parameter. The given list contains tuples consisting of two elements, such as the return value of the function in section a. The dictionary is constructed so that the tuples in the list correspond to key-value pairs, where the left element of the tuple is the key and the right element of the tuple is value.

Use the example below to test the function.
![](C:\Users\arhin\Downloads\ex2b.png)

## Exercise 3
Write a function points(stats), which takes a string as its argument.

The string given as an argument is an ice hockey team statistics in the format: [team]:[wins]-[losses]-[ties]

For example, the string: "Kumpula Intelligence:0-8-1" describes a team called Kumpula Intelligence with 0 wins, 8 losses and 1 tie.

The function points(stats) returns points gained by the team as an integer. The points are counted as follows: win brings three points, tie brings one point and no points are awarded for the loss.

The function should raise ValueError exception, if wins, losses or ties are not readable integers. For example executing the function with the string: "KBC:6-xx-1", would raise ValueError exception with the text "All stats were not Integers".

You can make an assumption that the given string contains an appropriate amount of colons and dashes, and that the integers are positive.

Strings that you can use to test your function:

- "Heba hawks:5-6-1"
- "Brewsters:3-12-10"
- "Sleepers:0-0-0"
- "KBC:AAA-1-ll"
- "Navy jerries:7-xx-1"
- "Loosisters:8-5-abb"


# About
The University of Helsinki MOOC Center makes high-quality online education possible by developing and researching educational software and online learning materials. Teachers both within and without the University of Helsinki rely on our tools to create impactful teaching materials. Our popular Massive Open Online Courses (MOOCs) have been available through MOOC.fi since 2012.



