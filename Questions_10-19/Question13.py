'''
Created on Apr 23, 2021

@author: Karthik
'''
def count_names(name_list):
    #start writing your code here
    #Populate the variables: count1 and count2
    count1=0
    count2=0
    new=''
    for name in name_list:
        new = new + name + " "
        if(name.endswith("at")):
            count1 = count1 + 1
        if(name.startswith('at') and name.endswith('at')):
            count1 -= 1
    print("_at -> ",count1)
    count2 = new.count("at")
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("%at% -> ",count2)

#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)