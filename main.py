import tkinter as tk
from Layouts.mainLayout import InventoryLayout

# Create the main application window
root = tk.Tk()
root.iconbitmap(r"C:\Users\chakr\PycharmProjects\MkInventory\.venv\Asserts\FeviconManaKirana.ico")
root.title("ManaKirana Inventory Management")

# Initialize the layout
inventory_layout = InventoryLayout(root)

# Create sections and widgets
inventory_layout.create_section(inventory_layout.product_frame, "Product")
# inventory_layout.create_section(inventory_layout.package_frame, "Package")
inventory_layout.create_section(inventory_layout.order_frame, "Order")
# inventory_layout.create_section(inventory_layout.delivery_frame, "Delivery")
inventory_layout.create_section(inventory_layout.catalouge_frame, "Catalouge")

# Add widgets to the frames of product
inventory_layout.add_widget(inventory_layout.product_frame, "Search Product Stock", (1, 0), "button", inventory_layout.button_click_handler_product)
inventory_layout.add_widget(inventory_layout.product_frame, "Add Product To Stock", (2, 0), "button", inventory_layout.button_click_handler_add_product)
inventory_layout.add_widget(inventory_layout.product_frame, "Modify Product Stock", (3, 0), "button", inventory_layout.button_click_handler_modify_product)
# inventory_layout.add_widget(inventory_layout.product_frame, "Stock Report", (4, 1), "button")
inventory_layout.add_widget(inventory_layout.product_frame, "Add Product/Image/Financial To business", (5, 0), "button",inventory_layout.button_click_handler_add_productMongoDB)
inventory_layout.add_widget(inventory_layout.product_frame, "Search/Update/Delete Product in business", (8, 0), "button", inventory_layout.button_click_handler_modify_productMongoDB)
# inventory_layout.add_widget(inventory_layout.product_frame, "Business Report", (10, 1), "button")
# Add widgets to the frames of package
# inventory_layout.add_widget(inventory_layout.package_frame, "Search Package", (1, 0), "button")
# inventory_layout.add_widget(inventory_layout.package_frame, "Add Package", (2, 0), "button")
# inventory_layout.add_widget(inventory_layout.package_frame, "Modify Package", (3, 0), "button")
# inventory_layout.add_widget(inventory_layout.package_frame, "Report", (4, 0), "button")

# Add widgets to the frames of Order
inventory_layout.add_widget(inventory_layout.order_frame, "Search Order", (1, 0), "button",inventory_layout.button_click_handler_search_orderMongoDB)
inventory_layout.add_widget(inventory_layout.order_frame, "Add Order", (2, 0), "button",inventory_layout.button_click_handler_add_orderMongoDB)
# inventory_layout.add_widget(inventory_layout.order_frame, "Modify Order", (3, 0), "button")
# inventory_layout.add_widget(inventory_layout.order_frame, "Report", (4, 0), "button")

# Add widgets to the frames of Delivery
# inventory_layout.add_widget(inventory_layout.delivery_frame, "Search Delivery", (1, 0), "button")
# inventory_layout.add_widget(inventory_layout.delivery_frame, "Add Delivery", (2, 0), "button")
# inventory_layout.add_widget(inventory_layout.delivery_frame, "Modify Delivery", (3, 0), "button")
# inventory_layout.add_widget(inventory_layout.delivery_frame, "Report", (4, 0), "button")

# Run the Tkinter event loop
# Create sections and widgets
# Add widgets to the frames of catlogs
# label = tk.Label(root, text="this is my first tkinter")
# label.pack(pady=20, padx=20)
# inventory_layout.add_widget(inventory_layout.catalouge_frame, label_text="Object", grid_config=(1, 0), widget_type="label")
inventory_layout.add_widget(inventory_layout.catalouge_frame, label_text="Object Dropdown", grid_config=(1, 0), widget_type="label")
object = ["Brands", "Category", "Location", "Products", "Suppliers", "Transport"]
inventory_layout.add_widget(inventory_layout.catalouge_frame, label_text="Object Dropdown", grid_config=(1, 1), widget_type="combobox", combobox_values=object)

inventory_layout.add_widget(inventory_layout.catalouge_frame, label_text="Operations Dropdown", grid_config=(2, 0), widget_type="label")
operations = ["create", "search", "update", "delete"]
inventory_layout.add_widget(inventory_layout.catalouge_frame, label_text="Operations Dropdown", grid_config=(2, 1), widget_type="combobox", combobox_values=operations)

inventory_layout.add_widget(inventory_layout.catalouge_frame, "Proceed", (3, 0), "button", inventory_layout.button_click_handler_catelogue)


root.mainloop()
