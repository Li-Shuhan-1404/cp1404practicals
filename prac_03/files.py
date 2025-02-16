"""
Write code that asks the user for their name,
then opens a file called and writes that name to it.
Use and for this question.
"""


def question_1():
    file = open("name.txt", "w")
    name = input("Name: ")
    print(name, file=file)
    file.close()


"""
In the same file, but as if it were a separate program, 
write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
(or whatever the name is in the file). Do not simply print the user's input variable!
Use and for this question.
"""


def question_2():
    file = open("name.txt", "r")
    name = file.read().strip()
    print(f"Hi {name}!")
    file.close()


"""
Create a text file called and save it in your prac directory. 
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens , reads only the first two numbers, 
adds them together then prints the result, which should be... 59. 
Use instead of and for this question.
"""


def question_3():
    total = 0
    with open("numbers.txt", "r") as file:
        for i in range(0, 2):
            number = file.readline()
            total += int(number)
        print(total)
    file.close()


"""
Now write a fourth block of code that prints the total for all lines in . 
This should work for a file with any number of numbers. 
Use instead of and for this question.
"""


def question_4():
    total = 0
    with open("number.txt", "r") as file:
        lines = file.readlines()
        for number in lines:
            total += int(number)
    print(total)
    file.close()


question_1()
question_2()
question_3()
question_4()
