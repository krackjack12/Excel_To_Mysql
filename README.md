EXCEL_TO_MYSQL
This project covers the validation and subsequent addition of {Phone Number,Email ID} from an Excel file in csv format to the mysql database. The code takes only one input: A Csv File. The Csv file contains Phone numbers and Email ID data with or without other information. The Code goes through the csv file and fetches data to be validated using RegEx and then added to the Mysql Database. Also a log file is added to track the INSERT operations in Database.

Pre-requisites
Python, Mysql and File Handling Basics.

Setup for Project
Mysql Database called DATA_ENTRY is already created and has the table Validated_Value. In the table, the Email ID field is the PRIMARY Key and Phone number is non Unique (as one phone number can be linked to multiple email IDs). Download the libraries required using pip3.

For Feedback and Suggestions
Please contact me on krishjoshi1202@gmail.com .