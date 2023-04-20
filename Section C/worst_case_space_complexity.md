# Worst-case Space Complexity of isbn_validation Function

## Description of function
This function takes in one argument, which is a `user_isbn` which represents an ISBN number as a string. The output is either `Valid` or `Invalid` depending on several manipulations with the original input string'.

## Breakdown
1. The first section creates a list called `isbn_list` by replacing any hyphens or spaces with empty strings. This has a space complexity of O(n) with n being the length of the string.
1. The function then initializes two lists that can be used later depending on the length of the original input. These lists both have a constant length and is thus O(1).
1. The function then determines if the last digit of the user input is an `x` and replaces this value with a `10` as per ISBN rules. The space complexity of this is also O(1).
1. Then the function iterates through the list and determines if each character is a digit, if it is the type is converted to an integer, if it is not the function returns `Invalid`. This has a space complexity of O(n) with n being the length if the list.
1. An empty list is then initiated to store the values after multiplication with the constant list created in number 2. The size of this list depends on the length of the user input ISBN, `user_isbn`, which at most can be 13. The space complexity of this operation is thus O(1).
1. The function then determines if the length of the user ISBN is either `10` or `13` and if it is neither it returns `Invalid`. This has an operational complexity of O(1).
1. The list is then multiplied with its corresponding constant multiplication list and is stored in a new list called `results_mul`. This has an operational complexity of O(n) with n being the length of the user input ISBN.
1. Lastly, the contents of the `results_mul` list is summed together and the total is checked to determine if it meets a certain condition. This has a space complexity of O(1).

## Summary
In summary, the function isbn_validation has a worst-case space complexity of O(n) where n represents the length of the `user_isbn` string.

