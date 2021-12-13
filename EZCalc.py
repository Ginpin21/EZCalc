import Classes as cl
import pandas as pd
#===============================================================================================================================================
def next():
    input("\n Press any buttion to continue....")
#===============================================================================================================================================
def new_user(u_type):  
    if u_type=="Student":
        s1=cl.student("","")
        s1.new()
        dup_check=find_user(s1.username)
        while dup_check < 0:
            new_name=input("The username "+s1.username+" is already taken please enter a new username: ")
            s1.username=new_name
            dup_check=find_user(new_name)     
        l1=[s1.username,s1.password,u_type]
        df=pd.DataFrame([l1])
        df.to_csv("Users.csv",mode="a",header=0,index=0) 
    elif u_type=="Teacher":
        t1=cl.teacher("","")
        t1.new()
        dup_check=find_user(t1.username)
        while dup_check < 0:
            new_name=input("The username "+t1.username+" is already taken please enter a new username: ")
            t1.username=new_name
            dup_check=find_user(new_name)  
        l1=[t1.username,t1.password,u_type]
        df=pd.DataFrame([l1])
        df.to_csv("Users.csv",mode="a",header=0,index=0)
    print("New",u_type,"added")
    next()

#===============================================================================================================================================
def change_pass(u_name):
    search=find_user(u_name)
    col_names=["Username","Password","Type"]
    df=pd.DataFrame() 
    df=pd.read_csv("Users.csv",names=col_names,index_col="Username")
    if search==-1:
        pass1=input("Enter your current password: ")
        for i in df.itertuples():
            if pass1==i[1]:
                new_pass=input("Enter the new password: ")
                df.at[u_name,"Password"]=new_pass
                df.to_csv("Users.csv",header=False,columns=None)
                print("Password successfully changed for the user",u_name)
                next()
                break
        else:
            print("Invalid Password")
            next()
    else:
        print("Username does not exist")


#===============================================================================================================================================
def enable(func_name):
    df2=pd.read_csv("Functions.csv",names=["Function","Enabled"],index_col="Function")
    for i in df2.itertuples():
        if i[0]==func_name and i[1]==False:
            df2.at[func_name,"Enabled"]=True
            df2.to_csv("Functions.csv",header=False,columns=None)
            print(func_name,"function enabled")
            break
        elif i[0]==func_name and i[1]==True:
            print("The function is already enabled")
            break
    else:
        print("The function does not exist")
    next() 
#===============================================================================================================================================
def disable(func_name):
    df2=pd.read_csv("Functions.csv",names=["Function","Enabled"],index_col="Function")
    for i in df2.itertuples():
        if i[0]==func_name and i[1]==True:
            df2.at[func_name,"Enabled"]=False
            df2.to_csv("Functions.csv",header=False,columns=None)
            print(func_name,"function disabled")
            break
        elif i[0]==func_name and i[1]==False:
            print("The function is already disabled")
            break
    else:
        print("The function does not exist")
    next() 
#===============================================================================================================================================
def find_user(u_name):
    try:
        col_names=["Username","Password","Type"]
        df=pd.DataFrame() 
        df=pd.read_csv("Users.csv",names=col_names,index_col="Username")
        for i in df.itertuples():
            if u_name==i[0]:
                return -1
                break
        else:
            return  1  
    except FileNotFoundError:
        return 0


#===============================================================================================================================================
def student_menu(u_name):
    name1=u_name
    while True:
        print("""
=========================================================================
        Welcome to Student's Menu
=========================================================================
        1.Arithmetic Functions
        2.Factorial Function
        3.Trigonometric Functions
        4.Decimal to binary
        5.Area Functions
        6.Change Password
        7.Back to menu
=========================================================================
        """)
        try:
            ch=int(input("Enter your choice: "))
            if ch==1:
                pass
            elif ch==2:
                pass        
            elif ch==3:
                pass
            elif ch==4:
                pass
            elif ch==5:
                pass
            elif ch==6:
                change_pass(name1)
            elif ch==7:
                break
            else:
                print("Invalid choice")
                next()
        except ValueError:
            print("Please enter an integer")
            next()
