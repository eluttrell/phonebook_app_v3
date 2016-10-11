import pg
db = pg.DB(dbname='phonebook_db')


def lookup_entry():
    name = raw_input("Name? ").capitalize()
    for i in range(len(result_list)):
        if result_list[i].name == name:
            print "\n%s:\n\nPhone: %s\nEmail: %s\n" % (result_list[i].name, result_list[i].phone_number, result_list[i].email)
            raw_input()
            found = True
        else:
            print "Entry not found."


while True:
    print "======================="
    print "|Electronic Phone Book|"
    print "======================="
    print "1. Look up an entry"
    print "2. Add an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"

    result_list = db.query('select * from phonebook').namedresult()

    response = raw_input('What do you want to do? (1-5): ').lower()

    if response == "1":
        lookup_entry()

    # if response == "2":
    #
    # if response == "3":
    #
    # if response == "4":

    if response == "5":
        break
