# Author: Khushpreet Singh
# version: 1.0
# Date Created: 13 Jan 2019
# Date Modified: 19 March 2019
from tkinter import *
import sqlite3 as GUIdb
import csv as file

listBoxList = []
id_db=id
class GUI():

    def __init__(self):
        self.loadcsv()
        self.insert()
        self.searchData()
        self.updaterow()
        self.deleterow()


def loadcsv(self):
    """this insertData function read csv and creating connection as well as inserting row in database. It is also retrieving
    records of database """
    try:
        path = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
        # opening csv file and putting file in object
        with open(path, encoding="ISO-8859-1") as csvfile:
            read = file.reader(csvfile)
            csvList = []
            j = 0
            for data in read:
                if (j > 3):
                    csvList.append(data)
                j += 1

        con = GUIdb.connect("FinalProject.db")  # connection with database
        print("Author is Khushpreet Singh")

        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS flowers")
            cur.execute("create table IF not exists flowers(id INTEGER PRIMARY KEY AUTOINCREMENT ,Species VARCHAR(70) , c_year INTEGER, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials VARCHAR(20),  Observer_Comments VARCHAR(20))")
            for i in range(len(csvList)):
                print(i)
                cur.execute('INSERT INTO flowers (Species,c_year,Julian_Day_of_Year,Plant_Identification_Number,Number_of_Buds,Number_of_Flowers,Number_of_Flowers_that_have_Reached_Maturity,Observer_Initials,Observer_Comments) VALUES (?,?,?,?,?,?,?,?,?)',(csvList[i]))

            print("inserted sucessfully")
            print("Developed by Khushpreet Singh")

            cur.execute("SELECT * FROM flowers;")

            data = cur.fetchall()
            Lb1.delete(0, END)
            msgbox.delete(0,END)
            listBoxList.clear()
            for d in data:
                listBoxList.append(d)
            headers = ["ID","species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
                       "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
                       "Observer Comments"]
            row_format = "{:<15s}{:<30s}{:<20s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
            Lb1.insert(0, row_format.format(*headers, sp=" "))

            for row in listBoxList:
                print(row)
                Lb1.insert(END, str(row[0]).ljust(15)+str(row[1]).ljust(25) +str(row[2]).ljust(20) +str(row[3]).ljust(50) +str(row[4]).ljust(50) +str(row[5]).ljust(40) +str(row[6]).ljust(50)+str(row[7]).ljust(70) +str(row[8]).ljust(40) +str(row[9]))
            msgbox.insert(END,"Data from csv file loaded in database sucessfully.Now you can perform operations on data")
    except:
        print("error loadig file. may be file missing")
    return "CSV loaded sucessfully"


def insert(self):

    con = GUIdb.connect("FinalProject.db")  # connection with database
    print("Author is Khushpreet Singh")
    with con:
        cur = con.cursor()
        cur.execute("create table IF not exists flowers(id INTEGER PRIMARY KEY AUTOINCREMENT ,Species VARCHAR(70) , c_year INTEGER, Julian_Day_of_Year INTEGER,  Plant_Identification_Number INTEGER,  Number_of_Buds INTEGER,  Number_of_Flowers INTEGER,  Number_of_Flowers_that_have_Reached_Maturity INTEGER,  Observer_Initials VARCHAR(20),  Observer_Comments VARCHAR(20))")
        cur.execute(
            'INSERT INTO flowers (Species,c_year,Julian_Day_of_Year,Plant_Identification_Number,Number_of_Buds,Number_of_Flowers,Number_of_Flowers_that_have_Reached_Maturity,Observer_Initials,Observer_Comments) VALUES (?,?,?,?,?,?,?,?,?)',
            [(species_text.get()), (year_text.get()), (Day_text.get()),
                             (Identification_text.get()), (Buds_text.get()), (flowers_text.get()),
                             (Maturity_text.get()), (Initials_text.get()), (Comments_text.get())])
        cur.execute("SELECT * FROM flowers;")
        data = cur.fetchall()
        Lb1.delete(0,END)
        listBoxList.clear()
        for d in data:
            listBoxList.append(d)

        headers = ["ID", "species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
                   "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
                   "Observer Comments"]
        row_format = "{:<15s}{:<30s}{:<20s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
        Lb1.insert(0, row_format.format(*headers, sp=" "))

        for row in listBoxList:
            print(row)
            Lb1.insert(END, str(row[0]).ljust(15) + str(row[1]).ljust(25) + str(row[2]).ljust(20) + str(row[3]).ljust(
                50) + str(row[4]).ljust(50) + str(row[5]).ljust(40) + str(row[6]).ljust(50) + str(row[7]).ljust(
                70) + str(row[8]).ljust(40) + str(row[9]))
        species_text.delete(0, END)
        year_text.delete(0, END)
        Day_text.delete(0, END)
        Identification_text.delete(0, END)
        Buds_text.delete(0, END)
        flowers_text.delete(0, END)
        Maturity_text.delete(0, END)
        Initials_text.delete(0, END)
        Comments_text.delete(0, END)
        msgbox.insert(END,"Data Row inserted in database table..........")
        print("list updated")
    return "data saved"


