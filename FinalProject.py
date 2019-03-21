# Author: Khushpreet Singh
# version: 1.0.1
# Date Created: 13 Jan 2019
# Date Modified: 21 March 2019

from tkinter import *
import sqlite3 as GUIdb
import csv as file

"""list for datalistbox"""
listBoxList = []

class FinalProject:

    def loadcsv(self):
        """this loadcsv function read csv and creating connection as well as inserting row in database. It is also populating
        the listbox from database"""
        try:
            path = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
            # opening csv file and putting file in object
            with open(path, encoding="ISO-8859-1") as csvfile:
                read = file.reader(csvfile)
                csvList = [] #list will contain csv file data
                j = 0
                for data in read:
                    if (j > 3):
                        csvList.append(data)
                    j += 1

            con = GUIdb.connect("FinalProject.db")  # connection with database
            print("Author is Khushpreet Singh")

            with con:
                cur = con.cursor() # cursor object
                cur.execute("DROP TABLE IF EXISTS flowers")# dropping table
                """creating table flower for data"""
                cur.execute("create table IF not exists flowers(id INTEGER PRIMARY KEY AUTOINCREMENT,Species VARCHAR(70),c_year INTEGER, Julian_Day_of_Year INTEGER,Plant_Identification_Number INTEGER,Number_of_Buds INTEGER,Number_of_Flowers INTEGER,Number_of_Flowers_that_have_Reached_Maturity INTEGER,Observer_Initials VARCHAR(20),Observer_Comments VARCHAR(20))")
                """inserting data to flowers table"""
                for i in range(len(csvList)):

                    cur.execute('INSERT INTO flowers (Species,c_year,Julian_Day_of_Year,Plant_Identification_Number,Number_of_Buds,Number_of_Flowers,Number_of_Flowers_that_have_Reached_Maturity,Observer_Initials,Observer_Comments) VALUES (?,?,?,?,?,?,?,?,?)',(csvList[i]))

                print("inserted sucessfully")
                print("Developed by Khushpreet Singh")

                cur.execute("SELECT * FROM flowers;")
                """Fetching data from datbase"""
                data = cur.fetchall()
                """clearing datalistbox"""
                DatalistBox.delete(0, END)
                """clearing notification or msg listbox"""
                msgbox.delete(0,END)
                #clearing arraylist toclean any garbage value before appending
                listBoxList.clear()
                for d in data:
                    listBoxList.append(d)
                """headers for listbox"""
                header = ["ID, species, Year, Julian Day of Year, Plant Identification Number, Number of Buds, Number of Flowers, Number of Flowers that have Reached Maturity, Observer Initials, Observer Comments"]
                for col in header:
                    DatalistBox.insert(0,col)
                """poulating datalistBox """
                for row in listBoxList:
                    print(row)
                    DatalistBox.insert(END, str(row[0]).ljust(10) + str(row[1]).ljust(25) + str(row[2]).ljust(10) + str(
                        row[3]).ljust(10) + str(row[4]).ljust(10) + str(row[5]).ljust(10) + str(row[6]).ljust(10) + str(
                        row[7]).ljust(10) + str(row[8]).ljust(10) + str(row[9]))
                msgbox.insert(END,"Data from csv file loaded in database sucessfully.Now you can perform operations on data")
        except:
            print("error loadig file. may be file missing")
        return "CSVloaded"


    def insert(self):
        """this insert function get data from entry fields and creating connection as well as inserting row in database. It is also
        populating new entry in the listbox from database"""

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")
        with con:
            cur = con.cursor()# cursor object
            """create table if not exists"""
            cur.execute("create table IF not exists flowers(id INTEGER PRIMARY KEY AUTOINCREMENT ,Species VARCHAR(70) , c_year INTEGER, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials VARCHAR(20),  Observer_Comments VARCHAR(20))")
            """inserting new row in database"""
            cur.execute(
                'INSERT INTO flowers (Species,c_year,Julian_Day_of_Year,Plant_Identification_Number,Number_of_Buds,Number_of_Flowers,Number_of_Flowers_that_have_Reached_Maturity,Observer_Initials,Observer_Comments) VALUES (?,?,?,?,?,?,?,?,?)',
                [(species_text.get()), (year_text.get()), (Day_text.get()),
                                 (Identification_text.get()), (Buds_text.get()), (flowers_text.get()),
                                 (Maturity_text.get()), (Initials_text.get()), (Comments_text.get())])
            cur.execute("SELECT * FROM flowers;")
            data = cur.fetchall()
            """clearing datalistbox"""
            DatalistBox.delete(0,END)
            # clearing arraylist to clean any garbage value before appending
            listBoxList.clear()
            for d in data:
                listBoxList.append(d)
            """header for datalistbox"""
            header = [
                "ID, species, Year, Julian Day of Year, Plant Identification Number, Number of Buds, Number of Flowers, Number of Flowers that have Reached Maturity, Observer Initials, Observer Comments"]
            for col in header:
                DatalistBox.insert(0, col)
            """inserting new entry at the end of datalistbox"""
            for row in listBoxList:
                print(row)
                DatalistBox.insert(END, str(row[0]).ljust(10) + str(row[1]).ljust(25) + str(row[2]).ljust(10) + str(
                    row[3]).ljust(10) + str(row[4]).ljust(10) + str(row[5]).ljust(10) + str(row[6]).ljust(10) + str(
                    row[7]).ljust(10) + str(row[8]).ljust(10) + str(row[9]))

            """clearing entry fields"""
            species_text.delete(0, END)
            year_text.delete(0, END)
            Day_text.delete(0, END)
            Identification_text.delete(0, END)
            Buds_text.delete(0, END)
            flowers_text.delete(0, END)
            Maturity_text.delete(0, END)
            Initials_text.delete(0, END)
            Comments_text.delete(0, END)
            msgbox.insert(END,"Data Row inserted in database table with new id at the end of list please scroll to view")
            print("list updated")
        return "datasaved"


    def searchData(self):

        """this searchData function get data from database and populate the data in entry fields for deletion and updation
           and creating connection."""

        msgbox.insert(END,"Searching........")
        """clearing entry fields before seraching entry and populating entry field with correct data"""
        species_text.delete(0,END)
        year_text.delete(0,END)
        Day_text.delete(0,END)
        Identification_text.delete(0,END)
        Buds_text.delete(0,END)
        flowers_text.delete(0,END)
        Maturity_text.delete(0,END)
        Initials_text.delete(0,END)
        Comments_text.delete(0,END)

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")
        with con:
            cur = con.cursor()# cursor object
            """getting value or id from serach_text entry """
            id = Search_text.get()
            """select where id is"""
            cur.execute('select * from flowers where id ='+id)
            row = cur.fetchall()
            """populating entry fields with searched id"""
            for data in row:
                species_text.insert(1,str(data[1]))
                year_text.insert(2,str(data[2]))
                Day_text.insert(3,str(data[3]))
                Identification_text.insert(4,str(data[4]))
                Buds_text.insert(5,str(data[5]))
                flowers_text.insert(6,str(data[6]))
                Maturity_text.insert(7,str(data[7]))
                Initials_text.insert(8,str(data[8]))
                Comments_text.insert(9,str(data[9]))
            print(row)

            msgbox.insert(END,"Search completed & data is populated in entry fields for updation and deletion")

        return "search"


    def updaterow(self):
        """this updaterow function get updated data from entry fields and creating connection as well as updates row in database. It is also
                populating updated entry in the listbox """

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")
        with con:
            cur = con.cursor()# database cursor
            """getting data from entry field into variables and getting id as well for update"""
            sp = species_text.get()
            year = year_text.get()
            day = Day_text.get()
            pid = Identification_text.get()
            buds = Buds_text.get()
            fnum = Buds_text.get()
            mat = Maturity_text.get()
            initials = Initials_text.get()
            comm = Comments_text.get()
            id = Search_text.get()
            """updating data with sql query where id is= Search_text.get()"""
            cur.execute("""UPDATE flowers SET Species=?,c_year=?,Julian_Day_of_Year=?,Plant_Identification_Number=?,Number_of_Buds=?, Number_of_Flowers=?,Number_of_Flowers_that_have_Reached_Maturity=?,Observer_Initials=?,Observer_Comments=? WHERE id=?""",(sp,year,day,pid,buds,fnum,mat,initials,comm,id))
            cur.execute("SELECT * FROM flowers;")
            data = cur.fetchall()
            """clearing datalistbox"""
            DatalistBox.delete(0, END)
            # clearing arraylist to clean any garbage value before appending
            listBoxList.clear()
            for d in data:
                listBoxList.append(d)
            """datalistbox header"""
            header = [
                "ID, species, Year, Julian Day of Year, Plant Identification Number, Number of Buds, Number of Flowers, Number of Flowers that have Reached Maturity, Observer Initials, Observer Comments"]
            for col in header:
                DatalistBox.insert(0, col)
            for row in listBoxList:
                print(row)
                DatalistBox.insert(END, str(row[0]).ljust(10) + str(row[1]).ljust(25) + str(row[2]).ljust(10) + str(
                    row[3]).ljust(10) + str(row[4]).ljust(10) + str(row[5]).ljust(10) + str(row[6]).ljust(10) + str(
                    row[7]).ljust(10) + str(row[8]).ljust(10) + str(row[9]))
            """clearing entry fields for new entries and new updations/serach"""
            species_text.delete(0, END)
            year_text.delete(0, END)
            Day_text.delete(0, END)
            Identification_text.delete(0, END)
            Buds_text.delete(0, END)
            flowers_text.delete(0, END)
            Maturity_text.delete(0, END)
            Initials_text.delete(0, END)
            Comments_text.delete(0, END)
            print("data updtaed")
            msgbox.insert(END,"Row with id = "+id+" is updated & listbox is also updated.....")

        return "Rowupdated"

    def deleterow(self):

        """this deleterow function deletes data from database and update the listbox."""

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")
        with con:
            """ database cursor"""
            cur = con.cursor()
            """getting value or id from serach_text entry """
            id = Search_text.get()
            print(id)
            """delete fron DB where id is Search_text.get() """
            cur.execute('delete from flowers where id ='+id)
            data = cur.execute('select * from main.flowers')
            print(cur)
        """clearing datalistbox"""
        DatalistBox.delete(0, END)
        # clearing arraylist to clean any garbage value before appending
        listBoxList.clear()
        for d in data:
            listBoxList.append(d)
        """datalistbox headers"""
        header = [
            "ID, species, Year, Julian Day of Year, Plant Identification Number, Number of Buds, Number of Flowers, Number of Flowers that have Reached Maturity, Observer Initials, Observer Comments"]
        for col in header:
            DatalistBox.insert(0, col)

        for row in listBoxList:
            print(row)
            DatalistBox.insert(END, str(row[0]).ljust(10) + str(row[1]).ljust(25) + str(row[2]).ljust(10) + str(
                row[3]).ljust(10) + str(row[4]).ljust(10) + str(row[5]).ljust(10) + str(row[6]).ljust(10) + str(
                row[7]).ljust(10) + str(row[8]).ljust(10) + str(row[9]))
        msgbox.insert(END,"Data Row with id "+id+" is deleted from database and listbox...")
        msgbox.insert(END,"Listbox updated....")
        """clearing entry fields"""
        species_text.delete(0, END)
        year_text.delete(0, END)
        Day_text.delete(0, END)
        Identification_text.delete(0, END)
        Buds_text.delete(0, END)
        flowers_text.delete(0, END)
        Maturity_text.delete(0, END)
        Initials_text.delete(0, END)
        Comments_text.delete(0, END)

        return "Row_deleted"


