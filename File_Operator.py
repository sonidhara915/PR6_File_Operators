# PR.6 File Operator

import datetime

class journal:

    
    def add_journal_manager(self):
        try:
            f = "f.txt"

            str_input = input("Enter your journal entry:\n")

            time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")

            #print(time)

            with open(f,"a") as file:
                file.write(f"[{time}]")
                file.write(str_input)
            
            print("\nEntry added successfully!")
        
        except Exception as e:
            
            print("Error ",e)


    def view_journal_manager(self):

        try:
            f = "f.txt"
            with open(f,"r") as file:

                content = file.read()

                if content:
                    print("\nAll Journal Entries")
                    print("-------------------------------")
                    print(content)
                         
                else:
                    print("\nJournal is empty!\n")

        except FileNotFoundError :
            print("No journal entries found.Start by adding a new entry!")

        except Exception as e:
            print("\nThe journal file does not exist.Please add a new entry first:",e)

    def Search_journal_manager(self):

        f = "f.txt"
        data = input("\nEnter Keyword or Date to Search :")

        try:
            file = open(f,"r")
            lines = file.readlines()
            found = False

            for line in lines :
                if f.lower() in line.lower():
                    print(line)
                    found = True
            if not found:
                print("\nKeyword Don't match")

            file.close()

        except FileNotFoundError:
            print(f"\n No entries were found for the keyword: {data}")
                
         
    def del_journal_manager(self):

        try:
            f = "f.txt"

            read = input("\n Are you sure you want to delete all entries?(yes / No):\n")

            if read == "yes":
                

                with open(f,"w") as file:
                    ent = file.write("Contend Deleted")
                    print(ent)
                    print("Conted Deleted Successfully !!")

            elif read == "no":
                print("your Entry's are safe ")
            

            else:
                ("All journal entries have been deleted.")
                

        except FileNotFoundError :
            print("No journal entries have been deleted.")

        except Exception as e:
            print("Error on this path:",e)

my_journal = journal()
while True:
    print("\n==== Welcome to Personal journal Manager ====\n")
    print("\nSelecte One Option From Given Option\n")
    print(" 1. Add a New Entry:")
    print(" 2. Viwe All Entery:")
    print(" 3. Search for an Entry:")
    print(" 4. Delete an Entry:")
    print(" 5 Exit")

    opp=input("\nEnter your choice")


    if opp == "1":
        my_journal.add_journal_manager()

    elif opp == "2":
        my_journal.view_journal_manager()

    elif opp == "3":
        my_journal.Search_journal_manager()

    elif opp == "4":
        my_journal.del_journal_manager()

    elif opp == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid option.Please select a valid option from the menu.\n")    
            
            


            
        

            
