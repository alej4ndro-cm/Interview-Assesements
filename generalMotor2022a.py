'''Programming challenge description:
Write a program that, given two clock times, prints out the absolute number of minutes between them.

Input:
Your program should read lines from standard input. Each line contains two wall clock times separated by a hyphen. Wall clock time is defined as hh:mm followed by AM' or 'PM', e.g. '09:05 AM'

Output:
Print to standard output the number of minutes between the two times from standard input. Print out each result on a new line.

Test 1
Test Input
10:00 AM - 11:00 AM

Expected Output
60

Test 2
Test Input
1:00 PM - 11:00 AM
Expected Output
1320'''
import sys

times = input()
t1, t2 = times.split('-')
hr_min, merdian1 = t1.split()
time_hr1, time_min1 = hr_min.split(':')
hr_min, merdian2 = t2.split()
time_hr2, time_min2 = hr_min.split(':')


minutes1, minutes2 = 0, 0
if merdian1 == 'AM':
    minutes1 = 12 * 60 + int(time_hr1) * 60 + int(time_min1)
else:
    minutes1 = int(time_hr1) * 60 + int(time_min1)
if merdian2 == 'AM':
    minutes2 = 12 * 60 + int(time_hr2) * 60 + int(time_min2)
else:
    minutes2 = int(time_hr2) * 60 + int(time_min2)

diff = minutes1-minutes2 if minutes1>minutes2 else minutes2-minutes1
print(diff)