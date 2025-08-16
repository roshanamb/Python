
# region Function Syntax

def myFunction():
    #"""This function prints a message.  It does not take any parameters."""
    """Description of function
                 
        Arguments:   
        parameter1(int):Description of parameter1
                        
        Returns:      
        int value - 10   
   """
    print("This is my function.")
    return 10;

x=myFunction();  # Call the function
print("The function returned:", x);  # Print the return value of the function
print(myFunction.__doc__);  # Print the docstring of the function
print(help(myFunction));  # Print the help documentation for the function

# endregion

# region  Functin which accept a list and find out even numbers in it 
def findEvenNumbers(numbers):
    """This function takes a list of numbers and returns a list of even numbers.
    
    Arguments:
    numbers (list): A list of integers.
    
    Returns:
    list: A list containing only the even numbers from the input list.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers are:", even_numbers)
    
    # Accept a list of integers from user input
    user_input = input("Enter numbers separated by spaces: ")
    int_list = [int(x) for x in user_input.split()]
    print("You entered:", int_list)

    evenNo = [];
    for num in int_list:
        if num % 2 == 0:
            evenNo.append(num);
    return evenNo;

even_num = findEvenNumbers([2, 3, 42, 51, 62, 70, 5, 9])
print("Even numbers are:", even_num)

# endregion

# region Square of even numbers in a list
inputList = [4,7,11,13,18,20]
#creating a list with square values of only the even numbers
squareList = [var**2 for var in inputList if var%2==0] # 1st method

 # 2nd method
# for var in inputList:
#     if var % 2 == 0:
#         squareList.append(var**2)
print(squareList)

# endregion

# region Return multiple value from a function

def arithmetic(num1, num2):
    add = num1 + num2;
    sub = num1 - num2;
    mul = num1 * num2;
    div = num1 / num2;

    return add, sub, mul, div;

# read  four values in four variables
a,b,c,d = arithmetic(20,5);
print("Addition : ", a);
print("Substraction : ", b);
print("Multiplication : ", c);
print("Division : ", d);
#endregion



