# Program to check both ISBN10 and ISBN13 numbers to determine if they are valid.

# Function is defined to allow for user ISBN input.
def isbn_validation(user_isbn):
    # Returns "Invalid" if user input nothing.
    if not user_isbn:
        return "Invalid"

    # User input is converted to a list along with constant lists for validation.
    isbn_list = list(user_isbn.replace(" ", "").replace("-",""))
    isbn10_multiply = [10,9,8,7,6,5,4,3,2,1]
    isbn13_multiply = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    
    # Possible "x" after input is replaced with a "10" and characters are converted to ints.
    if isbn_list[-1].lower() == "x":
        isbn_list[-1] = "10"
    else:
        for i in range (len(isbn_list)):
            if not isbn_list[i].isdigit():
                return "Invalid"
            isbn_list[i] = int(isbn_list[i])

    for i in range (len(isbn_list)):
        isbn_list[i] = int(isbn_list[i])
    
    # Length of list is calculated and used in if statements.
    isbn_length = len(isbn_list)
    result_mul = []

    # Validation for ISBN10 numbers.
    if isbn_length == 10:
        for x, y in zip(isbn_list, isbn10_multiply):
            result_mul.append(x*y)
        total = sum(result_mul)
        if total%11 == 0:
            return "Valid"
        else:
            return "Invalid"

    # Validation for ISBN13 numbers.
    elif isbn_length == 13:
        for x, y in zip(isbn_list, isbn13_multiply):
            result_mul.append(x*y)
        total = sum(result_mul)
        if total%10 == 0:
            return "Valid"
        else:
            return "Invalid"
            
    # Section to run if the numbers are anything but 10 or 13 characters long.
    else:
        return "Invalid"
