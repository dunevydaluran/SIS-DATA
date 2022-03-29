#Author: Daluran, Dunevy D.
import tkinter as tk
from tkinter import GROOVE, ttk
import csv
import os

#Creates a new 'data.csv' if that file is not present
if not os.path.exists('data.csv'):
        with open('data.csv','w') as csv_file:
                fieldnames=["ID Number","Last Name","First Name","Course","Year Level", "Gender"]
                write = csv.DictWriter(csv_file,fieldnames=fieldnames)
                write.writeheader()

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Information System")

title_label = tk.Label(win,text="Student Information System",font=("Bookman Old Style",30,"bold"),border=12,relief=tk.GROOVE,bg="pink",foreground="black")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Enter Details",font=("Bookman Old Style",20),bd=12,relief=tk.GROOVE,bg="lightpink")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame = tk.Frame(win,bd=12,bg="lightpink",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=620,height=575)

#=======Variables=======#

idnumber = tk.StringVar()
lastname = tk.StringVar()
firstname = tk.StringVar()
course = tk.StringVar()
yearlvl = tk.StringVar()
gender = tk.StringVar()

search_by = tk.StringVar()
#=======ENTRY=======#
idnumber_lbl = tk.Label(detail_frame,text="ID Number",font=('Bookman Old Style',14),bg="lightpink")
idnumber_lbl.grid(row=0,column=0,padx=2,pady=2)

idnumber_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=idnumber)
idnumber_ent.grid(row=0,column=1,padx=2,pady=2)

lastname_lbl = tk.Label(detail_frame,text="Last Name",font=('Bookman Old Style',14),bg="lightpink")
lastname_lbl.grid(row=1,column=0,padx=2,pady=2)

lastname_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=lastname)
lastname_ent.grid(row=1,column=1,padx=2,pady=2)

firstname_lbl = tk.Label(detail_frame,text="First Name",font=('Bookman Old Style',14),bg="lightpink")
firstname_lbl.grid(row=2,column=0,padx=2,pady=2)

firstname_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=firstname)
firstname_ent.grid(row=2,column=1,padx=2,pady=2)

course_lbl = tk.Label(detail_frame,text="Course",font=('Bookman Old Style',14),bg="lightpink")
course_lbl.grid(row=3,column=0,padx=2,pady=2)

course_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=course)
course_ent.grid(row=3,column=1,padx=2,pady=2)

yearlvl_lbl = tk.Label(detail_frame,text="Year level",font=('Bookman Old Style',14),bg="lightpink")
yearlvl_lbl.grid(row=4,column=0,padx=2,pady=2)

yearlvl_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=yearlvl)
yearlvl_ent.grid(row=4,column=1,padx=2,pady=2)

gender_lbl = tk.Label(detail_frame,text="Gender",font=('Bookman Old Style',14),bg="lightpink")
gender_lbl.grid(row=5,column=0,padx=2,pady=2)

gender_ent = tk.Entry(detail_frame,bd=7,font=('Bookman Old Style',14),textvariable=gender)
gender_ent.grid(row=5,column=1,padx=2,pady=2)

#+===============================#

#==========Buttons==============#

btn_frame = tk.Frame(detail_frame,bg="lightpink",bd=10,relief=tk.GROOVE)
btn_frame.place(x=25,y=340,width=370,height=120)

add_btn = tk.Button(btn_frame,bg="lightpink",text="Add",bd=5,font=("Bookman Old Style",13),width=14)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightpink",text="Update",bd=5,font=("Bookman Old Style",13),width=14)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightpink",text="Delete",bd=5,font=("Bookman Old Style",13),width=14)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

edit_btn = tk.Button(btn_frame,bg="lightpink",text="Edit",bd=5,font=("Bookman Old Style",13),width=14)
edit_btn.grid(row=1,column=1,padx=3,pady=2)

#+===============================#

#==========Search==============#

search_frame = tk.Frame(data_frame,bg="lightpink",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame,text="Search",bg="lightpink",font=("Bookman Old Style",14))
search_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("Bookman Old Style",14),state="readonly",textvariable=search_by)
search_in['values'] = ("ID Number", "Last Name", "First Name", "Course", "Year Level", "Gender")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(search_frame,text="Search", font=("Bookman Old Style",13),bd=5,width=6,bg=("lightpink"))
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn = tk.Button(search_frame,text="Show All", font=("Bookman Old Style",13),bd=5,width=6,bg=("lightpink"))
showall_btn.grid(row=0,column=3,padx=12,pady=2)

#==============================

#==========Database Frame==============#

main_frame = tk.Frame(data_frame,bg="lightpink",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

''''ID Number, Last Name, First Name, Course, Year Level, Gender'''

student_table = ttk.Treeview(data_frame,columns=("ID Number","Last Name", "First Name", "Course", "Year Level", "Gender"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("ID Number",text="ID Number")
student_table.heading("Last Name",text="Last Name")
student_table.heading("First Name",text="First Name")
student_table.heading("Course",text="Course")
student_table.heading("Year Level",text="Year Level")
student_table.heading("Gender",text="Gender")

student_table.column("ID Number",width=100)
student_table.column("Last Name",width=100)
student_table.column("First Name",width=100)
student_table.column("Course",width=100)
student_table.column("Year Level",width=100)
student_table.column("Gender",width=100)

student_table['show'] = 'headings'



student_table.pack(fill=tk.BOTH,expand=True)


win.mainloop()