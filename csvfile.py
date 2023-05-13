import csv
import regex
import logging

# Logging format : {TimeStamp} {Levelname:INFO} {Message}
logging.basicConfig(filename="data.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

# Function to provide Validation Functionality
def isValidated(List,Validated,a,b):
    phone =[]
    emailId = []
    EmID = r"[^@]+@[^@]+\.[^@]+" # Regex for Email ID
    Phone = r"(\+\d{2,3})?([ -])?([9876]{1})(\d{2})([ -]?)(\d{3})([ -]?)(\d{4})" # Regex for Phone Number
    
    for i in List:
        phone.append(List[a]) #Access the Phone Numbers
        emailId.append(List[b]) #Access the Email ID
        
    for i in range(0,len(List)):
        if regex.match(Phone,phone[i]): # Match the regex with Phone exp
            if (("+" in str(phone[i])) and len(phone[i]) > 10) or (len(phone[i]) == 10): 
                if regex.match(EmID,emailId[i]): # Match the regex with EmID exp
                    record = [phone[i],emailId[i]]
                    Validated.append(record)
                    break

# File Name Input
file_name = input("Enter file name: ")

try:
    with open(file_name,"r") as csv_file: # File Input 
        csv_reader = csv.reader(csv_file)

        Validated = [] # This will contain the validated records{phone_number,email}
        global a,b # {a,b} has the column number, that can be then accessed for Validation
        a=0
        b=0
        
        # Loop to set the Column Number
        for i in csv_reader: 
            a = i.index("Phone Number")
            b = i.index("Email ID")
            break
        
        for i in csv_reader:
            isValidated(i,Validated,a,b) # Calling Function for Validation
        
        '''for x in Validated:
            print(x)'''
        
except FileNotFoundError:
    print("File not found.")