'''
Created on Apr 23, 2021

@author: Karthik
'''
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    n=101+no_of_passengers
    for ticket_number in range(101,n):
        if(len(source)>3):
            sou = source[0:3]
        else:
            sou = source[0:]
        if(len(destination)>3):
            des = destination[0:3]
        else:
            sou = source[0:]
        ticket_number=str(ticket_number)
        s = [airline+':'+sou+":"+des+":"+ticket_number]
        ticket_number_list=ticket_number_list+s
        #Use the below return statement wherever applicable
    if(no_of_passengers>=5):
        ticket_number_list = ticket_number_list[no_of_passengers-5:]
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))