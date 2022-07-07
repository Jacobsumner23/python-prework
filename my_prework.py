# question 1
#Write a function to print"hello_USERNAME!"

from sys import get_coroutine_origin_tracking_depth


def hello_name(user_name):
    print("hello, " + user_name.upper() + "!" )

hello_name("gnarf")    
#not actually sure of how to put the function answer in " "
#question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    first = []
    odds = 1
    while odds <100:
        if odds % 2 != 0:
            first.append(odds)
        odds = odds+1
    print(first, odds)            
first_odds()    

#question 3
#Please write a Python function, max_num_in_list to return the maxnumber of a given list

def max_num_in_list(a_list):
    print(max(a_list))
a_list = [13, 97, 23, 65, 401, 3, 299]
max_num_in_list(a_list)

#question 4
#Write a function to return if the given year is a leap year

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            return False
        return True        

print(is_leap_year(2012))            

#question5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
num = [9,7,3,4,6,5,]
print(is_consecutive(num))