def searchData(self):
    msgbox.insert(END,"Searching........")

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
        cur = con.cursor()
        id = Search_text.get()
        cur.execute('select * from flowers where id ='+id)
        row = cur.fetchall()
        for d in row:
            id_text.setvar(id)
            species_text.insert(1,str(d[1]))
            year_text.insert(2,str(d[2]))
            Day_text.insert(3,str(d[3]))
            Identification_text.insert(4,str(d[4]))
            Buds_text.insert(5,str(d[5]))
            flowers_text.insert(6,str(d[6]))
            Maturity_text.insert(7,str(d[7]))
            Initials_text.insert(8,str(d[8]))
            Comments_text.insert(9,str(d[9]))
        print(row)

        msgbox.insert(END,"Search completed & data is populated in entry fields for updation and deletion")

    return "search"


def updaterow(self):

    con = GUIdb.connect("FinalProject.db")  # connection with database
    print("Author is Khushpreet Singh")
    with con:
        cur = con.cursor()
        sp = species_text.get()
        print(sp)
        year = year_text.get()
        print(year)
        day = Day_text.get()
        pid = Identification_text.get()
        buds = Buds_text.get()
        fnum = Buds_text.get()
        mat = Maturity_text.get()
        initials = Initials_text.get()
        comm = Comments_text.get()
        id = Search_text.get()
        cur.execute("""UPDATE flowers SET Species=?,c_year=?,Julian_Day_of_Year=?,Plant_Identification_Number=?,Number_of_Buds=?, Number_of_Flowers=?,Number_of_Flowers_that_have_Reached_Maturity=?,Observer_Initials=?,Observer_Comments=? WHERE id=?""",(sp,year,day,pid,buds,fnum,mat,initials,comm,id))
        row = cur.fetchall()
        cur.execute("SELECT * FROM flowers;")
        data = cur.fetchall()
        Lb1.delete(0, END)
        listBoxList.clear()
        for d in data:
            listBoxList.append(d)

        headers = ["ID", "species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
                   "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
                   "Observer Comments"]
        row_format = "{:<15s}{:<30s}{:<20s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
        Lb1.insert(0, row_format.format(*headers, sp=" "))

        for row in listBoxList:
            print(row)
            Lb1.insert(END, str(row[0]).ljust(15) + str(row[1]).ljust(25) + str(row[2]).ljust(20) + str(row[3]).ljust(
                50) + str(row[4]).ljust(50) + str(row[5]).ljust(40) + str(row[6]).ljust(50) + str(row[7]).ljust(
                70) + str(row[8]).ljust(40) + str(row[9]))
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
        msgbox.insert(END,"Row updated & listbox is also updated.....")

    return "Row updated"

def deleterow(self):

    con = GUIdb.connect("FinalProject.db")  # connection with database
    print("Author is Khushpreet Singh")
    with con:
        cur = con.cursor()
        id = Search_text.get()
        print(id)
        cur.execute('delete from flowers where id ='+id)
        data = cur.execute('select * from main.flowers')
        print(cur)
    Lb1.delete(0, END)
    listBoxList.clear()
    for d in data:
        listBoxList.append(d)

    headers = ["ID", "species", "Year", "Julian Day of Year", "Plant Identification Number", "Number of Buds",
               "Number of Flowers", "Number of Flowers that have Reached Maturity", "Observer Initials",
               "Observer Comments"]
    row_format = "{:<15s}{:<30s}{:<20s}{:<30s}{:<40s}{:<30s}{:<30s}{:<50s}{:<30s}{:<30s}"
    Lb1.insert(0, row_format.format(*headers, sp=" "))

    for row in listBoxList:
        print(row)
        Lb1.insert(END, str(row[0]).ljust(15) + str(row[1]).ljust(25) + str(row[2]).ljust(20) + str(row[3]).ljust(
            50) + str(row[4]).ljust(50) + str(row[5]).ljust(40) + str(row[6]).ljust(50) + str(row[7]).ljust(
            70) + str(row[8]).ljust(40) + str(row[9]))
    msgbox.insert(END,"Data Row with id "+id+" is deleted from database and listbox...")
    msgbox.insert(END,"Listbox updated....")

    species_text.delete(0, END)
    year_text.delete(0, END)
    Day_text.delete(0, END)
    Identification_text.delete(0, END)
    Buds_text.delete(0, END)
    flowers_text.delete(0, END)
    Maturity_text.delete(0, END)
    Initials_text.delete(0, END)
    Comments_text.delete(0, END)
    return "Row deleted"


