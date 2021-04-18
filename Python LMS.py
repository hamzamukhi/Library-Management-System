import datetime
import os
os.getcwd()

#creating a class
class LMS:
    """ This class is used to keep record of books library.
    It has total four module: "Display Books", "Issue Books", "Return Books", "Add Books" """

    #Constructor
    def __init__(self,list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name =  library_name
        self.books_dict = {}
        Id = 1
        #reading our database from notepad
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            #python dict datastruc(update book dict)
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name": "","Issue_data":"","Status":"Available"}})
            Id = Id + 1
    def display_books(self):
        print("------------------List of Books--------------")
        print("Books ID", "\t","Title")
        print("---------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"), "- [",value.get("Status"),"]")


    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%S")
        if books_id in self.books_dict.keys():
            #book is issued to someone else
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} \
                    on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
        
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Books Issued Succesfully !!! \n")
    
        else:
            print("Book ID not Found !!!")
        

# adding based on book name and book name should not be blank and cannot be exceed to 25
    def add_books(self):
        new_books = input("Enter Books Title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title lenghth is too long!! Title length should be 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"This Books '{new_books}' has been added succesfully !!!")

    
    def return_books(self):
        books_id = input("Enter books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in Library. Please check your book ID.")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
              self.books_dict[books_id]["lender_name"] = ""
              self.books_dict[books_id]["Issue_date"] = ""
              self.books_dict[books_id]["Status"] = "Available"
              print("Successfully Updated !!! \n")

        else:
            print("Book ID is not Found")  

try:
    myLMS = LMS("list_of_books.txt","Python's")
    press_key_list = {"D": "Display Books", "I":"Issued Books","A": "Add Books","R":"Return Books","Q":"Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n.................WELCOME To HM LIBRARY SYSTEM.....\n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Books")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Books\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
                print("Something went wrong.Please check your input !!!")
            
    
l = LMS("List_of_books.txt","Python's Library")
print(l.display_books()) 