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
            add = raw_input(
                "\nEntry not found. Would you like to add it? (Y or N)\n").lower()
            if add == "yes" or add == "y" or add == "":
                add_from_lookup(name)
            else:
                pass
            again = raw_input("Lookup another entry? (Y or N)\n").lower()
            if again == "y" or again == "yes" or again == "":
                pass
            else:
                keep_running = False


def add_from_lookup(name):
    keep_running = True
    while keep_running == True:
        result_list = db.query(
            "select * from phonebook where name = '%s'" % name).namedresult()
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
            raw_input("\n\tNew Entry:\n\nName: %s\nPhone: %s\nEmail: %s" % (
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
        confirm = raw_input("\nName: %s\nPhone: %s\nEmail: %s\nIs this the entry you want to delete? (Y or N)" % (
            result_list[0].name, result_list[0].phone_number, result_list[0].email)).lower()
        if confirm == "y" or confirm == "yes":
            db.delete('phonebook', {'id': '%d' % result_list[0].id})
            raw_input("Entry deleted.")
            break


def list_entries():
    keep_running = True
    while keep_running == True:
        id_list = db.query("select id from phonebook").namedresult()
        result_list = db.query("select * from phonebook").namedresult()
        for i in range(len(id_list)):
            print "\nName: %s\nPhone: %s\nEmail: %s\n" % (result_list[i].name, result_list[i].phone_number, result_list[i].email)
        raw_input()
        break

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

    if response == "3":
        update_entry()

    if response == "4":
        delete_entry()

    if response == "5":
        list_entries()

    elif response == "6":
        break
    else:
        pass
