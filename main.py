import mysql.connector as sql
from csvfile import Validated
import logging

try: 
    connection = sql.connect(host="localhost", user="root", password="") # Mysql connection
    cursorObject = connection.cursor() # Cursor object to execute sql statement
    
    try:
        cursorObject.execute("use DATA_ENTRY;") # use database
    except sql.errors.DatabaseError:
        logging.info(f"Record not inserted, Database Error!")

    for record in Validated:
        try:
            record[0] = record[0].replace(" ","")
            # Insert statement of validated value
            cursorObject.execute(f"Insert into Validated_Value values({int(record[0])},'{record[1]}');") 
            
            # Logged result
            logging.info(f"Record inserted({int(record[0])},'{record[1]}');")
    
        except sql.errors.DatabaseError:
            # In case of Database Error: Logged 
            logging.info(f"Record not inserted, Database Error!")

    connection.commit()
    connection.close()
    
except sql.errors.InterfaceError:
    print("InterfaceError: Error Related to Mysql Connection!")
except sql.errors.PoolError:
    print("Connection Pool Error!")
except sql.errors.DatabaseError:
    logging.info(f"Record not inserted, Database Error!")