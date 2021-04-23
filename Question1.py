'''
Created on Apr 23, 2021

@author: Karthik
'''
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult_ticket_cost = 37550
    child_ticket_cost = (1/3)*adult_ticket_cost
    total_adult_ticket_cost = no_of_adults * adult_ticket_cost
    total_child_ticket_cost = no_of_children * child_ticket_cost
    service_tax= 0.07*(total_adult_ticket_cost+total_child_ticket_cost)
    total_ticket_cost = 0.9 * (total_adult_ticket_cost+total_child_ticket_cost + service_tax)
    return total_ticket_cost
#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)