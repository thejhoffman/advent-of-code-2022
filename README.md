# advent-of-code-2022

I am using this readme as a journal of sorts as I complete the puzzles for [Advent of Code 2022](https://adventofcode.com/)

I found out about this challenge from another cohort mate in a coding boot camp I am currently attending.

I will graduate from the boot camp around the the same time that this event is over. It should be good practice for preparing for interviews.

I am going to do my best to log any notes/findings from attempting each day's puzzle.

### Day 1
Nothing too much to note. This was the first time actually loading data from a file using python. So it was nice to gain exposure on how to complete that task. Looking at other solutions, after solving my own, I want to try a slightly different method to read the input, or maybe event start using this library I found on reddit. [https://github.com/wimglenn/advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)

Other concepts I encountered while working on today's puzzle.
* The many different ways a list could be copied and the difference between a shallow and deep copy.
  * Resource: [Stack Overflow - How do i clone a list](https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment)
* The use of python's heap queue implementation to find nth larges elements:
  * Resource: [Stack Overflow - Get the second largest number](https://stackoverflow.com/questions/16225677/get-the-second-largest-number-in-a-list-in-linear-time)

### Day 2
Today's puzzle was significantly harder than yesterday's. It gave me the opportunity to try out python 3.10's `match` feature. My resulted still ended up looking like a giant if-else mess, but I was still able to get the result and solve the puzzle.

I believe my solution can be refactored heavily, but am unsure how to start doing so. I am going to look at other solutions online to try and find if there was an easier more elegant way to obtain the answer.