"""main desktop GUI window for widgets"""
root = Tk()
root.title("FinalProject 1.0.1 by KhushPreet Singh")
"""info label"""
info = Label(root,text="fill the fields to insert data & click on submit")
info.grid(row=0,column =0,sticky=W)

"""species label and entry fields is placed in root with help of grid"""
species = Label(root,text="species")
species.grid(row=1,column =0,sticky=W)
species_text = Entry(root)
species_text.grid(row=1,column=1)

"""year label and entry field"""
year = Label(root, text="Year")
year.grid(row=2, column=0,sticky=W)
year_text = Entry(root)
year_text.grid(row=2, column=1)

"""day label and entry field"""
Day = Label(root, text="Julian Day of Year")
Day.grid(row=3, column=0,sticky=W)
Day_text = Entry(root)
Day_text.grid(row=3, column=1)

"""Plant Identification Number label and entry field"""
Identification = Label(root, text="Plant Identification Number")
Identification.grid(row=4, column=0,sticky=W)
Identification_text = Entry(root)
Identification_text.grid(row=4, column=1)

"""number of buds label and entry field"""
buds = Label(root, text="Number of Buds")
buds.grid(row=5, column=0,sticky=W)
Buds_text = Entry(root)
Buds_text.grid(row=5, column=1)

