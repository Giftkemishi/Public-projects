import sqlite3
conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS inventory 
                   (name TEXT PRIMARY KEY, description TEXT, quantity INT, price REAL)''')
    conn.commit()
except sqlite3.Error as e:
    print(f"Error: {e}")




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()

root.title("Inventory Management System")
root.geometry("700x600")

head = tk.Label(root, text="Product Management", font=("Arial", 30), bg="mistyrose")
head.pack(padx="0", pady="25")

root.configure(bg="mistyrose")

name_label = tk.Label(root, text="Name:", bg="mistyrose")
name_label.pack()
name = tk.Entry(root, width=70)
name.pack(pady=15)

description_label = tk.Label(root, text="Description:", bg="mistyrose")
description_label.pack()
description = tk.Entry(root, width=70)
description.pack(pady=15)

quantity_label = tk.Label(root, text="Quantity:", bg="mistyrose")
quantity_label.pack()
quantity = tk.Entry(root, width=70)
quantity.pack(pady=15)

price_label = tk.Label(root, text="Price:", bg="mistyrose")
price_label.pack()
price = tk.Entry(root, width=70)
price.pack(pady=15)

Buttons_frame = tk.Frame(root, bg="mistyrose")
Buttons_frame.pack(padx=10, pady=10)


def Add_product():
    product_name = name.get()
    product_description = description.get()
    product_quantity = quantity.get()
    product_price = price.get()

    if not all([product_name, product_description, product_quantity, product_price]):
        messagebox.showerror("Error", "Please fill all product details")
        return

    try:
        # Database insertion
        cur.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)",
                    (product_name, product_description, int(product_quantity), float(product_price)))
        conn.commit()
    

        name.delete(0, tk.END)
        description.delete(0, tk.END)
        quantity.delete(0, tk.END)
        price.delete(0, tk.END)

        text_box.insert(tk.END, f"Product Name: {product_name}\n")
        text_box.insert(tk.END, f"Product Description: {product_description}\n")
        text_box.insert(tk.END, f"Product Quantity: {product_quantity}\n")
        text_box.insert(tk.END, f"Product Price: {product_price}\n\n")

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Product already exists")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")


Add_Button = tk.Button(Buttons_frame, text="Add", bg="aqua", width=15, height=2, command=Add_product)
Add_Button.pack(side=tk.LEFT, padx=5)


def Update_product():
    product_name = name.get()
    product_description = description.get()
    product_quantity = quantity.get()
    product_price = price.get()

    if not all ([product_name, product_description, product_quantity, product_price]):
        messagebox.showerror("Error", "Please fill all product details")
        return
    
    name.delete(0, tk.END)
    description.delete(0, tk.END)
    quantity.delete(0, tk.END)
    price.delete(0, tk.END)

    text = text_box.get(1.0, tk.END)
        
            # Get the text box content
    text = text_box.get(1.0, tk.END)
        
            # Split the content into product blocks
    product_blocks = text.split("\n\n")
        
            # Find and update the product block with the matching name
    updated_blocks = []
    product_found = False
    for block in product_blocks:
        lines = block.splitlines()
        if lines[0].split(": ")[0] == "Product Name" and lines[0].split(": ")[1] == product_name:
                    # Update product details
            updated_block = (
                        f"Product Name: {product_name}\n"
                        f"Product Description: {product_description}\n"
                        f"Product Quantity: {product_quantity}\n"
                        f"Product Price: {product_price}\n"
                    )
        updated_blocks.append(updated_block)
        product_found = True
    else:
        updated_blocks.append(block)
        
            # Clear the text box
        text_box.delete(1.0, tk.END)
        
            #updated blocks back into the text box
    for block in updated_blocks:
        text_box.insert(tk.END, block + "\n\n")
        
            # Display update message
    if product_found:
        text_box.insert(tk.END, f"Product '{product_name}' updated successfully.\n")
    else:
        text_box.insert(tk.END, f"Product '{product_name}' not found.\n")
    
Update_Button = tk.Button(Buttons_frame, text="Update", bg="aqua", width=15, height=2, command=Update_product)
Update_Button.pack(side=tk.LEFT, padx=5)


def Delete_product():
    product_name = name.get()
    product_description = description.get()
    product_quantity = quantity.get()
    product_price = price.get()

    if not all([product_name, product_description, product_quantity, product_price]):
        messagebox.showerror("Error", "Please fill all product details")
        return

    # Get the text box content
    text = text_box.get(1.0, tk.END)

    # Split the content into product blocks
    product_blocks = text.split("\n\n")

    # Find and remove the product block with the matching name
    for block in product_blocks:
        if block.startswith(f"Product Name: {product_name}"):
            text_box.delete(1.0, tk.END)
            for b in product_blocks:
                if b != block:
                    text_box.insert(tk.END, b + "\n\n")
            break

    # Clear entry fields
    name.delete(0, tk.END)
    description.delete(0, tk.END)
    quantity.delete(0, tk.END)
    price.delete(0, tk.END)

Delete_Button = tk.Button(Buttons_frame, text="Delete", bg="aqua", width=15, height=2, command=Delete_product)
Delete_Button.pack(side=tk.LEFT, padx=5)


Output_frame = tk.Frame(root)
Output_frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(Output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(Output_frame, width=80, height=15, yscrollcommand=scrollbar.set, bg="seashell")
text_box.pack()

scrollbar.config(command=text_box.yview)


# Create a combobox for sorting options
sorting_options = ["Sort by:", "Name (A-Z)", "Name (Z-A)", "Price (Low-High)", "Price (High-Low)", "Quantity (Low-High)", "Quantity (High-Low)"]
sorting_combobox = ttk.Combobox(root, values=sorting_options)
sorting_combobox.current(0)  # Set default value
sorting_combobox.pack()

def sort_products():
    selected_option = sorting_combobox.get()
    text = text_box.get(1.0, tk.END)
    product_blocks = text.split("\n\n")

    if selected_option == "Name (A-Z)":
        product_blocks.sort(key=lambda x: x.splitlines()[0].split(": ")[1])
# =============================================================================
#    elif selected_option == "Name (Z-A)":
#         product_blocks.sort(key=lambda x: x.splitlines()[0].split(": ")[1], reverse=True)
#    elif selected_option == "Price (Low-High)":
#         product_blocks.sort(key=lambda x: float(x.splitlines()[3].split(": ")[1]))
#    elif selected_option == "Price (High-Low)":
#         product_blocks.sort(key=lambda x: float(x.splitlines()[3].split(": ")[1]), reverse=True)
#    elif selected_option == "Quantity (Low-High)":
#         product_blocks.sort(key=lambda x: int(x.splitlines()[2].split(": ")[1]))
#    elif selected_option == "Quantity (High-Low)":
#         product_blocks.sort(key=lambda x: int(x.splitlines()[2].split(": ")[1]), reverse=True)
# =============================================================================

    text_box.delete(1.0, tk.END)
    for block in product_blocks:
        text_box.insert(tk.END, block + "\n\n")

# Create a button to trigger sorting
sort_button = tk.Button(root, text="Sort", width=10, command=sort_products)
sort_button.pack()



status_bar = tk.Label(root, text="Total Products: 0", relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(fill=tk.X, side=tk.BOTTOM)

def update_product_count():
    text = text_box.get(1.0, tk.END)
    product_count = text.count("Product Name:")
    status_bar.config(text=f"Total Products: {product_count}")

Check_State = tk.IntVar()

def close():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
conn.close()

#if __name__ == '__main__':
    
