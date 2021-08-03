import pymysql
import smtplib
from user import *

class Theater():
    def start_app(self,i):
        self.i=i
        while True:
            print("******************************************************")
            print("             welcome to",i[4])
            print("******************************************************")
            ch=self.options()
            if ch==1:
                print("******************************************************")
                print("****************Check Seat Availabal******************")
                print("******************************************************")
                mycur.execute("select tl_id from theatre_list where tid={}".format(self.i[0]))
                th=mycur.fetchone()[0]
                mycur.execute("select m_id from movie_reff where tl_id={}".format(th))
                mfdata=mycur.fetchall()
                print("******************************************************")
                print('**-ID-***-Name-*****-Type-****-Duration-**************')
                print("******************************************************")
                for i in mfdata:
                    mycur.execute("select * from movies where m_id={}".format(i[0]))
                    mo=mycur.fetchall()
                    print(mo[0][0],' ',mo[0][1],' ',mo[0][2],' ',mo[0][3])
                m=int(input("***Enter movie ID***:- "))
                
                mycur.execute("select s_id from movie_reff where m_id={} and tl_id={}".format(m,th))
                m1=mycur.fetchall()
                print("******************************************************")
                print("**-ID-***-Time-***-Price-*****************************")
                print("******************************************************")
                for i in m1:
                    g=i[0]
                    mycur.execute("select * from theatre_time where tlid={} and s_id={}".format(th,i[0]))
                    m5=mycur.fetchall()
                    for i in m5:
                        print(' ',i[0],i[3],i[4])
                    
                mo=int(input("***Enter time ID***:- "))
                mycur.execute("select capacity from screen where s_id={}".format(g))
                mdata=mycur.fetchone()
                mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                x1=mycur.fetchall()
                x=[]
                for i in x1:
                    x.append(i[0])
                print("******************************************************")
                print("*************************Seats************************")
                print("******************************************************")
                    
                a=0
                for i in range(1,mdata[0]):
                    for j in x:
                        if j==i:
                            print(i,"=>B  ",end='')
                            a=1
                    if a==0:
                        print(i,"=>A  ",end='')
                    if i==10 or i==20 or i==30 or i==40 or i==50:
                        print()
                    a=0
                    
                print("******************************************************")
                print("**********B=> booked, ** A=> Available****************")
                print("******************************************************")
                
                
            elif ch==2:
                print("******************************************************")
                print("****************Check Seat Availabal******************")
                print("******************************************************")
                mycur.execute("select tl_id from theatre_list where tid={}".format(self.i[0]))
                th=mycur.fetchone()[0]
                mycur.execute("select m_id from movie_reff where tl_id={}".format(th))
                mfdata=mycur.fetchall()
                print("******************************************************")
                print('**-ID-***-Name-*****-Type-****-Duration-**************')
                print("******************************************************")
                for i in mfdata:
                    mycur.execute("select * from movies where m_id={}".format(i[0]))
                    mo=mycur.fetchall()
                    print(mo[0][0],' ',mo[0][1],' ',mo[0][2],' ',mo[0][3])
                m=int(input("***Enter movie ID***:- "))
                
                mycur.execute("select s_id from movie_reff where m_id={} and tl_id={}".format(m,th))
                m1=mycur.fetchall()
                print("******************************************************")
                print("**-ID-***-Time-***-Price-*******************************")
                print("******************************************************")
                for i in m1:
                    g=i[0]
                    mycur.execute("select * from theatre_time where tlid={} and s_id={}".format(th,i[0]))
                    m5=mycur.fetchall()
                    for i in m5:
                        print(' ',i[0],i[3],i[4])
                    
                mo=int(input("***Enter time ID***:- "))
                mycur.execute("select capacity from screen where s_id={}".format(g))
                mdata=mycur.fetchone()
                mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                x1=mycur.fetchall()
                x=[]
                for i in x1:
                    x.append(i[0])
                print("******************************************************")
                print("*************************Seats************************")
                print("******************************************************")
                    
                a=0
                for i in range(1,mdata[0]):
                    for j in x:
                        if j==i:
                            print(i,"=>B  ",end='')
                            a=1
                    if a==0:
                        print(i,"=>A  ",end='')
                    if i==10 or i==20 or i==30 or i==40 or i==50:
                        print()
                    a=0
                    
                print("******************************************************")
                print("**********B=> booked, ** A=> Available****************")
                print("******************************************************")
                
                while True:
                    
                    y=int(input("****Enter Seat Number****:- "))
                    mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                    x1=mycur.fetchall()
                    x=[]
                    for i in x1:
                        x.append(i[0])
                                 
                    if y in x:
                        print("******************************************************")
                        print("***********The Seat Is Already Booked*****************")
                        print("******************************************************")
                    else:
                        mycur.execute("insert into book_s (seat_n,time_id) values({},{})".format(y,mo))
                        mydb.commit()
                        print("seat booked")
                        mycur.execute("select b_id from book_s where seat_n={} and time_id={}".format(y,mo))
                        mail=mycur.fetchone()[0]
                        
                        mycur.execute("select cost from theatre_time where time_id={}".format(mo))
                        mx=mycur.fetchone()[0]
                        mail1='booking id is -'+str(mail)+'you pay'+str(mx)
                        print(mail1)
                        print("******************************************************")
                        c=input("do you wanna book more tickets y/n")
                        if c=='n':
                            print("******************************************************")
                            break
            elif ch==3:
                print("******************************************************")
                print("********************Cancle Booking********************")
                print("******************************************************")
                b=int(input("***-Enter Booking ID***:-"))
                mycur.execute("delete from book_s where b_id={}".format(b))
                mydb.commit()
                print("******************************************************")
                print("*****************Tickets cancelled********************")
                print("******************************************************")

            elif ch==4:
                
                print("******************************************************")
                print("**********************Collection**********************")
                print("******************************************************")
                mycur.execute("select tl_id from theatre_list where tid={}".format(self.i[0]))
                th=mycur.fetchone()[0]
                mycur.execute("select m_id from movie_reff where tl_id={}".format(th))
                mfdata=mycur.fetchall()
                print("******************************************************")
                print('**-ID-***-Name-*****-Type-****-Duration-**************')
                print("******************************************************")
                for i in mfdata:
                    mycur.execute("select * from movies where m_id={}".format(i[0]))
                    mo=mycur.fetchall()
                    print(mo[0][0],' ',mo[0][1],' ',mo[0][2],' ',mo[0][3])
                m=int(input("***Enter movie ID***:- "))
                
                mycur.execute("select s_id from movie_reff where m_id={} and tl_id={}".format(m,th))
                m1=mycur.fetchall()
                print("******************************************************")
                print("**-ID-***-Time-***-Price-*****************************")
                print("******************************************************")
                for i in m1:
                    g=i[0]
                    mycur.execute("select * from theatre_time where tlid={} and s_id={}".format(th,i[0]))
                    m5=mycur.fetchall()
                    for i in m5:
                        print(' ',i[0],i[3],i[4])
                    
                mo=int(input("***Enter time ID***:- "))
                mycur.execute("select capacity from screen where s_id={}".format(g))
                mdata=mycur.fetchone()
                mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                x1=mycur.fetchall()
                x=[]
                for i in x1:
                    x.append(i[0])
                print("******************************************************")
                print("*************************Seats************************")
                print("******************************************************")
                    
                a=0
                for i in range(1,mdata[0]):
                    for j in x:
                        if j==i:
                            print(i,"=>B  ",end='')
                            a=1
                    if a==0:
                        print(i,"=>A  ",end='')
                    if i==10 or i==20 or i==30 or i==40 or i==50:
                        print()
                    a=0
                    
                print("******************************************************")
                print("**********B=> booked, ** A=> Available****************")
                print("******************************************************")
                
            elif ch==4:
                break

    def options(self):
        print("******************************************************")
        print("!           Press 1 for View Seats                   !")
        print("!           Press 2 for Book Tickets                 !")
        print("!           Press 3 for Cancel Tickets               !")
        print("!           Press 4 for Logout                       !")
        print("******************************************************")
        
        ch=int(input("***Enter Your Choice***:- "))
        return ch
