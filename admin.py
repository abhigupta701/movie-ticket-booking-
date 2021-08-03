import super_admin
from user import *


class Admin():

    def start(self,reg):
        self.reg=reg
        
        while True:
            print("******************************************************")
            print("     welcome to region_admin panal",reg[4])
            print("******************************************************")
            cho=self.option()
            if cho==1:
                print("******************************************************")
                print("*******************Add Theater************************")
                print("******************************************************")
                tname=input("****Enter Theater Name****:- ")
                uname=input("****  Enter UserName  ****:- ")
                pas=input("Enter Password for theatre user ")
                email=input("**** Enter Your Email ****:- ")
                mycur.execute("select * from cities where re_id={}".format(reg[-1]))
                cdata=mycur.fetchall()
                print("******************************************************")
                for i in cdata:
                    print("id ",i[0],"name",i[1])
                print("******************************************************")
                try:
                    city=int(input("enter city id"))
                    mycur.execute("insert into theatre_staff (ts_username,ts_password,role,ts_name,ts_email,suid,cityid) values ('{}','{}','theatre','{}','{}',1,{})".format(uname,pas,tname,email,city))
                    mydb.commit()
                    mycur.execute("select ts_id from theatre_staff where ts_username='{}' and ts_name='{}'".format(uname,tname))
                    the=mycur.fetchone()[0]
                    
                    capa=int(input("enter capacity"))
                    
                    mycur.execute("insert into theatre_list (tl_name,cityid,tid,capacity) values ('{}',{},{},{})".format(tname,city,the,capa))
                    mydb.commit()
                    mul=input("is it multiplex y/n")
                    if mul=='y':
                        
                        mycur.execute("select tl_id from theatre_list where tl_name='{}'".format(tname))
                        t=mycur.fetchone()
    
                        
                        while True:
                            sn=int(input("enter screen number"))
                            mycur.execute("insert into screen (s_number,capacity,t_id) values ({},{},{})".format(sn,capa,t[0]))
                            mydb.commit()
                            mycur.execute("select s_id from screen")
                            sn1=mycur.fetchall()
                            
                            mycur.execute("select tl_id from theatre_list where tl_name='{}' and tid={}".format(tname,the))
                            f=mycur.fetchone()
                            
                            pri=int(input("enter ticket price"))
                            mycur.execute("insert into theatre_time(tlid,s_id,times,cost) values({},{},030000,{})".format(f[0],sn1[-1][0],pri))
                            mydb.commit()
                            mycur.execute("insert into theatre_time(tlid,s_id,times,cost) values({},{},060000,{})".format(f[0],sn1[-1][0],pri))
                            mydb.commit()
                            mycur.execute("insert into theatre_time(tlid,s_id,times,cost) values({},{},090000,{})".format(f[0],sn1[-1][0],pri))
                            mydb.commit()
                            print("******************************************************")
                            c=input("do you wanna add more sereen ? y/n")
                            if c=='n':
                                print("******************************************************")
                                break
                   
                    print("data inserted")
                except Exception as e:
                    print("invalid choice",e)
            elif cho==2:
                print("******************************************************")
                print("*********************Add Movie************************")
                print("******************************************************")
                mname=input("***enter movie name***:- ")
                details=input("**enter details of movie**:- ")
                du=int(input("enter movie duration in minutes ex= for 3h enter 180:- "))
                mycur.execute("insert into movies(m_name,m_details,m_duration) values('{}','{}',{})".format(mname,details,du))
                mydb.commit()
                print("******************************************************")
                print("**********************movie added*********************")
                print("******************************************************")



                
            elif cho==3:
                print("******************************************************")
                print("*******************Delete Movie***********************")
                print("******************************************************")
                
                mycur.execute("select * from movies")
                mdata=mycur.fetchall()
                print("******************************************************")
                print("**-ID-****Movie Name**********************************")
                for i in mdata:
                   
                    print(" ",i[0],"  ",i[1])
                print("******************************************************")
                mid=int(input("***Enter ID***:-"))
                mycur.execute("delete from movies where m_id={}".format(mid))
                mydb.commit()
                print("******************************************************")
                print("*********************data deleted*********************")
                print("******************************************************")
                



            elif cho==4:
                print("******************************************************")
                mycur.execute("select * from theatre_list")
                tdata=mycur.fetchall()
                for i in tdata:
                    print(i)
                print("******************************************************")



            elif cho==5:
                print("******************************************************")
                print("********************Movies List***********************")
                print("******************************************************")
                mycur.execute("select * from movies")
                mdata=mycur.fetchall()
                print("**-ID-****_Movie Name_********************************")
                for i in mdata:
                    print(" ",i[0],"    ",i[1])
                print("******************************************************")



            elif cho==6:
                print("******************************************************")
                print("***************Add Movie In Theatre*******************")
                print("******************************************************")
                mycur.execute("select * from movies")
                mdata=mycur.fetchall()
                print("**-ID-****_Movie Name_********************************")
                for i in mdata:
                    print(" ",i[0],"    ",i[1])
                print("******************************************************")
                mov=int(input("***Enter movie id***:-"))
                mycur.execute("select * from theatre_list")
                tdata=mycur.fetchall()
                print("**-ID-****-Theatre Name-******************************")
                for i in tdata:
                    print("  ",i[0],"   ",i[1])
                print("******************************************************")
                th=int(input("enter theatre id"))
                mycur.execute("select * from screen where t_id={}".format(th))
                tdata=mycur.fetchall()
                
                for i in tdata:
                    print('id',i[0],'screen number- ',i[1],'capacity- ',i[2])
                sc1=int(input("enter screen id"))
                mycur.execute("insert into movie_reff (m_id,tl_id,s_id) values ({},{},{})".format(mov,th,sc1))
                mydb.commit()
                print("******************************************************")
                print("*********************data inserted********************")
                print("******************************************************")

                    
            elif cho==7:
                print("******************************************************")
                print("*******************Delete Booking*********************")
                print("******************************************************")
                mycur.execute("truncate book_s")
                mydb.commit()
                print("******************************************************")
                print("********************data deleted**********************")
                print("******************************************************")
            elif cho==8:
                print("******************************************************")
                print("******************Password Change*********************")
                print("******************************************************")
                pas=input("enter new password")
                mycur.execute("update admin set su_password='{}' where su_username='{}'".format(pas,reg[1]))
                mydb.commit()
                print("******************************************************")
                print("******************PASSWORD CHANGED********************")
                print("******************************************************")


            elif cho==9:
                break
            
    def option(self):
        print("******************************************************")
        print("!         Press 1 for Add Theater                    !")
        print("!         Press 2 for Add Movies                     !")
        print("!         Press 3 for Delete Movies                  !")
        print("!         Press 4 for Theater List                   !")
        print("!         Press 5 for Movie List                     !")
        print("!         press 6 for Add Movie In Theatre           !")
        print("!         press 7 for Reset Theatre Booking          !")
        print("!         press 8 for Change Password                !")
        print("!         press 9 for Logout                         !")
        print("******************************************************")
        try:
            ch=int(input("enter your choice"))
            return ch
        except Exception as a:
            print("OOPS somthing went wrong error-",a)
            return 0
    
        





'''






                    
               elif cho==5:
                   print("******************************************************")
                   print("******************Delete Theater**********************")
                   print("******************************************************")
                   mycur.execute("select * from theatre_list")
                   tdata=mycur.fetchall()
                   print("*-ID-*****Theatre Name********************************")
                   for i in tdata:
                       print(" ",i[0],"  ",i[1])
                   print("******************************************************")
                    
                   tid=int(input("****Entre Theatre ID****:- "))
                   con=input("do you really want to continue y/n")
                   if con == "y":
                       mycur.execute("delete from theatre_list where tl_id={}".format(tid))               
                       mydb.commit()
                   print("******************************************************")
                   print("*******************data deleted***********************")
                   print("******************************************************")
                    
                    


'''








        
        
        
        
        
        
