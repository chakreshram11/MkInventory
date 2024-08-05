import tkinter as tk
from tkinter import ttk

class CreateWindow:
    def __init__(self, root, object_selection):
        self.root = root
        self.object_selection = object_selection

    def open_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title(f"Create {self.object_selection}")

        label = tk.Label(new_window, text=f"Create {self.object_selection}", font=("Times New Roman", 14))
        label.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        if self.object_selection == "Brands":
            self.create_brands_window(new_window)
        elif self.object_selection == "Category":
            self.create_category_window(new_window)
        elif self.object_selection == "Location":
            self.create_location_window(new_window)
        elif self.object_selection == "Products":
            self.create_products_window(new_window)
        elif self.object_selection == "Suppliers":
            self.create_suppliers_window(new_window)
        elif self.object_selection == "Transport":
            self.create_transport_window(new_window)

    def create_brands_window(self, window):
        label_brand_name = tk.Label(window, text="Brand Name:", font=("Times New Roman", 12))
        label_brand_name.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry_brand_name = tk.Entry(window)
        entry_brand_name.grid(row=1, column=1, pady=5, padx=5, sticky='w')

        label_brand_name_telugu = tk.Label(window, text="Brand Name Telugu:", font=("Times New Roman", 12))
        label_brand_name_telugu.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        entry_brand_name_telugu = tk.Entry(window)
        entry_brand_name_telugu.grid(row=2, column=1, pady=5, padx=5, sticky='w')

        label_brand_description = tk.Label(window, text="Brand Description:", font=("Times New Roman", 12))
        label_brand_description.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        entry_brand_description = tk.Entry(window)
        entry_brand_description.grid(row=3, column=1, pady=5, padx=5, sticky='w')

        label_brand_type = tk.Label(window, text="Brand Type:", font=("Times New Roman", 12))
        label_brand_type.grid(row=4, column=0, pady=5, padx=5, sticky='w')

        label_brand_type = tk.Label(window, text="Brand Type:", font=("Times New Roman", 12))
        label_brand_type.grid(row=4, column=0, pady=5, padx=5, sticky='w')

        brand_types = ["Pre_packed", "Packed", "NA"]  # Replace with actual types
        selected_brand_type = tk.StringVar()
        selected_brand_type.set("Select a type")  # Placeholder

        combobox_brand_type = ttk.Combobox(window, textvariable=selected_brand_type, values=brand_types,
                                           state='readonly')
        combobox_brand_type.grid(row=4, column=1, pady=5, padx=5, sticky='w')

        button_save_brand = tk.Button(window, text="Save Brand", command=lambda: print(f"Brand '{entry_brand_name.get()}' of type '{combobox_brand_type.get()}' saved"))
        button_save_brand.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

    def create_category_window(self, window):
        label = tk.Label(window, text="Enter Category Name:", font=("Times New Roman", 12))
        label.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry = tk.Entry(window)
        entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')
        button = tk.Button(window, text="Save Category", command=lambda: print(f"Category '{entry.get()}' saved"))
        button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

    def create_location_window(self, window):
        label = tk.Label(window, text="Enter Location:", font=("Times New Roman", 12))
        label.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry = tk.Entry(window)
        entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')
        button = tk.Button(window, text="Save Location", command=lambda: print(f"Location '{entry.get()}' saved"))
        button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

    def create_products_window(self, window):
        label_product_name = tk.Label(window, text="Product Name:", font=("Times New Roman", 12))
        label_product_name.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry_product_name = tk.Entry(window)
        entry_product_name.grid(row=1, column=1, pady=5, padx=5, sticky='w')

        label_product_name_telugu = tk.Label(window, text="Product Name Telugu:", font=("Times New Roman", 12))
        label_product_name_telugu.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        entry_product_name_telugu = tk.Entry(window)
        entry_product_name_telugu.grid(row=2, column=1, pady=5, padx=5, sticky='w')

        label_product_description = tk.Label(window, text="Product Description:", font=("Times New Roman", 12))
        label_product_description.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        entry_product_description = tk.Entry(window)
        entry_product_description.grid(row=3, column=1, pady=5, padx=5, sticky='w')

        button_save_product = tk.Button(window, text="Save Product", command=lambda: print(f"Product '{entry_product_name.get()}' saved"))
        button_save_product.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

    def create_suppliers_window(self, window):
        label = tk.Label(window, text="Enter Supplier Name:", font=("Times New Roman", 12))
        label.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry = tk.Entry(window)
        entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')
        button = tk.Button(window, text="Save Supplier", command=lambda: print(f"Supplier '{entry.get()}' saved"))
        button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

    def create_transport_window(self, window):
        label = tk.Label(window, text="Enter Transport Details:", font=("Times New Roman", 12))
        label.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        entry = tk.Entry(window)
        entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')
        button = tk.Button(window, text="Save Transport", command=lambda: print(f"Transport '{entry.get()}' saved"))
        button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        window.grid_columnconfigure(1, weight=1)

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    app = CreateWindow(root, "Products")
    app.open_window()
    root.mainloop()
