# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
# This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

def final_grade(exam, projects):
    if exam <= 100 and projects >= 10:
        return (100)
    elif exam >= 75 and projects == 5:
        return(90)
    elif exam >= 50 and projects == 2:
        return(75)
    else:
        return(0)

# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
def update_light(current):
    if current == 'red':
        return 'green'
    elif current == 'yellow':
        return 'red'
    elif current == 'green':
        return 'yellow'
# Let's play! You have to return which player won! In case of a draw return Draw!.
def rps(p1, p2):
    hand = {'scissors' : 'paper', 'rock' : 'scissors', 'paper': 'rock'}
    if hand[p1] == p2:
        return 'Player 1 won!'
    elif hand[p2] == p1:
        return 'Player 2 won!'
    else:
        return 'Draw!'
# A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them.
def main (verb, noun):
    return verb + noun
# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).
def count_by(x, n):
     return [ i * x for i in range(1, n+1)]

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

def between(a,b):
    gtlt = list(range (a,b + 1))
    return gtlt