import pymysql
from user import *

class Super_user():
    def options(self):
        print("******************************************************")
        print("!             Press 1 for Add Admin                  !")
        print("!             press 2 for Delete Admin               !")
        print("!             press 3 for Admin list                 !")
        print("!             press 4 for add region                 !")
        print("!             press 5 for region list                !")
        print("!             press 6 for add city                   !")
        print("!             press 7 for city list                  !")
        print("!             press 8 for Logout                     !")
        print("******************************************************")
        try:
            ch=int(input("***enter your choice***:- "))
            return ch
        except Exception as e:
            print("oops something went wrong",e)
            return 0
    def start(self,i):
        
        while True:
            
            ch=self.options()
            if ch==1:
                try:
                    self.add_admin()
                except Exception as s:
                    print("somthing went wrong",s)
            elif ch==2:
                try:
                    self.delete_admin()
                except Exception as s:
                    print("somthing went wrong",s)
            elif ch==3:
                try:
                    self.admin_list()
                except Exception as s:
                    print("somthing went wrong",s)
            elif ch==4:
                try:
                    self.add_region()
                except Exception as s:
                    print("somthing went wrong",s)
            elif ch==5:
                try:
                    self.region_list()
                except Exception as s:
                    print("somthing went wrong",s)
            elif ch==6:
                try:
                    name=input("enter city name")
                    self.region_list()
                    rid=int(input("enter region id"))
                    mycur.execute("insert into cities(c_name,re_id) values('{}',{})".format(name,rid))
                    mydb.commit()
                    print("data inserted")
                except Exception as s:
                    print("somthing went wrong",s)
                    
            elif ch==7:
                mycur.execute("select * from cities")
                f=mycur.fetchall()
                for i in f:
                    print(i)
            elif ch==8:
                break

            else:
                print("wrong choice")

                
    def add_admin(self):
        try:
            print("******************************************************")
            print("*******************Add Region Admin*******************")
            print("******************************************************")
            
            name=input("***Enter admin name***:- ")
            user=input("***Enter user name***:- ")
            pas=input("***Enter password***:- ")
            email=input("***Enter email***:- ")
            mycur.execute("select * from regions")
            rdata=mycur.fetchall()
            print("id*****name*******************************************")
            for i in rdata:
                print(i[0],i[1])
            region=int(input("enter region id"))
            mycur.execute("insert into admin (su_username,su_password,role,su_name,su_email,reg_id) values('{}','{}','admin','{}','{}',{})".format(user,pas,name,email,region))
            mydb.commit()
            print("******************************************************")
            print("**********************Data Inserted*******************")
            print("******************************************************")
        except Exception as e:
            print(e)
    def delete_admin(self):
        print("******************************************************")
        print("********************Delete Admin**********************")
        print("******************************************************")
        user=input("***Enter User Name***:- ")
        con=input("Do you really want to delete this user ....? y/n")
        if con=='y':
            mycur.execute("select * from admin")
            for i in mycur.fetchall():
                if i[1]==user:
                    mycur.execute("delete from admin where su_username='{}'".format(user))
                    mydb.commit()
            print("******************************************************")
            print("********************User Deleted**********************")
            print("******************************************************")
                    
                
        else:
            print("******************************************************")
            print("****************Invalid User Name*********************")
            print("******************************************************")
        
    def admin_list(self):
        print("******************************************************")
        print("***********************Admin List*********************")
        print("******************************************************")
        mycur.execute('select * from admin')
        adata=mycur.fetchall()
        print("******************************************************")
        for i in adata:
            print("id=",i[0],'username=',i[1],'password=',i[2],'role=',i[3],'name=',i[4],'email=',i[5],'region',i[6])
        print("******************************************************")
    def add_region(self):
        print("******************************************************")
        print("************************Add Region********************")
        print("******************************************************")
        rname=input("enter region name")
        mycur.execute("insert into regions(r_name) values ('{}')".format(rname))
        mydb.commit()
        print("******************************************************")
        print("********************Data Inserted*********************")
        print("******************************************************")
        
    def region_list(self):
        print("******************************************************")
        print("**********************Region List*********************")
        print("******************************************************")
        mycur.execute("select * from regions")
        rdata=mycur.fetchall()
        print("******************************************************")
        for i in rdata:
            print("id",i[0],"name",i[1])

        print("******************************************************")
            
    
