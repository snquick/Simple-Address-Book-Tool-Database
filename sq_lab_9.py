import mysql.connector
from mysql.connector import errorcode

SELECT_AGE = '''SELECT 
                     *
                FROM 
                    people_master, addresses, people_address
                WHERE
                    person_dob = %(date_Birth)s'''

SELECT_PREFIX = '''SELECT 
                     *
                FROM 
                    people_master, addresses, people_address
                WHERE
                    person_first_name = %(f_name)s'''

SELECT_QUERY = '''SELECT 
                     pm.person_first_name, a.street_address, pm.active_phone_number
                FROM 
                    people_master pm, addresses a inner join people_address pa on pa.person_id = pa.person_id
                WHERE
                    person_last_name = %(l_name)s'''

def select_contact_age(dateBirth):
    try:
        mysql_connection = mysql.connector.connect(
            user="root",
            password='root',
            host='127.0.0.1',
            database='simple_address_book'
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print("Cannot connect to database:", err)

    else:
        cur = mysql_connection.cursor()
        cur.execute(SELECT_PREFIX, {'date_Birth': dateBirth})

        rows = cur.fetchmany(1)

        for row in rows:
            print('Everything on: {} {} {} {} {} {} {} {} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4],
                                                                              row[5],
                                                                              row[6], row[7], row[8], row[9], row[10],
                                                                              row[11]))
        print("Success")
        cur.close()
        mysql_connection.close()

def select_contact_prefix(first_name: str):
    try:
        mysql_connection = mysql.connector.connect(
            user="root",
            password='root',
            host='127.0.0.1',
            database='simple_address_book'
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print("Cannot connect to database:", err)

    else:
        cur = mysql_connection.cursor()
        cur.execute(SELECT_PREFIX, {'f_name': first_name})

        rows = cur.fetchmany(1)

        for row in rows:
            print('Everything on: {} {} {} {} {} {} {} {} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4], row[5],
                                           row[6], row[7], row[8], row[9], row[10], row[11]))

        print("Success")
        cur.close()
        mysql_connection.close()


def select_contact_current(last_name: str):
    try:
        mysql_connection = mysql.connector.connect(
            user="root",
            password='root',
            host='127.0.0.1',
            database='simple_address_book'
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print("Cannot connect to database:", err)

    else:
        cur = mysql_connection.cursor()
        cur.execute(SELECT_QUERY, {'l_name': last_name})

        rows = cur.fetchmany(1)

        for row in rows:
            print('person_first_name: {}, street_address: {}, '
                  ' active_phone_number: {}'.format(row[0], row[1], row[2]))

        print("Success")
        cur.close()
        mysql_connection.close()


if __name__ == '__main__':

    print(
        "Main menu:\n1- Search by last name\n2- Search by prefix\n3- Create new Contact\n4- Search by age range\n5- Exit\n\tenter command: ",
        end='')
    command = int(input(""))

    while command != 5:
        if command == 1:
            last_name = input("enter last name: ")
            info1 = select_contact_current(last_name)
            print(info1)
        elif command == 2:
            prefix = input("enter prefix: ")
            info2 = select_contact_prefix(prefix)
            print(info2)
        elif command == 3:
            print("")
            fnC = input("First name: ")
            lnC = input("Last Name: ")
            dob = input("Date of Birth (xxxx-yy-zz): ")
            pn = input("Active Phone Number (xxx-xxx-xxxx): ")
            a = input("Street Address: ")
            c = input("City: ")
            s = input("State: ")
            z = input("Zip Code: ")
        elif command == 4:
            age = input("Select age range (xxxx-xx-xx): ")
            info3 = select_contact_age(age)
            print(info3)


        print(
            "Main menu:\n1- Search by last name\n2- Search by prefix\n3- Create new Contact\n4- Search by age range\n5- Exit\n\tenter command: ",
            end='')
        command = int(input())