#===============================================================================================================================================
def teacher_menu(u_name):
    name1=u_name
    while True:
        print("""
=========================================================================
        Welcome to Teacher's Menu
=========================================================================
        1.View student usernames
        2.Enable function
        3.Disable function
        4.Check all functions status
        5.Change Password
        6.Back to menu
=========================================================================
        """)
        try:
            ch=int(input("Enter your choice: "))
            if ch==1:
                col_names=["Username","Password","Type"]
                df=pd.DataFrame() 
                df=pd.read_csv("Users.csv",names=col_names,index_col="Username")
                df.sort_values("Type",inplace=True)
                print(df[df["Type"]=="Student"])
                next()
            elif ch==2:
                a=input("Enter the function name: ")
                enable(a)
            elif ch==3:
                a=input("Enter the function name: ")
                disable(a)
            elif ch==4:
                df2=pd.read_csv("Functions.csv",names=["Function","Enabled"],index_col="Function")
                print(df2)
                next()
            elif ch==5:
                change_pass(name1)
            elif ch==6:
                next()
                break
            else:
                print("Invalid choice")
        except ValueError:
                print("Please enter an integer")
                next()        
#===============================================================================================================================================
def admin_menu():
    while True:
        print("""
=========================================================================
        Welcome to Admin Menu
=========================================================================
        1.Add new student
        2.Add new teacher
        3.View all users info
        4.Back to menu
=========================================================================""")
        try:
            ch=int(input("Enter your choice: "))
            if ch==1:
                new_user("Student")
            elif ch==2:
                new_user("Teacher")
            elif ch==3:
                col_names=["Username","Password","Type"]
                df=pd.DataFrame()
                df=pd.read_csv("Users.csv",index_col="Username",names=col_names)
                print(df)
                next()
            elif ch==4:
                next()
                break
            else:
                print("Invalid choice")
                next()
        except ValueError:
            print("Please enter an integer")
            next()

#===============================================================================================================================================
def main_menu():
    while True:
        print("""
=========================================================================
        Welcome to EZCalc
=========================================================================
        1.Login as Student
        2.Login as Teacher
        3.Login as Admin
        4.Exit
=========================================================================""")
        try:
            ch=int(input("Enter your choice: "))
            if ch==1:
                name1=str(input("Enter the username: "))
                pass1=str(input("Enter the password: "))
                col_names=["Username","Password","Type"]
                df=pd.DataFrame()
                df=pd.read_csv("Users.csv",index_col="Username",names=col_names)
                df.sort_values("Type",inplace=True)
                for i in df.itertuples():
                    if name1==i[0] and pass1==i[1]:             
                        student_menu(name1)
                        break
                else:
                    print("Invalid username or password")
                    next()
            elif ch==2:
                name1=str(input("Enter the username: "))
                pass1=str(input("Enter the password: "))
                col_names=["Username","Password","Type"]
                df=pd.DataFrame()
                df=pd.read_csv("Users.csv",index_col="Username",names=col_names)
                df.sort_values("Type",inplace=True)
                for i in df.itertuples():
                    if name1==i[0] and pass1==i[1]:             
                        teacher_menu(name1)
                        break
                else:
                    print("Invalid username or password")
                    next()
            elif ch==3:
                name1=str(input("Enter the username: "))
                pass1=str(input("Enter the password: "))
                if name1=="admin" and pass1=="admin123":
                    admin_menu()
                else:
                    print("Invalid username or password")
                    next()
            elif ch==4:
                SystemExit()
                break
            else:
                print("\nInvalid Choice")
                next()
        except ValueError:
            print("Please enter an integer")
            next()
#===============================================================================================================================================
main_menu()