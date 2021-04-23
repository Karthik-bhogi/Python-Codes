# Python-Codes 

1. The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: <br>
   Rate per Adult: Rs. 37550.0 <br>
   Rate per Child: 1/3rd of the rate per adult <br>
   Service Tax: 7% of the ticket amount (including all passengers) <br>
   As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax). <br>
   Find and display the total ticket cost for a group which had adults and children. <br>

2. Write a python program that displays a message as follows for a given number: <br>
   1. If it is a multiple of three, display "Zip" <br>
   2. If it is a multiple of five, display "Zap". <br>
   3. If it is a multiple of both three and five, display "Zoom". <br>
   4. If it does not satisfy any of the above given conditions, display "Invalid". <br>
 
3. Write a Python program to find the sum of digits of a given number. <br>
   E.g. Sum of number 123 will be 6 <br>

4. Write a python program to find and display the product of three positive integer values based on the rule mentioned below: <br>
   It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left       also should not be included. <br>
   If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1. <br>
   
5. Write a python function to check whether three given numbers can form the sides of a triangle. <br>

6. You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using      minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1. <br>

7. FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order. <br>

   A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-        vegetarian combo than the vegetarian combo. <br>

   Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery          charges are as mentioned below: <br>
   
   ![q7](https://user-images.githubusercontent.com/64722906/115866626-8ecf6a80-a457-11eb-9b00-f67be8412279.png)

   Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount    to be paid by a customer.  <br>
   The below information must be used to check the validity of the data provided by the customer: <br>
   1. Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian. <br>
   2. Distance in kms must be greater than 0. <br>
   3. Quantity ordered should be minimum 1. <br>
   4. If any of the input is invalid, the bill amount should be considered as -1. <br>
     
8. The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. Write a python program to implement the following        requirements: <br>

   Initialize the following variables with appropriate input values:account_number, account_balance, salary, loan_type, loan_amount_expected and customer_emi_expected. <br>
   The account number should be of 4 digits and its first digit should be 1. <br>
   The customer should have a minimum balance of Rupees 1 Lakh in the account. <br>
   If the above rules are valid, determine the eligible loan amount and the EMI that the bank can provide to its customers based on their salary and the loan type they expect to    avail. <br>
   The bank would provide the loan, only if the loan amount and the number of EMI’s requested by the customer is less than or equal to the loan amount and the number of EMI’s      decided by the bank respectively. <br>
   Display appropriate error messages for all invalid data. If all the business rules are satisfied ,then display account number, eligible and requested loan amount and EMI’s.
   Test your code by providing different values for the input variables. <br>
   
   ![q8](https://user-images.githubusercontent.com/64722906/115866586-8119e500-a457-11eb-9ac5-fcc74c1fe72a.png)
  
9. Write a python program to solve a classic ancient Chinese puzzle.<br>
   We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? <br>

10. Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.<br>
    1. Always num1 should be less than num2<br>
    2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied<br>
       a. Sum of the digits of the number is a multiple of 3<br>
       b. Number has only two digits<br>
       c. Number is a multiple of 5<br>
    3. Display the maximum element from the list<br>
    In case of any invalid data or if the list is empty, display -1.<br>
    
11. Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences <br>

12. Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:<br>
    The ticket number should be generated as airline:src:dest:number where<br>
    1. Consider AI as the value for airline <br>
    2. src and dest should be the first three characters of the source and destination cities.<br>
    3. number should be auto-generated starting from 101<br>
    The program should return the list of ticket numbers of last five passengers.<br>
    **Note**: If passenger count is less than 5, return the list of all generated ticket numbers.<br>
    
13. Write a python program which displays the count of the names that matches a given pattern from a list of names provided.  <br>
    Consider the pattern characters to be: <br>
    1. "_ at" where "_" can be one occurrence of any character
    2. "%at%" where "%" can have zero or any number of occurrences of a character

14. Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list. <br>

15. ARS Gems Store sells different varieties of gems to its customers.<br>
   Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. Any purchase with a total bill amount above        Rs.30000 is entitled for 5% discount. If any gem required by the customer is not available in the store, then consider total bill amount to be -1.<br>
   Assume that quantity required by the customer for any gem will always be greater than 0.<br>
   Perform case-sensitive comparison wherever applicable.<br>
   
16. Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.<br> 
    **Note**: Assume that all the numbers are two digit numbers.<br> 
    
17. Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return       false.<br>
    **Note**: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW     etc.<br>
    
18. Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that     run.<br>
    Write a python function which performs the run length encoding for a given String and returns the run length encoded String. Provide different String values and test your       program <br>
    
19. A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the teacher rewards them with chocolates.<br>
    Write a Python function to<br>
    1. Find the total number of chocolates received by all the children put together. Assume that each child is identified by an id and it is stored in a tuple and the number of     chocolates given to each child is stored in a list.
    2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp. <br>
    3. If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.<br>
    4. If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the extra chocolates provided for the child must be added to         his/her existing number of chocolates and display the list containing the total number of chocolates received by each child.<br>
