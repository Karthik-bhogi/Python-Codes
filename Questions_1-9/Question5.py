'''
Created on Apr 23, 2021

@author: Karthik
'''
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    if((num1+num2)>(num3) and (num2+num3)>(num1) and (num1+num3)>(num2)) :
        return success
    else :
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=(int)(input())
num2=(int)(input())
num3=(int)(input())
print(form_triangle(num1, num2, num3))