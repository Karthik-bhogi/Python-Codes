'''
Created on Apr 23, 2021

@author: Karthik
'''
def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    l =len(str(number))
    while (l>=1) :
        n=number%10
        sum_of_digits = sum_of_digits + n
        number=number//10
        l=l-1
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(157)
print("Sum of digits:",sum_of_digits)