from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import openpyxl


def insert():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    course=e_course.get()
    fee=e_fee.get()
    #checking if user given all details or not
    if id=="" or name=="" or phone=="" or course=="" or fee=="" :
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="rameshSQL123#", database="studentsdb")
        cursor=con.cursor()
        cursor.execute("insert into student values('"+id+"','"+name+"','"+phone+"','"+course+"','"+fee+"')")
        con.commit()
        #after inserting we need to clear input boxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_course.delete(0,'end')
        e_fee.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        con.close()       
def delete():
    if(e_id.get()==""):
        MessageBox.showinfo("Delete Status","ID is Compulsory for delete")
    else:
        con=mysql.connect(host="localhost",user="root",password="rameshSQL123#", database="studentsdb")
        cursor=con.cursor()
        cursor.execute("delete from student where id='"+e_id.get() +"'")
        con.commit()
        #after inserting we need to clear input boxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_course.delete(0,'end')
        e_fee.delete(0,'end')
        show()
        MessageBox.showinfo("Delete Status","Deleted Successfully")
        con.close()
def update():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    course=e_course.get()
    fee=e_fee.get()
    #checking if user given all details or not
    if id=="" or name=="" or phone=="" or course=="" or fee=="" :
        MessageBox.showinfo("Update Details","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="rameshSQL123#", database="studentsdb")
        cursor=con.cursor()
        cursor.execute("update student set name='"+name+"',phone='"+phone+"',course='"+course+"',fee='"+fee+"' where id='"+id+"'")
        con.commit()
        #after inserting we need to clear input boxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_course.delete(0,'end')
        e_fee.delete(0,'end')
        show()
        MessageBox.showinfo("Update Status","Updated Successfully")
        con.close()   
def get():
    if e_id.get() == "":
        MessageBox.showinfo("Fetch Status", "ID is compulsory for Fetch")
    else:
        con = mysql.connect(host="localhost", user="root", password="rameshSQL123#", database="studentsdb")
        cursor = con.cursor()
        cursor.execute("select * from student where id='" + e_id.get() + "'")
        rows = cursor.fetchall()
        
        if not rows:
            MessageBox.showinfo("Fetch Status", "No ID is present")
        else:
            # Clear entry widgets before inserting new data
            e_name.delete(0, END)
            e_phone.delete(0, END)
            e_course.delete(0, END)
            e_fee.delete(0, END)

            for row in rows:
                e_name.insert(0, row[1])
                e_phone.insert(0, row[2])
                e_course.insert(0, row[3])
                e_fee.insert(0, row[4])

            MessageBox.showinfo("Fetch Status", "Fetched Successfully")
        
        con.close()
    

def show():
    con = mysql.connect(host="localhost", user="root", password="rameshSQL123#", database="studentsdb")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertData = "{:<5} {:<15} {:<15} {:<15} {:<10}".format(str(row[0]), row[1], row[2], row[3], row[4])
        list.insert(list.size(), insertData)
    con.close()

def export_to_excel():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["ID", "Name", "Phone", "Course", "Fee"])

    for i in range(list.size()):
        data = list.get(i).split()
        sheet.append(data)

    workbook.save("student_data.xlsx")
    MessageBox.showinfo("Export Status", "Data exported to student_data.xlsx")

#creating root window
root=Tk()
root.geometry("800x400")#800 width and 400 pixels is Height
root.title("Manikanta Computers")

# Load the background image
bg_image = PhotoImage(file="bgp.png")

# Create a label with the background image
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#creating labels
id=Label(root,text="ID",font=('bold',10)).place(x=20,y=30)
name=Label(root,text="Name",font=('bold',10)).place(x=20,y=60)
phone=Label(root,text="Phone",font=('bold',10)).place(x=20,y=90)
course=Label(root,text="Course",font=('bold',10)).place(x=20,y=120)
fee=Label(root,text="Fees",font=('bold',10)).place(x=20,y=150)

#creating entry boxes
e_id=Entry(root)
e_id.place(x=150,y=30)

e_name=Entry(root)
e_name.place(x=150,y=60)

e_phone=Entry(root)
e_phone.place(x=150,y=90)

e_course=Entry(root)
e_course.place(x=150,y=120)

e_fee=Entry(root)
e_fee.place(x=150,y=150)


#creating buttons
insert=Button(root,text="Insert",font=("italic",10),bg="white",command=insert).place(x=40,y=200)
delete=Button(root,text="Delete",font=("italic",10),bg="white",command=delete).place(x=90,y=200)
update=Button(root,text="Update",font=("italic",10),bg="white",command=update).place(x=150,y=200)
get=Button(root,text="Get",font=("italic",10),bg="white",command=get).place(x=210,y=200)
export_excel_button = Button(root, text="Export to Excel", font=("italic", 10), bg="white", command=export_to_excel)
export_excel_button.place(x=40, y=230)

list=Listbox(root, width=80, height=20)
list.place(x=290,y=40)
show()
root.mainloop()
