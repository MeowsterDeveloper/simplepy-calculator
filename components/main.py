# Script made by Félix Sánchez (hi@snap-camel)
# Github https://github.com/snapcamel
# Twitter @snapcamel
# Instagram @snapcamel

# Class colors for the terminal.
class color:
    header = '\033[95m'
    results = '\033[92m'
    text = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'

# Welcome message
print(" ") # Void
print(color.header + """
   ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗██████╗ ██╗   ██╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
   ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗╚██╗ ██╔╝     ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ███████╗██║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝ ╚████╔╝█████╗██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
   ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔═══╝   ╚██╔╝ ╚════╝██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗██║        ██║        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝        ╚═╝         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                                                            ██████╗ ██╗   ██╗     ██████╗███╗   ██╗ █████╗ ██████╗  ██████╗ █████╗ ███╗   ███╗███████╗██╗     
                                                            ██╔══██╗╚██╗ ██╔╝    ██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔════╝██║     
                                                            ██████╔╝ ╚████╔╝     ███████╗██╔██╗ ██║███████║██████╔╝██║     ███████║██╔████╔██║█████╗  ██║     
                                                            ██╔══██╗  ╚██╔╝      ╚════██║██║╚██╗██║██╔══██║██╔═══╝ ██║     ██╔══██║██║╚██╔╝██║██╔══╝  ██║     
                                                            ██████╔╝   ██║       ███████║██║ ╚████║██║  ██║██║     ╚██████╗██║  ██║██║ ╚═╝ ██║███████╗███████╗
                                                            ╚═════╝    ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
    """ + color.end)
print(" ") # Void
first_election = 0 # First election of numbers
while True:
    n1 = input(color.text + " Type the first number: " + color.end)
    try:
        n1 = float(n1)
    except:
        print(" ") # Void
        print(color.fail + "     Error that's not a valid argument, use only numbers" + color.end) # error message n1
        print(" ") # Void
    else:
        break
second_election = 0 # Second election of numbers
while True:
    print(" ") # Void
    n2 = input(color.text + " Type the second number: " + color.end)
    try:
        n2 = float(n2) # Validation
    except:
        print("  ") # Void
        print(color.fail + "     Error that's not a valid argument, use only numbers" + color.end) # Error message n2
    else:
        break
operation_election = 0 # Election of operation and options
while True:
    print(color.header + """
 Operations:

 ( + ) Addition.
 ( * ) Multiply.
 ( / ) Divide.

 Options:
 
 ( r ) Change numbers.
 ( e ) Exit.
""" + color.end)
    operation = input(color.text + " Type an option: " + color.end) # Operations input config, do not change.
    try:
        operation = str(operation)
    finally:
        if operation == '+': # Total config, you can add more if you want.
            print(" ") # Void
            print(color.results + "     The total is: ", n1 + n2) # Addition
        elif operation == '*':
            print(" ") # Void
            print(color.results + "     The total is: ", n1 * n2) # Multiplication
        elif operation == '/':
            print(" ") # Void
            print(color.results + "     The total is: ", n1 / n2) # Division
        elif operation == 'r': # Change number config
            while True:
                print(" ") # Void
                n1 = input(color.text + " Please type again your first number: " + color.end) # N1 input, do not change.
                try:
                    n1 = float(n1) # Validation config 
                except:
                    print(" ") # Void
                    print(color.fail + "     Error that's not a valid argument, please use only numbers" + color.end) # Error message of number 1
                    print(" ") # Void
                    continue
                else:
                    break 
            while True:
                print(" ") # Void
                n2 = input(color.text + " Please Type again your second number: " + color.end) # Change of the second number
                try:
                    n2 = float(n2) # Validation 
                except:
                    print(" ") # Void
                    print(color.text + "     Error that's not a valid argument, please use only numbers" + color.end) # Error message of number 2
                    print(" ") # Void
                    continue
                else:
                    break 
        elif operation == 'e': # Exit of script
            print(" ") # Void
            print(color.header + """ 
   ██████╗ ██╗   ██╗███████╗
   ██╔══██╗╚██╗ ██╔╝██╔════╝
   ██████╔╝ ╚████╔╝ █████╗  
   ██╔══██╗  ╚██╔╝  ██╔══╝  
   ██████╔╝   ██║   ███████╗
   ╚═════╝    ╚═╝   ╚══════╝
            """ + color.end) # Exit message
            print(" ") # Void
            exit() # Exit parameter 
        else:
            print(" ") # Void
            print(color.fail + "     Error that's not a valid argument, please type an operation or option" + color.end) # Error message from bad type of argument
