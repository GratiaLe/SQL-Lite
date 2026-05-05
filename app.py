import sqlite3
# constants and variables
DATABASE = "fighters.db"

# functions
def print_all_aircraft():
    '''print all nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                             speed     max_g    climb   range   payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# main code
while True:
    user_input = input(
        """What would you like to do.\n
        1. Print all aircraft\n
        2. Print all aircraft sorted by speed\n
        3. Print all aircraft sorted by max g force\n
        4. Print all aircraft sorted by climb\n
        5. Print all aircraft sorted by range\n
        6. Print all aircraft sorted by payload\n
        7. Exit\n
        """
            )

    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    elif user_input == "6":
        pass
    elif user_input == "7":
        print("Goodbye.")
        break
    else:
            print("That was not an option\n")
