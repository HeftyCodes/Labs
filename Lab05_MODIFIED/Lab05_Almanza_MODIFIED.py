# Name: Kenny Almanza
# Date: 03-08023 
# File: Lab05_Almanza.py

# _   _       __ _         
#| | | | ___ / _| |_ _   _ 
#| |_| |/ _ \ |_| __| | | |
#|  _  |  __/  _| |_| |_| |
#|_| |_|\___|_|  \__|\__, |
#                    |___/ 

# Purpose: Basic I/O functionality + writing files
import sys, os

# the easiest way to debug is to uncomment the args line with the list of values and comment out the sys.argv line
# when running through the command line, you need to uncomment the sys.argv line and comment/delete the list line
#Kenny: Shows the user the companies in FAANG to choose from then it checks to see if user input is acceptable.
print("Companies:fb,amzn,goog,nflx")
company_input = input("Enter Company of Interest: ")
companies = ("fb" "goog" "nflx" "aapl")
switch = True           #Kenny: I use this later in my code to allow me to prevent unnecessary files from being created.

if company_input in companies:
    print("")
else:
    print(company_input + " does not exist in file")
    print("Please choose a different company")
    switch = False


args = sys.argv
args = [".py", "faang.txt", "w", company_input, "open"]


# the first argument is the Python file, which we don't care about in the script
filename = args[1]
option = args[2]        # support "r" for reading, 'w' for writing
company = args[3]       # options: 'aapl', 'amzn', 'fb', 'goog', 'nflx'
label = args[4]


# if writing a file, label is the selected column
if len(args) == 5:
    label = args[4]     # options: 'high', 'open', 'low', 'close', or 'volume'


# check that the number of arguments is appropriate
if len(args) <4 or len(args) > 5:
    print("Incorrect number of arguments provided!")
    sys.exit()


# open the file
# process file by removing newlines and splitting tab-delimited file
# we don't have to use file.close() b/c using the `with open() as file` construct
#   lines: list of lists
with open(filename, 'r') as file:
    lines = [line.strip().split("\t") for line in file.readlines()]


# grab the first line of information (.txt file header)
# and remove it from the collection
header = lines[0]
lines.remove(header)


# validation of user input
if label not in header:
    print(f"The option {label} does not exist in this dataset!")
    sys.exit()


# the `header` variable is a list
# find what position in the list we can expect to find the `ticker` value (i.e. 'aapl', 'amzn', etc.)
ticker_pos = header.index("ticker")


# if we are reading the information then print to the terminal
if option.lower() == 'r' and len(args) == 4:
    # prepare the header to be printed
    print("\t".join(header).expandtabs(20))

    # and go through every line in the file
    for line in lines:
        # printing out the information if the line matches the company of interest
        if line[ticker_pos] == company:
            print("\t".join(line).expandtabs(20))


# if we are writing the information...
elif option.lower() == 'w' and len(args) == 5:
    
    # create a `cwd` variable that uses the getcwd() function
    cwd = os.getcwd()

    # pull together the company and column label to save as a file
    # this will result in a file such as 'amzn_volume.txt'
    file_name = "_".join([company, label]) + ".txt"
    xls_file_name = "_".join([company, label]) + ".xls"

    # create an if statement that makes sure the file does not exist
    # if it does exist print out a message and use sys.exit() to terminate the program
    if (os.path.exists(file_name)):
        print("File already exists!")
        sys.exit()

    if (os.path.exists(xls_file_name)):
        print("This Excel File Already Exists")
        #sys.exit

    # create a `label_pos` variable to finds the index of the label in the `header`` list
    # hint: modify what you see on line 45
        label_pos = header.index(label)

    # at this point we can assume that the file does not already exist, so we can create it
    # giving ourselves the ability to write to the file
    
if switch == True:          #Kenny: This switch will allow me to open and write to a file so long as company_input is in companies 
    with open(file_name, "w+") as file:
        file.write("date" "\t" "\t" "high" "\t" "\t" "low" "\t" "\t" "open" "\t" "\t" "close" "\t" "  volume" "\t" "ticker" "\n")
        #Kenny: This write command allows the .txt file to be more readable

        # create a for loop that looks at each line in lines
        for line in lines:
            if company_input in line:
                print(line)          #Kenny: Prints the data that will be written to the file
            string_data = (str(line))                   
            newline_data = str(string_data + "\n")
            file.write(newline_data)
                       
                # inside the for loop, check if the given line matches the company of interest
                 # if it matches, use file.write() to print out the information with a newline \n at the end
if switch == True:
    with open(xls_file_name, "w") as xls:
        string_data = (str(line))                   
        newline_data = str(string_data + "\n")
        xls.write(newline_data)
        
                 
    pass

else:
    print("Option Not Supported!")
    