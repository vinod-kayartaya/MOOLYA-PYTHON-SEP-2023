"""
A menu-driven app for doing CRUD operations on a SQLite database table
"""
import sqlite3

db_config = 'customers_db.sqlite'


def menu():
    print('''
*** Main Menu ***
0 -> Exit
1 -> List all customers
2 -> Add a new customer
3 -> Delete an existing customer
4 -> Update customer data
5 -> Search customer
6 -> Create `customers` table''')

    choice = input('Enter your choice: ')
    try:
        choice = int(choice)
    except ValueError:
        choice = -1

    return choice


def create_table():
    try:
        with open('customers_table.sql') as file:
            sql_cmd = file.read()

            with sqlite3.connect(db_config) as conn:
                cur = conn.cursor()
                cur.execute(sql_cmd)
                print('Table created successfully!')

    except sqlite3.DatabaseError as err:
        print(f'Got an error - {err}')


def add_customer():
    print('Enter new customer details: ')
    name = input('Name   : ')
    gender = input('Gender : ')
    email = input('Email  : ')
    phone = input('Phone  :  ')
    city = input('City   : ')

    sql_cmd = 'insert into customers (name, gender, email, phone, city) values (?, ?, ?, ?, ?)'
    try:
        with sqlite3.connect(db_config) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, (name, gender, email, phone, city))
            print('New customer record added successfully')
    except sqlite3.DatabaseError as err:
        print(f'Something went wrong - {err}')


def __accept(message, default_value):
    data = input(f'{message}({default_value}) ')
    return default_value if data == '' else data


def update_customer_data():
    try:
        customer_id = int(input('Enter customer id to edit: '))
        sql_cmd = 'select * from customers where id = ?'
        with sqlite3.connect(db_config) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, (customer_id,))
            c = cur.fetchone()
            if c is None:
                print(f'No customer data found for id {customer_id}')
                return

            print('Enter new data for customer record: ')
            name = __accept('Name   : ', c[1])
            gender = __accept('Gender : ', c[2])
            email = __accept('Email  : ', c[3])
            phone = __accept('Phone  : ', c[4])
            city = __accept('City   : ', c[5])
            sql_cmd = 'update customers set name=?, gender=?, email=?, phone=?, city=? where id=?'
            cur.execute(sql_cmd, (name, gender, email, phone, city, customer_id))
            print('Customer data updated successfully!')

    except ValueError:
        print('id must be an integer')


def delete_customer_data():
    try:
        customer_id = int(input('Enter customer id to delete: '))
        sql_cmd = 'select * from customers where id = ?'
        with sqlite3.connect(db_config) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, (customer_id,))
            c = cur.fetchone()
            if c is None:
                print(f'No customer data found for id {customer_id}')
                return

            print(f'Customer data for id {customer_id}:')
            print('''
Id     : %d
Name   : %s
Gender : %s
Email  : %s
Phone  : %s
City   : %s
''' % c)
            ans = input('Are you sure you want to delete this? yes/no (no) ')
            if ans.lower() == 'yes':
                sql_cmd = 'delete from customers where id = ?'
                cur.execute(sql_cmd, (customer_id, ))
                print('Customer data deleted successfully')
            else:
                print('Customer data is not deleted!')
    except ValueError:
        print('id must be an integer')


def search_customers():
    text = input('Enter search text: ')
    text = text.strip()

    if text == '':
        print('Nothing to search')
        return

    sql_cmd = 'select * from customers where name like ? or email like ? or city like ?'
    with sqlite3.connect(db_config) as conn:
        cur = conn.cursor()
        param = f'%{text}%'
        cur.execute(sql_cmd, (param, param, param))
        customers = cur.fetchall()

        if len(customers) == 0:
            print(f'No customer data found for the search text "{text}"')
            return

        if len(customers) == 1:
            c = customers[0]
            print('''One customer found
            
Id     : %d
Name   : %s
Gender : %s
Email  : %s
Phone  : %s
City   : %s
            ''' % c)
            return

        print('%-5s %-20s %-10s %-50s %-15s %-20s' % ('Id', 'Name', 'Gender', 'Email addr', 'Phone#', 'City'))
        print('=' * 125)
        for customer in customers:
            print('%-5s %-20s %-10s %-50s %-15s %-20s' % customer)
        print('-' * 125)


def list_all_customers():
    sql_cmd = 'select * from customers'
    try:
        with sqlite3.connect(db_config) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd)
            customers = cur.fetchall()

            if len(customers) == 0:
                print('No customers in your database. Try adding few.')
                return

            print('%-5s %-20s %-10s %-50s %-15s %-20s' % ('Id', 'Name', 'Gender', 'Email addr', 'Phone#', 'City'))
            print('=' * 125)
            for customer in customers:
                print('%-5s %-20s %-10s %-50s %-15s %-20s' % customer)
            print('-' * 125)

    except sqlite3.DatabaseError as err:
        print(f'Something went wrong - {err}')


def main():
    while True:
        choice = menu()
        if choice == 0:
            print('Thank you. Have a nice day!')
            break
        elif choice == 1:
            list_all_customers()
        elif choice == 2:
            add_customer()
        elif choice == 3:
            delete_customer_data()
        elif choice == 4:
            update_customer_data()
        elif choice == 5:
            search_customers()
        elif choice == 6:
            create_table()
        else:
            print('Invalid choice. Please retry.')


if __name__ == '__main__':
    main()