"""number of flowers label and entry field"""
flower = Label(root, text="Number of Flowers")
flower.grid(row=6, column=0,sticky=W)
flowers_text = Entry(root)
flowers_text.grid(row=6, column=1)

"""Number of Flowers that have Reached Maturity label and entry field"""
Maturity = Label(root, text="Number of Flowers that have Reached Maturity")
Maturity.grid(row=7, column=0,sticky=W)
Maturity_text = Entry(root)
Maturity_text.grid(row=7, column=1)

"""Observer Initials label and entry field"""
Initials = Label(root, text="Observer Initials")
Initials.grid(row=8, column=0,sticky=W)
Initials_text = Entry(root)
Initials_text.grid(row=8, column=1)

"""Observer comments label and entry field"""
Comments = Label(root, text="Observer Comments")
Comments.grid(row=9, column=0,sticky=W)
Comments_text = Entry(root)
Comments_text.grid(row=9, column=1)


"""submit buttond calling insert method when clicked"""
submit = Button(root,text="Submit",anchor=CENTER)
submit.grid(row=11, column=1,sticky=EW)
submit.bind('<Button-1>', FinalProject.insert)

"""csvButton loads data from csv when clicked by calling loadcsv function"""
csvButton = Button(root, text="insert from csv", anchor=CENTER)
csvButton.grid(row=12, column=1,sticky=EW)
csvButton.bind("<Button-1>", FinalProject.loadcsv)

