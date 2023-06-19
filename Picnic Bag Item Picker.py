from tkinter import*
import random
root = Tk()
root.title("Picnic Bag Item Picker")
root.geometry("800x400")
root.configure(bg = "red")

items = Label(root, font = ("Comic Sans MS", 12, "bold"))
item_to_pick = Label(root)

items_list = ["Book", "Food", "Mat", "Basket", "Pencil", "Eraser", "Hand Sanitizer", "Napkins", "Snacks"]
items["text"] = str(items_list)

def generate():
    item_index = random.randint(0,8)
    item_to_pick["text"] = "Put " + items_list[item_index] + " In Your Bag"
    


generate_button = Button(root, font = ("Comic Sans MS", 12, "bold"), bg = "red2", command = generate, fg = "black", text = "Pick An Item")

items.place(relx = 0.5, rely = 0.25, anchor = CENTER)
item_to_pick.place(relx = 0.5, rely = 0.5, anchor = CENTER)
generate_button.place(relx = 0.5, rely = 0.75, anchor = CENTER)


root.mainloop()