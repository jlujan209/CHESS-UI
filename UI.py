import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import pandas as pd


class MyApp:
    def __init__(self, master):
        # Load all csv files
        self.caro = pd.read_csv("CaroKann.csv")
        self.queen = pd.read_csv("QueensGambit.csv")
        self.sicilian = pd.read_csv("SicilianDefense.csv")
        self.vienna = pd.read_csv("ViennaGame.csv")
        self.wcc_2018 = pd.read_csv("WCC20181st.csv")
        self.wcc_2013 = pd.read_csv("WCC20136th.csv")

        self.master = master
        self.master.geometry("300x200")
        self.master.title("Learn Chess")

        # Create the frames
        self.frame_main = tk.Frame(self.master)
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame3 = tk.Frame(self.master)
        self.frame4 = tk.Frame(self.master)
        self.frame5 = tk.Frame(self.master)
        self.frame6 = tk.Frame(self.master)

        # Create a Treeview widget to display caro
        self.tree_caro = ttk.Treeview(self.frame1, height=15)
        self.tree_caro['columns'] = list(self.caro.columns)
        for column in list(self.caro.columns):
            self.tree_caro.column(column, width=100)
            self.tree_caro.heading(column, text=column)
        for i, row in enumerate(self.caro.itertuples(), start=1):
            self.tree_caro.insert('', 'end', text=i, values=row[1:])

        # Create a Treeview widget to display queen
        self.tree_queen = ttk.Treeview(self.frame2, height=15)
        self.tree_queen['columns'] = list(self.caro.columns)
        for column in list(self.queen.columns):
            self.tree_queen.column(column, width=100)
            self.tree_queen.heading(column, text=column)
        for i, row in enumerate(self.queen.itertuples(), start=1):
            self.tree_queen.insert('', 'end', text=i, values=row[1:])

        # Create a Treeview widget to display sicilian
        self.tree_sicilian = ttk.Treeview(self.frame3, height=15)
        self.tree_sicilian['columns'] = list(self.sicilian.columns)
        for column in list(self.sicilian.columns):
            self.tree_sicilian.column(column, width=100)
            self.tree_sicilian.heading(column, text=column)
        for i, row in enumerate(self.sicilian.itertuples(), start=1):
            self.tree_sicilian.insert('', 'end', text=i, values=row[1:])

        # Create a Treeview widget to display vienna
        self.tree_vienna = ttk.Treeview(self.frame4, height=15)
        self.tree_vienna['columns'] = list(self.vienna.columns)
        for column in list(self.vienna.columns):
            self.tree_vienna.column(column, width=100)
            self.tree_vienna.heading(column, text=column)
        for i, row in enumerate(self.vienna.itertuples(), start=1):
            self.tree_vienna.insert('', 'end', text=i, values=row[1:])

        # Create a Treeview widget to display wcc_2013
        self.tree_wcc_2013 = ttk.Treeview(self.frame5, height=30)
        self.tree_wcc_2013['columns'] = list(self.wcc_2013.columns)
        for column in list(self.wcc_2013.columns):
            self.tree_wcc_2013.column(column, width=150)
            self.tree_wcc_2013.heading(column, text=column)
        for i, row in enumerate(self.wcc_2013.itertuples(), start=1):
            self.tree_wcc_2013.insert('', 'end', text=i, values=row[1:])

         # Create a Treeview widget to display wcc_2018
        self.tree_wcc_2018 = ttk.Treeview(self.frame6, height=30)
        self.tree_wcc_2018['columns'] = list(self.wcc_2018.columns)
        for column in list(self.wcc_2018.columns):
            self.tree_wcc_2018.column(column, width=150)
            self.tree_wcc_2018.heading(column, text=column)
        for i, row in enumerate(self.wcc_2018.itertuples(), start=1):
            self.tree_wcc_2018.insert('', 'end', text=i, values=row[1:])

        # Create the widgets for the main frame
        self.label_main = tk.Label(
            self.frame_main, text="STUDY CHESS", font=("Arial", 48), bg="Black", fg="White")
        self.label_main.pack()
        self.button1_main = tk.Button(
            self.frame_main, text="Learn the Caro-Kann Opening", font=("Times New Roman", 24), command=self.show_frame1)
        self.button1_main.pack()
        self.button2_main = tk.Button(
            self.frame_main, text="Learn the Queen's Gambit Opening", font=("Times New Roman", 24), command=self.show_frame2)
        self.button2_main.pack()
        self.button3_main = tk.Button(
            self.frame_main, text="Learn the Sicilian Defense Opening", font=("Times New Roman", 24), command=self.show_frame3)
        self.button3_main.pack()
        self.button4_main = tk.Button(
            self.frame_main, text="Learn the Vienna Game", font=("Times New Roman", 24), command=self.show_frame4)
        self.button4_main.pack()
        self.button5_main = tk.Button(
            self.frame_main, text="WCC 2013 6th Game", font=("Times New Roman", 24), command=self.show_frame5)
        self.button5_main.pack()
        self.button6_main = tk.Button(
            self.frame_main, text="WCC 2018 1st Game", font=("Times New Roman", 24), command=self.show_frame6)
        self.button6_main.pack()

        # Create the widgets for frame 1
        self.label1 = tk.Label(self.frame1, text="This is the main line of the Caro-Kann Opening.",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label1.pack()
        self.tree_caro.pack()
        self.button1 = tk.Button(
            self.frame1, text="Return to Home Screen", command=self.show_main_frame)
        self.button1.pack()

        # Create the widgets for frame 2
        self.label2 = tk.Label(self.frame2, text="This is the main line of the Queen's Gambit Opening",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label2.pack()
        self.tree_queen.pack()
        self.button2 = tk.Button(
            self.frame2, text="Return to Home Screen", command=self.show_main_frame)
        self.button2.pack()

        # Create the widgets for frame 3
        self.label3 = tk.Label(self.frame3, text="This is the main line of the Sicilian Defense Opening",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label3.pack()
        self.tree_sicilian.pack()
        self.button3 = tk.Button(
            self.frame3, text="Return to Home Screen", command=self.show_main_frame)
        self.button3.pack()

        # Create the widgets for frame 4
        self.label4 = tk.Label(self.frame4, text="This is the main line of the Vienna Game Opening",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label4.pack()
        self.tree_vienna.pack()
        self.button4 = tk.Button(
            self.frame4, text="Return to Home Screen", command=self.show_main_frame)
        self.button4.pack()

        # Create the widgets for frame 5
        self.label5 = tk.Label(self.frame5, text="Game 6 of the 2013 World Chess Championship",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label5.pack()
        self.tree_wcc_2013.pack()
        self.button5 = tk.Button(
            self.frame5, text="Return to Home Screen", command=self.show_main_frame)
        self.button5.pack()

        # Create the widgets for frame 6
        self.label6 = tk.Label(self.frame6, text="Game 1 of the 2018 World Chess Championship",
                               font=("Arial", 40), bg="Black", fg="White")
        self.label6.pack()
        self.tree_wcc_2018.pack()
        self.button6 = tk.Button(
            self.frame6, text="Return to Home Screen", command=self.show_main_frame)
        self.button6.pack()

        # Show the main frame
        self.show_main_frame()

    def show_main_frame(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame_main.pack()

    def show_frame1(self):
        self.frame_main.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        self.frame_main.pack_forget()
        self.frame1.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame2.pack()

    def show_frame3(self):
        self.frame_main.pack_forget()
        self.frame2.pack_forget()
        self.frame1.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame3.pack()

    def show_frame4(self):
        self.frame_main.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame1.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame4.pack()

    def show_frame5(self):
        self.frame_main.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame1.pack_forget()
        self.frame6.pack_forget()
        self.frame5.pack()

    def show_frame6(self):
        self.frame_main.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame1.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack()


# Create Root Window
root = tk.Tk()


# Load Image
image_file = Image.open("chessboard.jpg")
image = ImageTk.PhotoImage(image_file)

# Create label with image
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


screen_width = root.winfo_screenwidth() - 10
screen_height = root.winfo_screenheight() - 10

root_width = screen_width
root_height = screen_height

app = MyApp(root)

root.geometry(
    f"{root_width}x{root_height}+{int((screen_width-root_width)/2)}+{int((screen_height-root_height)/2)}")
root.mainloop()
