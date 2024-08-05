import tkinter as tk

class SearchWindow:
    def __init__(self, root, object_selection):
        self.root = root
        self.object_selection = object_selection

    def open_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title(f"Search {self.object_selection}")

        label = tk.Label(new_window, text=f"Search {self.object_selection}", font=("Times New Roman", 14))
        label.pack(pady=20, padx=20)

        if self.object_selection == "Brands":
            self.search_brands_window(new_window)
        elif self.object_selection == "Category":
            self.search_category_window(new_window)
        elif self.object_selection == "Location":
            self.search_location_window(new_window)
        elif self.object_selection == "Products":
            self.search_products_window(new_window)
        elif self.object_selection == "Suppliers":
            self.search_suppliers_window(new_window)
        elif self.object_selection == "Transport":
            self.search_transport_window(new_window)

    def search_brands_window(self, window):
        label = tk.Label(window, text="Enter Brand Name to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Brand", command=lambda: print(f"Searching Brand '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def search_category_window(self, window):
        label = tk.Label(window, text="Enter Category Name to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Category", command=lambda: print(f"Searching Category '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def search_location_window(self, window):
        label = tk.Label(window, text="Enter Location to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Location", command=lambda: print(f"Searching Location '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def search_products_window(self, window):
        label = tk.Label(window, text="Enter Product Name to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Product", command=lambda: print(f"Searching Product '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def search_suppliers_window(self, window):
        label = tk.Label(window, text="Enter Supplier Name to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Supplier", command=lambda: print(f"Searching Supplier '{entry.get()}'"))
        button.pack(pady=10, padx=10)

    def search_transport_window(self, window):
        label = tk.Label(window, text="Enter Transport Details to Search:", font=("Times New Roman", 12))
        label.pack(pady=5, padx=5)
        entry = tk.Entry(window)
        entry.pack(pady=5, padx=5)
        button = tk.Button(window, text="Search Transport", command=lambda: print(f"Searching Transport '{entry.get()}'"))
        button.pack(pady=10, padx=10)
