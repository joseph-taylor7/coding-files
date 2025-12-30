
import os
import sys

users = [{"Name": "Mutangana", "Number": "0780920096"},
         {"Name": "Mutabazi", "Number": "0786089262"},
         {"Name": "Mutangana", "Number": "0733033555"}]

name = input("Search By Name: ").strip()

for user in users:
    if user['Name'] == name:
        print(f"{user['Name']} {user['Number']}")
    
    

number = input("Enter A Number ").strip()

while True:

    for user in users:
        if user['Number'] == number:
            amount =float(input(f"Enter amount to send to {user['Name']}: "))
           
            
        