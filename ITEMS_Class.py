from random import randint as rnd


class Items():  # parents class
    ''' creat class of items stock & accounting (Add & Remove & Update & cost Sales & Profit)  '''

    def __init__(self):
        print(f"\n*** items stock & accounting programm is starting ***".upper())
        self.All_Users = {}
        self.All_items = {}
        # ___________________________________________________________
        while True:
            ''' infinty loop for users log in & creat user & exit'''
            # try:
            user_login = input(
                '\n1-SIGHN UP\t\t(key - "1")\n2-SIGHN IN\t\t(key - "2")\n3-USER UPDATE\t\t(key - "3")\n4-EXIT\t\t\t(key - "E")\n\nEnter Choise  : ')  # optins for user input
            if user_login == "1":
                self.Sighn_Up()
                print("#####"*10)
            # ________________________________________________________________________
            elif user_login == "2":
                self.class_name = input(
                    "\n** please enter your item name to run program ** :".title())
                print(
                    f"\n*** welcom to {self.class_name} programm \n***".title())
                print(f"all users is {list(self.All_Users.keys())}")
                self.Sighn_In()
                print("#####"*10)
            # ________________________________________________________________________
            elif user_login == "3":
                self.update_user()
                print("#####"*10)
            # ________________________________________________________________________
            elif user_login.lower() == "e":  # fun for exit program
                print("*****"*5)
                print(f"exit {self.class_name} programm".upper())
                print("#####"*10)
                break
                # ________________________________________________________________________
            else:
                print("*****"*5)  # wrong enter modify
                print("** please select on of choise '1','2','3','E' **".title())
                print("#####"*10)
            # except:
            #     print("*****"*5)  # wrong enter modify
            #     print("** please select on of choise '1','2','3','4' **".title())
            #     print("#####"*10)
    # ________________________________________________________________________
    # ___users settings__________________________________________________________

    def Sighn_In(self):
        '''functions for sigh_in in all users'''
        user_name = input("user name or email :".title())
        user_pass = input("pass word :".title())
        user_depart = input("user department (stock or accounting) :".title())
        print(f"\n***hello : --({user_name})-- welcome back***".title())
        while True:
            if user_name.lower() in self.All_Users.keys() and user_pass.lower() == self.All_Users.get(user_name, {}).get("user_pass"):
                if user_depart.lower() == "stock":
                    # print(# f"***hello : --({user_name})-- welcome back***".title())
                    item_modify = input(
                        '''***\nChoise Your stock Modify***\n1-Add Item\t\t(key - "A")\n2-Update Item\t\t(key - "U")\n3-Del Item\t\t(key - "D")\n4-ShowAll Items\t\t(key - "SH")\n5-Item Details\t\t(key - "ID")\n7-Exit\t\t\t(key - "E")\nEnter Choise  : ''')  # optins for user input
                    if item_modify.lower() == "a":
                        self.add_item()  # fun for adding items
                        print("#####"*10)
                    elif item_modify.lower() == "u":
                        self.update_item()  # fun for update items
                        print("#####"*10)
                    elif item_modify.lower() == "d":
                        self.delete_item()  # fun for del items
                        print("#####"*10)
                    elif item_modify.lower() == "sh":  # def for show all serail items
                        self.show_All_items()
                        print("#####"*10)
                    elif item_modify.lower() == "id":  # def for show items details
                        self.show_item_details()
                        print("#####"*10)
                    elif item_modify.lower() == "e":  # fun for exit program
                        print("*****"*5)
                        print(f"exit stock department".upper())
                        print("#####"*10)
                        break
                    else:
                        print("*****"*5)  # wrong enter modify
                        print("**please select 'a','u','d','sh','id','e'**".title())
                        print("#####"*10)
                # __________________________________________________________________
                elif user_depart.lower() == "accounting":
                    # print(
                    #     f"***hello : --({user_name})-- welcome back***".title())
                    item_modify = input(
                        '''\nChoise Your Items Modify\n\n1-ShowAll Items\t\t(key - "SH")\n2-Item Details\t\t(key - "ID")\n3-Accounting\t\t(key - "AC")\n8-Exit\t\t\t(key - "E")\nEnter Choise  : ''')  # optins for user input
                    if item_modify.lower() == "sh":  # def for show all serail items
                        self.show_All_items()
                        print("#####"*10)
                    elif item_modify.lower() == "id":  # def for show items details
                        self.show_item_details()
                        print("#####"*10)
                    elif item_modify.lower() == "ac":
                        self.item_accounting()  # fun for accounting item
                        print("#####"*10)
                    elif item_modify.lower() == "e":  # fun for exit program
                        print("*****"*5)
                        print(f"exit accounting department".upper())
                        print("#####"*10)
                        break
                    else:
                        print("*****"*5)  # wrong enter modify
                        print("**please select choise sh,id,ac,e**".title())
                        print("#####"*10)
                else:
                    print(
                        '"user_name or user_pass invalid"\n"please enter valid name & password again"'.title())
                    print("*****"*5)
                    break
            else:
                print(
                    '"user_name or user_pass invalid"\n"please enter valid name & password again"'.title())
                print("*****"*5)
                break
    # ___________________________________________________________

    def Sighn_Up(self):
        '''functions for Sighn_Up users
        input:
        # capital or small or numbers or special
        (string :user name & user password & user department)
        function: **if user name and password is correct you can sighn up**
        or **tary agian**
        '''
        user_name = input("user name or email :".title())
        user_pass = input("pass_word :".title())
        user_depart = input("user department (stock or accounting) :".title())
        if user_depart.lower() == "stock" or user_depart.lower() == 'accounting':
            self.All_Users[user_name.lower()] = {
                "user_pass": user_pass.lower(), "user_depart": user_depart.lower()}
            print(
                f"\n---hello **{user_name}** you have create new account---".title())
            # print(self.All_Users.keys())
            print("*****"*5)
            return self.All_Users
        else:
            print("please enter valid department")
            user_depart = input(
                "user department (stock or accounting) :".title())
            self.All_Users[user_name.lower()] = {
                "user_pass": user_pass.lower(), "user_depart": user_depart.lower()}
            print(f"hello welcome {user_name} please sighn in".title())
            # print(self.All_Users.keys())
            print("*****"*5)
            return self.All_Users
    # _________________________________________________________________

    def update_user(self):
        '''functions for update user from  all users'''
        print(list(self.All_Users.keys()))
        user_name = input("user name or email :".title())
        _ = input("pass word :".title())
        if user_name.lower() in self.All_Users.keys():
            del self.All_Users[user_name]
            n_user_name = input("new user name & email :".title())
            n_user_pass = input("new pass_word :".title())
            n_user_depart = input(
                "new user department (stock or accounting) :".title())
            self.All_Users[n_user_name.lower()] = {
                "user_pass": n_user_pass.lower(), "user_depart": n_user_depart.lower()}
            print(f"new user is : {n_user_name} please sighn in".title())
            print("*****"*5)
            return self.All_Users
        elif user_name.lower() not in self.All_Users.keys():
            print(
                '"user_name or user_pass invalid"\n"please enter valid name & password again"'.title())
            print("*****"*5)
    # ___________________________________________________________

    # items settings
    def add_item(self):
        '''functions for add items in all items'''
        add_items = {}
        item_name = input(f"{self.class_name} Name :")
        # make serial for item
        item_seiral = f"00{rnd(10,100)}{item_name.upper()}-{rnd(100,1000)}/022"
        # must be int
        item_cost = int((input(f"{self.class_name} Cost :")))
        # must be int
        item_sell = int((input(f"{self.class_name} Sell Price :")))
        item_stock = int(
            (input(f"{self.class_name} Stosk :")))  # must be int
        add_items[item_seiral] = {"item_name": item_name.upper(
        ), "item_cost": item_cost, "item_sell": item_sell, "item_stock": item_stock}
        print(
            f"****{self.class_name} You Have Add Is : ({item_seiral})****".title())
        print("*****"*5)
        self.All_items.update(add_items)
        print(f"** add_new {self.class_name} is finshed **".title())
    # ___________________________________________________________

    def update_item(self):
        '''functions for update item in all items'''
        print(f"all serial is {list(self.All_items.keys())}")
        item_seiral = input(f"{self.class_name} Seiral number :")
        if item_seiral in self.All_items.keys():
            del self.All_items[item_seiral]  # delet old item
            n_item_name = input(
                f"new {self.class_name} Name :")  # add new item
            # make serial for item
            n_item_seiral = f"00{rnd(10,100)}{n_item_name.upper()}-{rnd(100,1000)}/022"
            n_item_cost = int((input(f"new {self.class_name} Cost :")))
            n_item_sell = int(
                (input(f"new {self.class_name} Sell Price :")))
            n_item_inv = int((input(f"new {self.class_name} Stosk :")))
            self.All_items[n_item_seiral] = {"item_name": n_item_name.upper(
            ), "item_cost": n_item_cost, "item_sell": n_item_sell, "item_stock": n_item_inv}
            print(f"new {self.class_name} Is : {n_item_seiral}".title())
            print("*****"*5)
        elif item_seiral not in self.All_items.keys():
            print(
                f'""{self.class_name} seiral invalid"\n"please try enter valid serial try again"'.title())
            print("*****"*5)
        else:
            print(f"update {self.class_name} is finshed".title())
    # _________________________________________________________________

    def delete_item(self):
        '''functions for deleting items from  all items'''
        print(f"all serial is {list(self.All_items.keys())}")
        item_seiral = input(f"{self.class_name} Seiral number :")
        if item_seiral in self.All_items.keys():
            del self.All_items[item_seiral]
            print(f"Item : {item_seiral} is delete".title())
            print("*****"*5)
        elif item_seiral not in self.All_items.keys():
            print(
                f'"{self.class_name} seiral invalid"\n"please try enter valid serial try again"'.title())
            print("*****"*5)
        else:
            print(f"delete {self.class_name} is finshed".title())
    # ___________________________________________________________

    def show_All_items(self):
        '''functions for deleting items from  all items'''
        show_items = list(self.All_items.keys())
        print(f"all {self.class_name} is {show_items}".title())
        print(f"show of all {self.class_name} is finshed".title())
        print("*****"*5)
    # ________________________________________________________________

    def show_item_details(self):
        '''functions for deleting items from  all items'''
        print(f"all serial is {list(self.All_items.keys())}")
        item_seiral = input(f"{self.class_name} Seiral number :")
        if item_seiral in self.All_items.keys():
            show_item = list(self.All_items.get(item_seiral, {}).items())
            print(f"Item : {item_seiral} details is {show_item}".title())
            print("*****"*5)
        elif item_seiral not in self.All_items.keys():
            print(
                f'"{self.class_name} seiral invalid"\n"please try enter valid serial try again"'.title())
            print("*****"*5)
        else:
            print(f"details of {self.class_name} is finshed".title())
    # _______________________________________________________________________

    def item_accounting(self):
        '''functions for item accounting  '''
        print(f"all serial is {list(self.All_items.keys())}")
        item_seiral = input(f"{self.class_name} Seiral number :")
        global stock_item  # stock of item change in sales or purshase
        stock_item = self.All_items.get(item_seiral, {}).get("item_stock")
        while True:
            item_account = input(
                f'''***Choise  {self.class_name} accounting \n1-Stock Item\t\t(key - "S")\n2-Cost Item\t\t(key - "C")\n3-Sales Item\t\t(key - "SL")\n4-Exit\t\t\t(key - "E")***\nEnter Choise  : ''')  # optins for user input
            if item_seiral in self.All_items.keys():
                if item_account.lower() == "s":
                    # get cuurent stock of item
                    cur_stock = stock_item
                    print(
                        f"stock of {self.class_name}-({item_seiral}) = ({cur_stock} items)".title())
                    print("*****"*5)
                    print(
                        f"stock of {self.class_name} is finshed".title())
                    pass
                elif item_account.lower() == "c":
                    # get total cost of purshaing item and plus to stock of item
                    item_cost_price = self.All_items.get(
                        item_seiral, {}).get("item_cost")
                    item_buy = int(input("Enter Number Of Purshaing Items : "))
                    stock_item += item_buy
                    item_cost = item_buy*item_cost_price
                    print(
                        f"cost of Purshaing  {self.class_name}-({item_seiral}) = items ({item_buy}) * cost price ({item_cost_price}) = ({item_cost} $)".title())
                    print(
                        f"current stock of {self.class_name} is ({stock_item} items)".title())
                    print("*****"*5)
                    print(
                        f"cost of {self.class_name} is finshed".title())
                elif item_account.lower() == "sl":
                    # get total sales of selling item and decress it from stock of item
                    item_sell_price = self.All_items.get(
                        item_seiral, {}).get("item_sell")
                    sales_item = int(input("Enter Number Of Sales Items : "))
                    stock_item -= sales_item
                    item_sales = sales_item*item_sell_price
                    total_profit = (stock_item*item_sell_price) - \
                        (stock_item*item_cost_price)
                    print(
                        f"total sales of {self.class_name} - ({item_seiral}) = sales {self.class_name} ({sales_item}) * sales price ({item_sell_price}) = ({item_sales} $)".title())
                    print(
                        f"total prfit of {self.class_name} = {item_sales} - {item_cost}  = ({total_profit} $)".title())
                    print(
                        f"current stock of {self.class_name} is ({stock_item} items)".title())
                    print("*****"*5)
                    print(
                        f"sales of all {self.class_name} is finshed".title())
                # elif item_account.lower() == "p":
                #     # get total profit of item
                #     total_profit = item_sales-item_cost
                #     print(
                #         f"profit of {self.class_name} - ({item_seiral}) = total sales ({item_sales}) - total cost ({item_cost}) = ({total_profit} $)".title())
                #     print("*****"*5)
                #     print(f"profit of {self.class_name} is finshed".title())
                elif item_account.lower() == "e":  # fun for exit program
                    print("*****"*5)
                    print(f"exit {self.class_name} accounting".upper())
                    print("#####"*10)
                    break
                else:
                    print("please select choise s,c,p,e".title())
            else:
                print(
                    f'"{self.class_name} seiral invalid"\n"please try enter valid serial try again"'.title())
                print("*****"*5)
                break

help(Items)
item_1 = Items()

