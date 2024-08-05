import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import importlib
# import os
# from PIL import Image, ImageTk
from Layouts.createCatalouge import CreateWindow
from Layouts.searchProductStockLayout import SearchProductStockLayout
from Layouts.addProductStock import AddProductStock
from Layouts.modifyProduct import ModifyProduct
from Layouts.modifyProductMongoDB import ModifyProductMongoDB
from Layouts.addProductMongoDB import  AddProductMongoDB
from Layouts.searchOrderMongoDB import SearchOrderMongoDB
from Layouts.addOrderMongoDB import AddOrderMongoDB
from DB.dBTransactionsMongoDB import DBTransactionsMongoDB
from DB.dBTransactions import DBTransactions

class InventoryLayout:
    def __init__(self, root):
        self.root = root
        self.root.title("ManaKirana Inventory Management")
        # self.root.geometry("800x600")  # Initial window size
        self.root.iconbitmap(r"C:\Users\chakr\PycharmProjects\MkInventory\.venv\Asserts\FeviconManaKirana.ico")
        self.root.attributes("-fullscreen", True)  # Make the window fullscreen
        # Load the logo image
        # logo_image = Image.open("../Asserts/logo_ManaKirana.png")
        # print(os.path.abspath("../Asserts/logo_ManaKirana.png"))
        # logo_photo = ImageTk.PhotoImage(logo_image)
        self.product_frame = tk.Frame(root)
        self.order_frame = tk.Frame(root)
        self.catalouge_frame = tk.Frame(root)

        self.product_frame.grid(row=0, column=0)
        self.order_frame.grid(row=1, column=0)
        self.catalouge_frame.grid(row=2, column=0)
        # Create the frames for different sections
        self.create_frames()
        # Add buttons for window control
        self.add_window_control_buttons()
        self.object_combobox = None
        self.operations_combobox = None

    def button_click_handler_product(self):
        # Instantiate the SearchProductStockLayout class
        search_layout = SearchProductStockLayout()
        # Call the method you want to execute
        search_layout.open_window()
        # print(search_layout.root)

    def open_create_window(self):
        # Logic to open the create operation window
        print("Opening create operation window for Products")
        # Example code to open a new window
        create_window = tk.Toplevel(self.root)
        create_window.title("Create Product")
        label = tk.Label(create_window, text="Create Product Window")
        label.pack(padx=20, pady=20)

    def button_click_handler_add_product(self):
        # Instantiate the SearchProductStockLayout class
        add_layout = AddProductStock()
        # Call the method you want to execute
        add_layout.open_window()
        # print(search_layout.root)
    def button_click_handler_modify_product(self):
        # Instantiate the SearchProductStockLayout class
        modify_product = ModifyProduct()
        # Call the method you want to execute
        modify_product.open_window()
        # print(search_layout.root)
    def button_click_handler_modify_productMongoDB(self):
        # Instantiate the SearchProductStockLayout class
        modifyProductMongoDB = ModifyProductMongoDB()
        # Call the method you want to execute
        modifyProductMongoDB.open_window()
        # print(search_layout.root)

    def button_click_handler_add_productMongoDB(self):
        child_window = tk.Toplevel(self.root)  # Pass 'self.root' instead of 'root'
        db_handler = DBTransactionsMongoDB()  # Instance of MongoDB handler
        mysql_handler = DBTransactions()  # Instance of MySQL handler
        addProductMongoDB = AddProductMongoDB(child_window, db_handler, mysql_handler)
        child_window.mainloop()
    def button_click_handler_search_orderMongoDB(self):
        # Instantiate the SearchProductStockLayout class
        searchOrderMongoDB = SearchOrderMongoDB()
        # Call the method you want to execute
        searchOrderMongoDB
        # child_window.mainloop()
        # print(search_layout.root)
    def button_click_handler_add_orderMongoDB(self):
        # Instantiate the SearchProductStockLayout class
        addOrderMongoDB = AddOrderMongoDB()
        # Call the method you want to execute
        addOrderMongoDB


    def create_frames(self):
        # Create a frame for the Product section
        self.product_frame = tk.Frame(self.root, bg="lightgrey")
        self.product_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # # Create a frame for the Package section
        # self.package_frame = tk.Frame(self.root, bg="lightgrey")
        # self.package_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Create a frame for the Order section
        self.order_frame = tk.Frame(self.root, bg="lightgrey")
        self.order_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # # Create a frame for the Delivery section
        # self.delivery_frame = tk.Frame(self.root, bg="lightgrey")
        # self.delivery_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        #create a frame for the catalouge secation
        self.catalouge_frame = tk.Frame(self.root, bg="lightgrey")
        self.catalouge_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


        # Ensure equal weight for rows and columns
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def add_window_control_buttons(self):
        # Create title label
        # title_label = tk.Label(self.root, text="ManaKirana Inventory Management",image=logo_photo, font=("Arial", 18) , bg="white", fg="brown")
        # title_label = tk.Label(self.root, text="ManaKirana Inventory Management", font=("Arial", 18),bg="white", fg="brown", image=logo_photo, compound="left")
        title_label = tk.Label(self.root, text="ManaKirana Inventory Management", font=("Arial", 18), bg="white",fg="brown")
        title_label.grid(row=0, column=0,  columnspan=2,padx=10, pady=10)

        # Create button for closing window
        close_button = tk.Button(self.root, text="Close", command=self.close_window, font=("Arial", 14), bg="red",
                                 fg="white")
        close_button.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ne")

        # Temporarily remove minimize_button to prevent overlap
        minimize_button = tk.Button(self.root, text="Minimize", command=self.minimize_window, font=("Arial", 14),
                                    bg="white", fg="red")
        minimize_button.grid_remove()

        # Calculate the position of minimize_button after close_button
        self.root.update()  # Update the widget to get its dimensions
        close_button.update()  # Update the button to get its dimensions
        minimize_button.grid(row=0, column=1, padx=close_button.winfo_width() + 10, pady=10, sticky="ne")

    def close_window(self):
        self.root.destroy()

    def minimize_window(self):
        self.root.iconify()

    def create_section(self, frame, title):
        section_label = tk.Label(frame, text=title, font=("Arial", 14), fg="brown")
        section_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    def add_widget(self, frame, label_text, grid_config, widget_type, btn_cmd=None, font=None, combobox_values=None):
        if widget_type == "button":
            button = tk.Button(frame, text=label_text.strip(), anchor="w", font=("Arial", 12), fg="green", bg="white", command=btn_cmd)
            button.grid(row=grid_config[0], column=grid_config[1], padx=5, pady=5, sticky="nsew")
        elif widget_type == "combobox":
            if combobox_values is None:
                combobox_values = []
            combobox = ttk.Combobox(frame, values=combobox_values, state="readonly")
            combobox.grid(row=grid_config[0], column=grid_config[1], padx=5, pady=5, sticky="nsew")
            combobox.set("Select an option")  # Set placeholder
            if grid_config == (1, 1):
                self.object_combobox = combobox
            elif grid_config == (2, 1):
                self.operations_combobox = combobox
        else:
            if font is None:
                font = tkFont.Font(family="Times New Roman", size=12)
            label = tk.Label(frame, text=label_text.strip(), font=font)
            label.grid(row=grid_config[0], column=grid_config[1], padx=5, pady=5, sticky="nsew")

    def button_click_handler_catelogue(self):
        object_selection = self.object_combobox.get()
        operation_selection = self.operations_combobox.get()
        if object_selection and operation_selection:
            self.open_window_based_on_selection(object_selection, operation_selection)

    def open_window_based_on_selection(self, object_selection, operation_selection):
        file_mapping = {
            "create": "createCatalouge",
            "search": "searchCatalouge",
            "update": "updateCatalouge",
            "delete": "deleteCatalouge"
        }

        try:
            module_name = f"Layouts.{file_mapping[operation_selection]}"
            operation_module = importlib.import_module(module_name)

            window_class_name = f"{operation_selection.capitalize()}Window"
            window_class = getattr(operation_module, window_class_name)
            window_instance = window_class(self.root, object_selection)
            window_instance.open_window()
        except ImportError:
            print(f"Module {module_name} not found.")
        except AttributeError:
            print(f"Class {window_class_name} not found in {module_name}.")