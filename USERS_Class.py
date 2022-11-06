# class of USERS for immplement in any system of company
class Users(): # parents class
      def __init__(self):
            ''' creat class of users (sighn in & sighn up)'''
            self.All_Users = {"abdo.elsharef": {"user_pass": "abdo123456789", "user_depart": "admin"}}
      #_____________________________________________________________
      def Sighn_In(self):
            '''functions for sigh_in in all users'''
            user_name = input("user name & email :".title())
            user_pass = input("pass name :".title())
            if user_name.lower() in self.All_Users.keys() and user_pass.lower() == self.All_Users.get(user_name, {}).get("user_pass"):
                  print(f"hello : ({user_name}) welcome back".title())
                  print("*****"*5)
                  return user_name, user_pass
            elif user_name.lower() not in self.All_Users.keys() or user_pass.lower() == self.All_Users.get(user_name, {}).get("user_pass"):
                  print('"user_nam or user_pass invalid"\n"please try enter valid name or password again"'.title())
                  print("*****"*5)
      # ___________________________________________________________
      def Sighn_Up(self):
            '''functions for Sighn_Up user in all users'''
            user_name = input("user name & email :".title())
            user_pass = input("pass_word :".title())
            user_depart = input("user department :".title())
            self.All_Users[user_name.lower()] = {"user_pass": user_pass.lower(), "user_depart": user_depart.lower()}
            print(f"hello welcome {user_name} please sighn in".title())
            print(self.All_Users.keys())
            print("*****"*5)
            return self.All_Users
      #_________________________________________________________________
      def update_user(self):
            '''functions for update user from  all users'''
            print(list(self.All_Users.keys()))
            user_name = input("user name & email :".title())
            if user_name.lower() in self.All_Users.keys():
                  del self.All_Users[user_name]
                  n_user_name = input("new user name & email :".title())
                  n_user_pass = input("new pass_word :".title())
                  n_user_depart = input("new user department :".title())
                  self.All_Users[n_user_name.lower()] = {"user_pass": n_user_pass.lower(), "user_depart": n_user_depart.lower()}
                  print(f"new user is : {n_user_name} please sighn in".title())
                  print("*****"*5)
                  return self.All_Users
            elif user_name.lower()  not in self.All_Users.keys():
                  print('"user_nam or user_pass invalid"\n"please try enter valid name or password again"'.title())
                  print("*****"*5)
      # ___________________________________________________________
      # new workkkkkkkkkkkkkkkkkkkkkkkkkkkkk



