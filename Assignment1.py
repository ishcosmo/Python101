import matplotlib.pyplot as plt
from datetime import datetime as d
import tabulate as t
import sys

n = "Grocery Store Billing System".center(168, " ")
a = "WELCOME TO ABC GROCERY STORE".center(168, "=")
print(n)
print(a)

class Store:
    def __init__(self):
        self.sections = {
            "Fruits": {"Mango": 110, "Banana": 50, "Apple": 60, "Orange": 40, "Grapes": 50, "Guava": 60, "Papaya": 50,
                       "Pineapple": 60, "Watermelon": 50, "Pomegranate": 70, "Kiwi": 80, "Lychee": 80, "Strawberry": 120,
                       "Muskmelon": 70, "Cantaloupe": 40, "Sapota (Chikoo)": 90, "Custard apple (Sitaphal)": 80, "Jackfruit": 40,
                       "Avocado": 130,
                       "Dragonfruit": 190, "Blueberries": 70, "Raspberries": 90, "Peach": 70, "Pear": 40,
                       "Amla (Gooseberry)": 50, "Passion fruit": 80, "Jamun (Indian blackberry)": 70,
                       "Indian Gooseberry (Amla)": 90, "Wood Apple (Bael)": 50},
            "Vegetables": {"Potato": 40, "Tomato": 40, "Onion": 40, "Garlic": 40, "Ginger": 40, "Spinach": 35,
                           "Okra": 55, "Eggplant": 40, "Cauliflower": 30, "Cabbage": 30, "Green peas": 40, "Bitter gourd": 30,
                           "Ridge gourd": 40, "Bottle gourd": 40, "Snake gourd": 40, "Brinjal": 30, "Carrot": 35, "Beetroot": 30,
                           "Radish": 35,
                           "Turnip": 35, "Cucumber": 35, "Lettuce": 30, "Green beans": 30, "Cluster beans": 45, "Fenugreek leaves": 30,
                           "Coriander leaves": 35, "Curry leaves": 25, "Mint leaves": 25, "Green chili": 25, "Red chili": 35,
                           "Bell pepper": 40,
                           "Sweet potato": 25, "Pumpkin": 35, "Drumstick": 35, "Indian beans": 30, "Sweet corn": 30},
            "Rice and grains": {"rice": 60, "wheat": 40, "barley": 40, "quinoa": 60, "oats": 40, "corn": 35, "millet": 35},
            "Dals": {"lentils": 350, "chickpeas": 230, "black beans": 450, "kidney beans": 340, "split peas": 300,
                     "mung beans": 45, "black-eyed peas": 60, "adzuki beans": 45, "pinto beans": 45, "navy beans": 50,
                     "soybeans": 45},
            "Dairy": {"ghee": 650, "paneer": 30, "curd": 39, "lassi": 40, "buttermilk": 45},
            "Cookware": {"pressure cooker": 500, "tawa": 250, "kadai": 500, "idli steamer": 700, "pressure pan": 450,
                         "handi": 350, "appam pan": 300, "dhokla stand": 390, "puri press": 340},
            "Snacks and sweets": {"samosa": 35, "pakora": 35, "bhajiya": 40, "dhokla": 20, "vada": 20, "poha": 30, "chaat": 35,
                                  "samosa chaat": 35, "jalebi": 30, "gulab jamun": 30, "barfi": 50, "laddu": 20, "halwa": 40,
                                  "kachori": 33}
        }
        self.items = []
        self.total_bill = 0

    def menu(self):
        print("Menu:")
        print("1. Display Grocery Sections")
        print("2. Add Items to Cart")
        print("3. Display Bill")
        print("4. Exit")

    def display_sections(self):
        print("Grocery Sections".center(168, "="))
        for index, section in enumerate(self.sections.keys(), start=1):
            print(f"{index}. {section}")

    def add(self):
        self.display_sections()
        section_choice = int(input("Enter the section number to explore (0 to exit): "))
        if section_choice == 0:
            return
        elif section_choice > 0 and section_choice <= len(self.sections):
            section_name = list(self.sections.keys())[section_choice - 1]
            print(f"{section_name} Section".center(168, "="))
            for index, (item_name, price) in enumerate(self.sections[section_name].items(), start=1):
                print(f"{index}. {item_name}: ₹{price}")
            item_index = int(input("Enter the item number to add to cart (0 to go back): "))
            if item_index == 0:
                return
            elif item_index > 0 and item_index <= len(self.sections[section_name]):
                quantity = int(input("Enter the quantity: "))
                item_name = list(self.sections[section_name].keys())[item_index - 1]
                item_price = self.sections[section_name][item_name]
                self.items.append((section_name, item_index - 1, quantity))
                print(f"{item_name} (₹{item_price}) added to cart.")
            else:
                print("Invalid item number.")
        else:
            print("Invalid section number.")

    def display_bill(self):
        r = []
        total = 0
        head = ["Item", "Quantity", "Amount"]

        for index, v in enumerate(self.items):
            amount = (list(self.sections[v[0]].values())[v[1]]) * v[2]
            total += amount
            item = list(self.sections[v[0]].keys())[v[1]]
            quantity = v[2]
            o = [item, quantity, amount]
            r.append(o)
        customer_name = input("Kindly Enter your Name: ")
        D = d.now()
        print("Name:", customer_name)
        print(D, "\n")
        r.append(["TOTAL", "", total])
        print(t.tabulate(r, headers=head, tablefmt="simple"))
        print("Thanks for shopping! Please visit again later.")
        self.visualize_bill()
        sys.exit()

    def visualize_bill(self):
        item_names = [item[0] for item in self.items]
        item_amounts = [self.sections[item[0]][list(self.sections[item[0]].keys())[item[1]]] * item[2] for item in self.items]

        plt.figure(figsize=(10,4 ))
        plt.grid(color="green",ls="dashed")
        plt.bar(item_names, item_amounts, color='red')
        plt.xlabel('Items')
        plt.ylabel('Amount')
        plt.title('Bill Visualisation')


        plt.show()


    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_sections()
            elif choice == "2":
                self.add()
            elif choice == "3":
                self.display_bill()
            elif choice == "4":
                print("Thank you for shopping with us!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a valid option.")

grocery_store = Store()
grocery_store.run()
