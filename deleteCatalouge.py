import tkinter as tk

class DeleteWindow:
    def __init__(self, root, object_selection):
        self.root = root
        self.object_selection = object_selection

    def open_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title(f"Delete {self.object_selection}")

        label = tk.Label(new_window, text=f"Delete {self.object_selection}", font=("Times New Roman", 14))
        label.pack(pady=20, padx=20)

        if self.object_selection == "Brands":
            self.delete_brands_window(new_window)
        elif self.object_selection == "Category":
            self.delete_category_window(new_window)
        elif self.object_selection == "Location":
            self.delete_location_window(new_window)
        elif self.object_selection == "Products":
            self.delete_products_window(new_window)
        elif self.object_selection == "Suppliers":
            self.delete_suppliers_window(new_window)
        elif self.object_selection == "Transport":
            self.delete_transport_window(new_window)

    def delete_brands_window(self, window):
        label = tk.Label(window, text="Enter Brand Name to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Brand", command=lambda: print(f"Deleting Brand '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def delete_category_window(self, window):
        label = tk.Label(window, text="Enter Category Name to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Category", command=lambda: print(f"Deleting Category '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def delete_location_window(self, window):
        label = tk.Label(window, text="Enter Location to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Location", command=lambda: print(f"Deleting Location '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def delete_products_window(self, window):
        label = tk.Label(window, text="Enter Product Name to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Product", command=lambda: print(f"Deleting Product '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def delete_suppliers_window(self, window):
        label = tk.Label(window, text="Enter Supplier Name to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Supplier", command=lambda: print(f"Deleting Supplier '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def delete_transport_window(self, window):
        label = tk.Label(window, text="Enter Transport Details to Delete:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Delete Transport", command=lambda: print(f"Deleting Transport '{entry.get()}'"))
        button.pack(pady=10, padx=10)
