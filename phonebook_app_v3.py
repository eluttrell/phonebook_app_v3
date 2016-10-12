import pg
db = pg.DB(dbname='phonebook_db')


def lookup_entry():
    keep_running = True
    while keep_running == True:
        name = raw_input("Name? ").capitalize()
        result_list = db.query(
            "select * from phonebook where name ilike '%s'" % name).namedresult()
        if len(result_list) > 0:
            print "\n%s:\n\nPhone: %s\nEmail: %s\n" % (result_list[0].name, result_list[0].phone_number, result_list[0].email)
            raw_input()
            again = raw_input("Lookup another entry? (Y or N)\n").lower()
            if again == "y" or again == "yes" or again == "":
                pass
            else:
                keep_running = False
        else:
            print "\nEntry not found."
            raw_input()
            again = raw_input("Lookup another entry? (Y or N)\n").lower()
            if again == "y" or again == "yes" or again == "":
                pass
            else:
                keep_running = False


def add_entry():
    keep_running = True
    while keep_running == True:
        name = raw_input("Name? ").capitalize()
        result_list = db.query(
            "select * from phonebook where name = '%s'" % name).namedresult()
        if len(result_list) > 0:
            raw_input("This entry already exists.")
            break
        else:
            pass
        phone = raw_input("Phonenumber? ")
        email = raw_input("Email? ").lower()
        confirm = raw_input("\nName: %s\nPhone: %s\nEmail: %s\nIs this information correct? (Y or N)" % (
            name, phone, email)).lower()
        if confirm == "y" or confirm == "yes":
            db.insert('phonebook', name=name, phone_number=phone, email=email)
            new_list = db.query(
                "select * from phonebook where name = '%s'" % name).namedresult()
            raw_input("New Entry:\nName: %s\nPhone: %s\nEmail: %s" % (
                new_list[0].name, new_list[0].phone_number, new_list[0].email))
            break
        else:
            raw_input("New entry cancelled.")
            break


def delete_entry():
    keep_running = True
    while keep_running == True:
        name = raw_input("Name? ").capitalize()
        result_list = db.query(
            "select * from phonebook where name = '%s'" % name).namedresult()
        if len(result_list) == 0:
            raw_input("Entry not found.")
            break
        else:
            pass
        confirm = raw_input("Is this the entry you want to delete? (Y or N)\nName: %s\nPhone: %s\nEmail: %s" % (
            result_list[0].name, result_list[0].phone_number, result_list[0].email)).lower()
        if confirm == "y" or confirm == "yes":
            db.delete('phonebook', {'id': % s}) % result_list.id


while True:
    print "======================="
    print "|Electronic Phone Book|"
    print "======================="
    print "1. Look up an entry"
    print "2. Add an entry"
    print "3. Update an entry"
    print "4. Delete an entry"
    print "5. List all entries"
    print "6. Quit"

    result_list = db.query('select * from phonebook').namedresult()

    response = raw_input('What do you want to do? (1-6): ').lower()

    if response == "1":
        lookup_entry()

    elif response == "2":
        add_entry()

    # if response == "3":
    #
    if response == "4":
        delete_entry()

    elif response == "6":
        break
    else:
        pass
