# ISBN Validity Checker - Python

## Description
This is a program to check if a 10 digit ISBN or a 13 digit ISBN number is valid or not.

## Table of Contents
1. Installation
1. Usage
1. Credits

## Installation
The code can be copied into any code editor.
Comments are available in the code to explain what each section does.
A test suite is included and can be run to test the function.

To run this program, follow the following steps:
1. Clone the repository to your local machine.
1. Make sure you have docker installed, if not install it first then continue here.
1. Run the command `docker build -t [image_name] .`.
1. Once the image is built, run `docker run [image_name] [ISBN_number]` where you replace the `[ISBN_number]` with the number you want to check.

Included in the cloned repository is also a test tuite to ensure the function is accurate.
To run the test suite:
1. Follow the same steps for installation above.
1. Enter the command `python test_isbn.py`.
1. This will run the tests and provide its output in the terminal.
 
## Usage
In order to use this function you can simply use the name of the function with the ISBN number in question as an argument:
`isbn_validation("758-458-4576")`

This function can deal with ISBN numbers containing hyphens, spaces or an ''at the end.
## Credits
This project was created by Christopher Barnard (ChrisTheFish96)
