class student:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def new(self):
        name1=str(input("Enter the username: "))
        password1=str(input("Enter the password: "))
        l=len(password1)
        while l<8:
            password1=str(input("Password should be longer than 5 characters, enter a new password: "))
            l=len(password1)

        self.username=name1
        self.password=password1


class teacher:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def new(self):
        name1=str(input("Enter the username: "))
        password1=str(input("Enter the password: "))
        l=len(password1)
        while l<8:
            password1=str(input("Password should be longer than 5 characters, enter a new password: "))
            l=len(password1)
        self.username=name1
        self.password=password1

class admin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def new(self):
        name1=str(input("Enter the username: "))
        password1=str(input("Enter the password: "))
        l=len(password1)
        while l<5:
            password1=str(input("Password should be longer than 5 characters, enter a new password: "))
            l=len(password1)        
        self.username=name1
        self.password=password1