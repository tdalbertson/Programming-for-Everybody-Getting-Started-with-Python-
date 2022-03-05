"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    try:
    	if num == "done":
        	break
       	
        # Setting num to int for if statements
        num = int(num)
        
        # Setting largest and smallest to a value other than None
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
            
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        
    except ValueError:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)


"""
Output:
Invalid input
Maximum is 10
Minimum is 2
"""
