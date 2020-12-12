--- Day 6: Custom Customs ---

The form asks a series of 26 yes-or-no questions marked a through z.
There is a input.file with the questions answered "yes". Each line is a person's answer, groups are separated
by blank lines.

Part 1:

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Part 2:

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

example:
abc

a
b
c

ab
ac

total_anyone = 3 + 3 + 3 = 9
total_everyone = 3 + 0 + 1 = 4