len_max = 12

root = Tk()

id = Label(root,text="fill the fields to insert data & click on submit")
id.grid(row=0,column =0,sticky=W)
id_text = Label(root,text="")
id_text.grid(row=0,column=1)

species = Label(root,text="species")
species.grid(row=1,column =0,sticky=W)
species_text = Entry(root)
species_text.grid(row=1,column=1)

year = Label(root, text="Year")
year.grid(row=2, column=0,sticky=W)
year_text = Entry(root)
year_text.grid(row=2, column=1)

Day = Label(root, text="Julian Day of Year")
Day.grid(row=3, column=0,sticky=W)
Day_text = Entry(root)
Day_text.grid(row=3, column=1)

Identification = Label(root, text="Plant Identification Number")
Identification.grid(row=4, column=0,sticky=W)
Identification_text = Entry(root)
Identification_text.grid(row=4, column=1)

buds = Label(root, text="Number of Buds")
buds.grid(row=5, column=0,sticky=W)
Buds_text = Entry(root)
Buds_text.grid(row=5, column=1)

flower = Label(root, text="Number of Flowers")
flower.grid(row=6, column=0,sticky=W)
flowers_text = Entry(root)
flowers_text.grid(row=6, column=1)

Maturity = Label(root, text="Number of Flowers that have Reached Maturity")
Maturity.grid(row=7, column=0,sticky=W)
Maturity_text = Entry(root)
Maturity_text.grid(row=7, column=1)


Initials = Label(root, text="Observer Initials")
Initials.grid(row=8, column=0,sticky=W)
Initials_text = Entry(root)
Initials_text.grid(row=8, column=1)

Comments = Label(root, text="Observer Comments")
Comments.grid(row=9, column=0,sticky=W)
Comments_text = Entry(root)
Comments_text.grid(row=9, column=1)

submit = Button(root,text="Submit",anchor=CENTER)
submit.grid(row=11, column=1,sticky=EW)
submit.bind('<Button-1>', insert)

csvButton = Button(root, text="insert from csv", anchor=CENTER)
csvButton.grid(row=12, column=1,sticky=EW)
csvButton.bind("<Button-1>", loadcsv)

Search = Button(root, text="serachID")
Search.grid(row=14, column=1,sticky=N)
Search.bind("<Button-1>", searchData)

Search_text = Entry(root)
Search_text.grid(row=13, column=1,sticky=S)

update = Button(root, text="update", anchor=N,bg="black",fg="#006366")

update.grid(row=14, column=1,sticky=SW)
update.bind("<Button-1>", updaterow)

delete = Button(root, text="Delete", anchor=N)
delete.grid(row=14, column=1,sticky=SE)
delete.bind("<Button-1>", deleterow)
Lb1 = Listbox(width = 100)

Lb1.grid(row=0,column=2, rowspan=12,
    padx=5, sticky=E+W+S+N)
Lb1.insert(END,"Please click on 'insert from csv' button first & this listbox will display data......!!")
Lb1.itemconfig(END, foreground="RED")

msgbox = Listbox(width = 50)
msgbox.grid(row=13,column=2, rowspan=2, sticky=E+W+S+N)
msgbox.insert(END,"This will display notify the user about operations......!!")


namebox = Listbox(width = 50)
namebox.grid(row=13,column=0, rowspan=2, sticky=E+W+S+N)
namebox.insert(END,"1. Developed by Khushpreet Singh")
namebox.insert(END,"2. User will load data from csv")
namebox.insert(END,"3. User can submit with entry fields")
namebox.insert(END,"4. User can delete by seraching with ID")
namebox.insert(END,"5. User can Update data by seraching with ID")
namebox.insert(END,"6. Insert from CSV highly recommended")



root.mainloop()

root = Tk()

obj = GUI()
obj.saveData()
obj.insertData()
