import pg
from os.path import exists
db = pg.DB(dbname='phonebook_db')


query = db.query('select * from phonebook')
# print query
new_list = query.dictresult()
print new_list
raw_input()


keep_running = True
while keep_running == True:
    print "======================="
    print "|Electronic Phone Book|"
    print "======================="
    print "1. Look up an entry"
    print "2. Add an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    response = raw_input('What do you want to do? (1-5): ').lower()

    # phonebook_dict = {}
    #
    # phonebook_file = open('phonebook.pickle', 'r')
    # phonebook_dict = pickle.load(phonebook_file)
    # phonebook_file.close()
    #
    # if response == "1":
    #     lookup_entry()
    # elif response == "2":
    #     set_entry()
    # elif response == "3":
    #     delete_entry()
    # elif response == "4":
    #     list_entries()
    #     raw_input('')
    # elif response == "5" or response == "QUIT" or response == "Q":
    #     break
    # else:
    #     non_valid = raw_input("Not a valid entry.\n")

    if response == "1":
        continue_lookup = True
        while continue_lookup == True:
            look_up = raw_input(
                "What is the name you would like to look up?").capitalize()
            if look_up == "Q" or look_up == "Quit" or look_up == "Cancel":
                pass
            for i in range(len(new_list)):
                if look_up in new_list[i]['name']:
                    print "%s:\n\nPhone: %s\nEmail: %s" % (new_list[i]['name'], new_list[i]['phone_number'], new_list[i]['email'])
                    raw_input()
                    continue_lookup = False
                else:
                    print "Entry not found."
                    continue_lookup = False
        if continue_lookup == False:
            pass

    if response == "2":
        continue_set_entry = True
        while continue_set_entry == True:
            add_entry = raw_input(
                "What is the name you would like to add?").capitalize()
            if add_entry == "Q" or add_entry == "Quit" or add_entry == "Cancel":
                break

            if add_entry in new_list:
                print "That name already exists."
                try_again = raw_input(
                    "Would you like to try a different name?").lower()
                if try_again == "y" or try_again == "yes":
                    add_entry = raw_input(
                        "What is the name you would like to add?").capitalize()
                else:
                    continue_set_entry = False
            new_number = raw_input(
                "What is %s's phone number? (###-###-####)" % add_entry)
            new_email = raw_input(
                "What is %s's email address? (name@domain.com)" % add_entry).lower()
            print "New name: %s\nPhone: %s\nEmail: %s" % (add_entry, new_number, new_email)
            confirm = raw_input("Is this correct? (Y or N)").lower()
            if confirm == "y" or confirm == "yes":
                db.insert('phonebook', name=add_entry,
                          phone_number=new_number, email=new_email)
                query = db.query('select * from phonebook')
                print query
                raw_input()
                try_again = raw_input(
                    "Would you like to try a different name?").lower()
                if try_again == "y" or try_again == "yes":
                    pass
                elif try_again == "n" or try_again == "no":
                    continue_set_entry = False
                else:
                    continue_set_entry = False
        pass
    if response == "5":
        break
