import super_admin
import theatre
#from getpass import getpass
from user import *
import user
import random
import smtplib
import admin

class User_admin():
    def option(self):
        print("******************************************************")
        print("!              Press 1 for User Login                !")
        print("!              Press 2 for Sign Up                   !")
        print("******************************************************")
        cho=int(input("Enter Your choice"))
        return cho
    def login(self):
        try:
            user=input("****Enter UserName****:- ")
            pas=input( "****Enter Password****:- ")
            #pas=getpass("enter pass")
            mycur.execute("select * from admin")
            data=mycur.fetchall()
            mycur.execute("select * from users")
            udata=mycur.fetchall()
            mycur.execute("select * from theatre_staff")
            tdata=mycur.fetchall()
            for j in [data,udata,tdata]:
                for i in j:
                    
                    if i[1]==user and i[2]==pas:
                        if i[3]=="suadmin":
                            s=super_admin.Super_user()
                            s.start(i)
                        elif i[3]=="admin":
                            a=admin.Admin()
                            a.start(i)
                        elif i[3]=="user":
                            u=User()
                            u.start(i)
                        elif i[3]=="theatre":
                            t=theatre.Theater()
                            t.start_app(i)
        except Exception as e:
            print("oops something went wrong",e)
    def singup(self):
        print("******************************************************")
        user=input("****Enter UserName****:- ")
        pas=input("****Enter Password****:- ")
        name=input("****  Enter Name  ****:- ")
        email=input("**** enter email ****:- ")
        print("******************************************************")
        print("************Check your email for otp******************")
        print("******************************************************")
        value=random.randint(1000,9999)
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login("egabhigupta@gmail.com","Abhi@8120610655")
        mail.sendmail("egabhigupta@gmail.com",email,str(value))
        mail.quit()
        otp=int(input("****  Enter OTP  ****:- "))
        if otp==value:
            mycur.execute("select * from regions")
            rdata=mycur.fetchall()
            print("******************************************************")
            print("***-ID-*****-REGION NAME-*****************************")
            print("******************************************************")
            for i in rdata:
                print("    ",i[0],'      ',i[1])
            print("******************************************************")
            re=int(input("enter region id"))
            mycur.execute("insert into users(u_username,u_password,role,u_name,u_email,r_id) values('{}','{}','user','{}','{}',{} )".format(user,pas,name,email,re))
            mydb.commit()
            print("******************************************************")
            print("*********************user created*********************")
            print("******************************************************")
            
    def startapp(self):
        while True:
            
            ch=self.option()
            if ch == 1:
                self.login()
            elif ch == 2:
                self.singup()

u=User_admin()          
u.startapp()
