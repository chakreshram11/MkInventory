import tkinter as tk

class UpdateWindow:
    def __init__(self, root, object_selection):
        self.root = root
        self.object_selection = object_selection

    def open_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title(f"Update {self.object_selection}")

        label = tk.Label(new_window, text=f"Update {self.object_selection}", font=("Times New Roman", 14))
        label.pack(pady=20, padx=20)

        if self.object_selection == "Brands":
            self.update_brands_window(new_window)
        elif self.object_selection == "Category":
            self.update_category_window(new_window)
        elif self.object_selection == "Location":
            self.update_location_window(new_window)
        elif self.object_selection == "Products":
            self.update_products_window(new_window)
        elif self.object_selection == "Suppliers":
            self.update_suppliers_window(new_window)
        elif self.object_selection == "Transport":
            self.update_transport_window(new_window)

    def update_brands_window(self, window):
        label = tk.Label(window, text="Enter Brand Name to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Brand", command=lambda: print(f"Updating Brand '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def update_category_window(self, window):
        label = tk.Label(window, text="Enter Category Name to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Category", command=lambda: print(f"Updating Category '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def update_location_window(self, window):
        label = tk.Label(window, text="Enter Location to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Location", command=lambda: print(f"Updating Location '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def update_products_window(self, window):
        label = tk.Label(window, text="Enter Product Name to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Product", command=lambda: print(f"Updating Product '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def update_suppliers_window(self, window):
        label = tk.Label(window, text="Enter Supplier Name to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Supplier", command=lambda: print(f"Updating Supplier '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def update_transport_window(self, window):
        label = tk.Label(window, text="Enter Transport Details to Update:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Update Transport", command=lambda: print(f"Updating Transport '{entry.get()}'"))
        button.pack(pady=10, padx=10)
