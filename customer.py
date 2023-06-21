import random
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk


class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1290x550+350+320")

        x = random.randint(1000, 9999)
        self.var_ref = StringVar()
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_surname = StringVar()
        self.var_gender = StringVar()
        self.var_telephone_no = StringVar()
        self.var_nationality = StringVar()
        self.var_country = StringVar()

        lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=5, y=2, width=1295, height=50)

        img2 = Image.open("E:/images/Capture100.PNG")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimage2, bd=0, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=40)

        LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"))
        LabelFrameleft.place(x=5, y=50, width=425, height=490)

        lbl_cust_ref = Label(LabelFrameleft, text="Customer Ref", font=("times new roman", 12), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_ref, font=("times new roman", 13), width=29, state="readonly")
        entry_ref.grid(row=0, column=1)

        lbl_cust_name = Label(LabelFrameleft, text="Customer Name", font=("arial", 13), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        self.txt_cust_name = ttk.Entry(LabelFrameleft, textvariable=self.var_cust_name, font=("arial", 13))
        self.txt_cust_name.grid(row=1, column=1)  # Updated line

        lbl_surname = Label(LabelFrameleft, text="Surname:", font=("Arial", 10), padx=2, pady=6)
        lbl_surname.grid(row=2, column=0, sticky=W)
        entry_surname = ttk.Entry(LabelFrameleft, textvariable=self.var_surname, font=("arial", 10, "bold"), width=29)
        entry_surname.grid(row=2, column=1)

        lbl_gender = Label(LabelFrameleft, text="Gender:", font=("arial", 10), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(LabelFrameleft, textvariable=self.var_gender, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_gender["values"] = ("male", "female", "other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        lbl_phone = Label(LabelFrameleft, text="Telephone:", font=("arial", 10), padx=2, pady=6)
        lbl_phone.grid(row=4, column=0, sticky=W)

        entry_phone = ttk.Entry(LabelFrameleft, textvariable=self.var_telephone_no, font=("arial", 10, "bold"), width=29)
        entry_phone.grid(row=4, column=1)

        lbl_nationality = Label(LabelFrameleft, text="Nationality:", font=("arial", 10), padx=2, pady=6)
        lbl_nationality.grid(row=5, column=0, sticky=W)

        entry_nationality = ttk.Entry(LabelFrameleft, textvariable=self.var_nationality, font=("arial", 10, "bold"), width=29)
        entry_nationality.grid(row=5, column=1)

        lbl_country = Label(LabelFrameleft, text="Country:", font=("arial", 10), padx=2, pady=6)
        lbl_country.grid(row=6, column=0, sticky=W)

        entry_country = ttk.Entry(LabelFrameleft, textvariable=self.var_country, font=("arial", 10, "bold"), width=29)
        entry_country.grid(row=6, column=1)

        lbl_id_type = Label(LabelFrameleft, text="ID Type:", font=("arial", 10), padx=2, pady=6)
        lbl_id_type.grid(row=7, column=0, sticky=W)

        combo_id_type = ttk.Combobox(LabelFrameleft, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_id_type["values"] = ("National ID", "Driving License", "Passport")
        combo_id_type.current(0)
        combo_id_type.grid(row=7, column=1)

        lbl_id_number = Label(LabelFrameleft, text="ID Number:", font=("arial", 10), padx=2, pady=6)
        lbl_id_number.grid(row=8, column=0, sticky=W)

        entry_id_number = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_id_number.grid(row=8, column=1)

        lbl_check_in = Label(LabelFrameleft, text="Check In:", font=("arial", 10), padx=2, pady=6)
        lbl_check_in.grid(row=9, column=0, sticky=W)

        entry_check_in = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_check_in.grid(row=9, column=1)

        lbl_check_out = Label(LabelFrameleft, text="Check Out:", font=("arial", 10), padx=2, pady=6)
        lbl_check_out.grid(row=10, column=0, sticky=W)

        entry_check_out = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_check_out.grid(row=10, column=1)

        lbl_meal = Label(LabelFrameleft, text="Meal:", font=("arial", 10), padx=2, pady=6)
        lbl_meal.grid(row=11, column=0, sticky=W)

        combo_meal = ttk.Combobox(LabelFrameleft, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_meal["values"] = ("Breakfast", "Lunch", "Dinner", "Breakfast & Lunch", "Breakfast & Dinner", "Lunch & Dinner", "All Meals")
        combo_meal.current(0)
        combo_meal.grid(row=11, column=1)

        lbl_room_type = Label(LabelFrameleft, text="Room Type:", font=("arial", 10), padx=2, pady=6)
        lbl_room_type.grid(row=12, column=0, sticky=W)

        combo_room_type = ttk.Combobox(LabelFrameleft, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_room_type["values"] = ("Single", "Double", "Family")
        combo_room_type.current(0)
        combo_room_type.grid(row=12, column=1)

        lbl_room_no = Label(LabelFrameleft, text="Room No:", font=("arial", 10), padx=2, pady=6)
        lbl_room_no.grid(row=13, column=0, sticky=W)

        combo_room_no = ttk.Combobox(LabelFrameleft, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_room_no["values"] = ("101", "102", "103", "104", "105", "106")
        combo_room_no.current(0)
        combo_room_no.grid(row=13, column=1)

        lbl_room_ext_no = Label(LabelFrameleft, text="Room Ext No:", font=("arial", 10), padx=2, pady=6)
        lbl_room_ext_no.grid(row=14, column=0, sticky=W)

        entry_room_ext_no = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_room_ext_no.grid(row=14, column=1)

        lbl_room_rate = Label(LabelFrameleft, text="Room Rate:", font=("arial", 10), padx=2, pady=6)
        lbl_room_rate.grid(row=15, column=0, sticky=W)

        entry_room_rate = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_room_rate.grid(row=15, column=1)

        lbl_amount_paid = Label(LabelFrameleft, text="Amount Paid:", font=("arial", 10), padx=2, pady=6)
        lbl_amount_paid.grid(row=16, column=0, sticky=W)

        entry_amount_paid = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_amount_paid.grid(row=16, column=1)

        lbl_amount_due = Label(LabelFrameleft, text="Amount Due:", font=("arial", 10), padx=2, pady=6)
        lbl_amount_due.grid(row=17, column=0, sticky=W)

        entry_amount_due = ttk.Entry(LabelFrameleft, font=("arial", 10, "bold"), width=29)
        entry_amount_due.grid(row=17, column=1)

        lbl_address = Label(LabelFrameleft, text="Address:", font=("arial", 10), padx=2, pady=6)
        lbl_address.grid(row=18, column=0, sticky=W)

        txt_address = Text(LabelFrameleft, font=("arial", 10, "bold"), width=30, height=4)
        txt_address.grid(row=18, column=1, padx=2)

        LabelFrameright = LabelFrame(self.root, bd=2, relief=RIDGE)
        LabelFrameright.place(x=430, y=50, width=860, height=490)

        lbl_search = Label(LabelFrameright, text="Search By", font=("arial", 10), padx=2, pady=6)
        lbl_search.grid(row=0, column=0, sticky=W)

        combo_search = ttk.Combobox(LabelFrameright, font=("arial", 10, "bold"), width=27, state="readonly")
        combo_search["values"] = ("Ref", "Name", "Mobile")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        entry_search = ttk.Entry(LabelFrameright, font=("arial", 10, "bold"), width=29)
        entry_search.grid(row=0, column=2)

        btn_search = Button(LabelFrameright, text="Search", font=("arial", 10, "bold"), width=10)
        btn_search.grid(row=0, column=3, padx=5)

        btn_show_all = Button(LabelFrameright, text="Show All", font=("arial", 10, "bold"), width=10)
        btn_show_all.grid(row=0, column=4, padx=5)

        Table_Frame = Frame(LabelFrameright, bd=2, relief=RIDGE)
        Table_Frame.place(x=10, y=60, width=835, height=410)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.Cust_table = ttk.Treeview(Table_Frame, column=(
        "ref", "name", "surname", "gender", "phone", "nationality", "country", "id_type", "id_number", "check_in",
        "check_out", "meal", "room_type", "room_no", "room_ext_no", "room_rate", "amount_paid", "amount_due", "address"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_table.xview)
        scroll_y.config(command=self.Cust_table.yview)

        self.Cust_table.heading("ref", text="Ref")
        self.Cust_table.heading("name", text="Name")
        self.Cust_table.heading("surname", text="Surname")
        self.Cust_table.heading("gender", text="Gender")
        self.Cust_table.heading("phone", text="Phone")
        self.Cust_table.heading("nationality", text="Nationality")
        self.Cust_table.heading("country", text="Country")
        self.Cust_table.heading("id_type", text="ID Type")
        self.Cust_table.heading("id_number", text="ID Number")
        self.Cust_table.heading("check_in", text="Check In")
        self.Cust_table.heading("check_out", text="Check Out")
        self.Cust_table.heading("meal", text="Meal")
        self.Cust_table.heading("room_type", text="Room Type")
        self.Cust_table.heading("room_no", text="Room No")
        self.Cust_table.heading("room_ext_no", text="Room Ext No")
        self.Cust_table.heading("room_rate", text="Room Rate")
        self.Cust_table.heading("amount_paid", text="Amount Paid")
        self.Cust_table.heading("amount_due", text="Amount Due")
        self.Cust_table.heading("address", text="Address")

        self.Cust_table["show"] = "headings"

        self.Cust_table.column("ref", width=100)
        self.Cust_table.column("name", width=100)
        self.Cust_table.column("surname", width=100)
        self.Cust_table.column("gender", width=100)
        self.Cust_table.column("phone", width=100)
        self.Cust_table.column("nationality", width=100)
        self.Cust_table.column("country", width=100)
        self.Cust_table.column("id_type", width=100)
        self.Cust_table.column("id_number", width=100)
        self.Cust_table.column("check_in", width=100)
        self.Cust_table.column("check_out", width=100)
        self.Cust_table.column("meal", width=100)
        self.Cust_table.column("room_type", width=100)
        self.Cust_table.column("room_no", width=100)
        self.Cust_table.column("room_ext_no", width=100)
        self.Cust_table.column("room_rate", width=100)
        self.Cust_table.column("amount_paid", width=100)
        self.Cust_table.column("amount_due", width=100)
        self.Cust_table.column("address", width=150)

        self.Cust_table.pack(fill=BOTH, expand=1)

        self.Cust_table.bind("<ButtonRelease>", self.get_cursor)

    def get_cursor(self, ev):
        cursor_row = self.Cust_table.focus()
        contents = self.Cust_table.item(cursor_row)
        row = contents["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_surname.set(row[2])
        self.var_gender.set(row[3])
        self.var_telephone_no.set(row[4])
        self.var_nationality.set(row[5])
        self.var_country.set(row[6])
        self.var_id_type.set(row[7])
        self.var_id_number.set(row[8])
        self.var_check_in.set(row[9])
        self.var_check_out.set(row[10])
        self.var_meal.set(row[11])
        self.var_room_type.set(row[12])
        self.var_room_no.set(row[13])
        self.var_room_ext_no.set(row[14])
        self.var_room_rate.set(row[15])
        self.var_amount_paid.set(row[16])
        self.var_amount_due.set(row[17])

    def add_customer(self):
        if self.var_ref.get() == "" or self.var_cust_name.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="password",
                    database="hotel"
                )
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO customers (ref, name, surname, gender, phone, nationality, country, id_type, id_number, check_in, check_out, meal, room_type, room_no, room_ext_no, room_rate, amount_paid, amount_due, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_surname.get(),
                        self.var_gender.get(),
                        self.var_telephone_no.get(),
                        self.var_nationality.get(),
                        self.var_country.get(),
                        self.var_id_type.get(),
                        self.var_id_number.get(),
                        self.var_check_in.get(),
                        self.var_check_out.get(),
                        self.var_meal.get(),
                        self.var_room_type.get(),
                        self.var_room_no.get(),
                        self.var_room_ext_no.get(),
                        self.var_room_rate.get(),
                        self.var_amount_paid.get(),
                        self.var_amount_due.get(),
                        self.txt_address.get("1.0", END)
                    )
                )
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Customer has been added successfully!")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}")
