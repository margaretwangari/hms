from tkinter import *

from PIL import Image, ImageTk

from customer import Cust_win


class HotelmanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open("E:/images/hotel-1831072_1280.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimage1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        img2 = Image.open("E:/images/Capture100.PNG")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=220, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        img3 = Image.open("E:/images/reception-g1a6e324c7_1280.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        lblimg3.place(x=220, y=0, width=1310, height=590)

        img4 = Image.open("E:/images/bread-g1007395bf_1280.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=240, width=230, height=210)

        img5 = Image.open("E:/images/Capture.PNG")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=440, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)

if __name__ == "__main__":
    root = Tk()
    hotel_system = HotelmanagementSystem(root)
    root.mainloop()

   