"""Search button calls searchData method and populate entry fields for deleting and updation"""
Search = Button(root, text="serachID")
Search.grid(row=14, column=1,sticky=N)
Search.bind("<Button-1>", FinalProject.searchData)
"""serach entry field"""
Search_text = Entry(root)
Search_text.grid(row=13, column=1,sticky=S)

"""update button calls updaterow method for updating data into database"""
update = Button(root, text="update",fg="#006366")
update.grid(row=14, column=1,sticky=SW)
update.bind("<Button-1>", FinalProject.updaterow)

"""delete Button calls deleterow method to delete data from database"""
delete = Button(root, text="Delete", anchor=N)
delete.grid(row=14, column=1,sticky=SE)
delete.bind("<Button-1>", FinalProject.deleterow)
DatalistBox = Listbox(width = 100)

"""list box shows the data when user will perform CRUD operations"""
DatalistBox.grid(row=0,column=2, rowspan=12,padx=5, sticky=E+W+S+N)
DatalistBox.insert(END,"Please click on 'insert from csv' button first & this listbox will display data......!!")
DatalistBox.itemconfig(END, foreground="RED")

"""gives updates to user when any operation performed on database table"""
msgbox = Listbox(width = 50)
msgbox.grid(row=13,column=2, rowspan=2, sticky=E+W+S+N)
msgbox.insert(END,"This will display notify the user about operations......!!")

"""name box gives instructions to user"""
namebox = Listbox(width = 50)
namebox.grid(row=13,column=0, rowspan=2, sticky=E+W+S+N)
namebox.insert(END,"1. Developed by Khushpreet Singh")
namebox.insert(END,"2. User will load data from csv")
namebox.insert(END,"3. User can submit with entry fields")
namebox.insert(END,"4. User can Update data by seraching with ID")
namebox.insert(END,"5. User can delete by seraching with ID")
namebox.insert(END,"6. Insert from CSV is highly recommended for better result")

root.mainloop()


