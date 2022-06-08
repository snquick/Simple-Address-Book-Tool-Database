Assignment Prompt: 

In this lab, your task is to develop a simple address book tool. The tool maintains contact information of people. For each person, the tool maintains name and date of birth. Contact information consists of physical address and phone number. For physical addresses, the system must be able to maintain current and previous addresses. Current/active address information should have starting date and no end date, previous addresses must have a starting date and an ending date. A person cannot have multiple active physical address. For phone number, the system must maintain active phone numbers only, no previous phone numbers. For implementation, use MySQL database system. MySQL is open source and is available for Linux as well as Windows. For software application, use Python. The tool/application must support the following functionality:

1. Search current contact information by last name, the user enters last name, the system must locate active physical address and phone number and display the information back to the user.

2. Search current contact information by prefix, the user enters a name prefix, the system must locate and display all active contact information to the user, one per line.

3. Create new contact, there are two possible scenarios
- Contact name already exists – the system must create a new physical address and make it the active one, previously active physical address becomes part of historical ones (simply by adding ending date to it). As for phone number, the system should simply update/override the active phone number.
- Contact name does not exist – the system must create a new physical address and phone number records and associate them with the new name.

4. Search active contact information by age, the user inputs an age range, and the system must find all active contact information for people whose age falls in that range, one contact per line.
 
The following is a database design that should accommodate above requirements:
Table – people_master (person_id, person_name, person_DOB, active_phone_number).
Table – addresses (address_id, street_address, city, state, zip_code)
Table – people_address (person_id, address_id, start_date, end_date)
For the application, you can simply use a Python program that displays a menu with four possible commands as listed above, program sits in a loop, gets a command option, collect necessary input, performs needed SQL queries against the MySQL database, and displays result back to user. A QUIT option can added to above commands for user to exit.
