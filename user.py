import pymysql
import smtplib

mydb=pymysql.connect(host="localhost",user="root",passwd="",port=3306,database="ticket_booking")
mycur = mydb.cursor()


class User():
    def start(self,email):
        self.email=email
        
        while True:
            print("******************************************************")
            print("             welcome you",email[4])
            print("******************************************************")
            ch=self.option()
            
            if ch==1:
                print("******************************************************")
                print("****************Tickets Booking Portal****************")
                print("******************************************************")
                mycur.execute("select * from regions")
                rdata=mycur.fetchall()
                print("******************************************************")
                print("**-ID-****-Region-************************************")
                print("******************************************************")
                for i in rdata:
                    if i[0]>1:
                        print(' ',i[0],'  ',i[1])
                reg=int(input("*****Enter ID*****:- "))
                
                mycur.execute("select * from cities where re_id={}".format(reg))
                cdata=mycur.fetchall()
                print("******************************************************")
                print("**-ID-****-Cities-************************************")
                print("******************************************************")
                for i in cdata:
                    print(" ",i[0],'  ',i[1])
                    
                city=int(input("****Enter ID****:- "))
                mycur.execute("select * from theatre_list where cityid={}".format(city))
                tdata=mycur.fetchall()
                print("******************************************************")
                print("**-ID-****-Theatre Name-******************************")
                print("******************************************************")
                for i in tdata:
                    print(' ',i[0],'  ',i[1])
                th=int(input("enter theatre id"))
                mycur.execute("select m_id from movie_reff where tl_id={}".format(th))
                mfdata=mycur.fetchall()
                print("******************************************************")
                print('**-ID-*****-Movie Name-*********-Type-*****-Duration-*')
                print("******************************************************")
                for i in mfdata:
                    mycur.execute("select * from movies where m_id={}".format(i[0]))
                    mo=mycur.fetchall()
                    print(mo[0][0],' ',mo[0][1],' ',mo[0][2],' ',mo[0][3])
                m=int(input("****Enter Movie ID****:- "))
                
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
                        print(i[0],i[3],i[4])
                    
                mo=int(input("***-Enter Time ID***:- "))
                mycur.execute("select capacity from screen where s_id={}".format(g))
                mdata=mycur.fetchone()
                mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                x1=mycur.fetchall()
                x=[]
                for i in x1:
                    x.append(i[0])
                a=0
                print("******************************************************")
                print("*************************Seats************************")
                print("******************************************************")
                
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
                print()
                print("******************************************************")
                print("***********B=> booked ** A=> Available ***************")
                print("******************************************************")
                while True:
                    mycur.execute("select seat_n from book_s where time_id={}".format(mo))
                    x1=mycur.fetchall()
                    x=[]
                    for i in x1:
                        x.append(i[0])
                    y=int(input("***Enter seat number**:- "))
                    
                    if y in x:
                        print("******************************************************")
                        print("***********This Seat Is Already Booked****************")
                        print("******************************************************")
                    else:
                        mycur.execute("insert into book_s (seat_n,time_id) values({},{})".format(y,mo))
                        mydb.commit()
                        
                        mycur.execute("select b_id from book_s where seat_n={} and time_id={}".format(y,mo))
                        mail=mycur.fetchone()[0]
                        
                        mycur.execute("select cost from theatre_time where time_id={}".format(mo))
                        mx=mycur.fetchone()[0]
                        
                        mail1='booking id is -'+str(mail)+' your seat number is -'+str(y)+'screen id is- '+str(mo)+' you pay'+str(mx)
                        print("******************************************************")
                        print("****",mail1,"****")
                        print("******************************************************")


                        
                        mail=smtplib.SMTP('smtp.gmail.com',587)
                        mail.starttls()
                        mail.login("egabhigupta@gmail.com","Abhi@8120610655")
                        mail.sendmail("egabhigupta@gmail.com",self.email[5],str(mail1))
                        mail.quit()
                        c=input("do you wanna book more tickets y/n")
                        if c=='n':
                            break

            elif ch ==2:
                print("******************************************************")
                print("**************Tickets Cancel Portal*******************")
                print("******************************************************")
                b=int(input("enter booking id"))
                mycur.execute("delete from book_s where b_id={}".format(b))
                mydb.commit()
                print("******************************************************")
                print("*******************Ticket Cancel**********************")
                print("******************************************************")
                
            elif ch==3:
                print("******************************************************")
                print("******************Password Change*********************")
                print("******************************************************")
                pas=input("enter new password")
                mycur.execute("update users set u_password='{}' where u_username='{}'".format(pas,email[1]))
                mydb.commit()
                print("******************************************************")
                print("******************PASSWORD CHANGED********************")
                print("******************************************************")
                
            elif ch==4:
                break
                

    def option(self):
        print("******************************************************")
        print("!            Press 1 For Ticket Booking              !")
        print("!            Press 2 For Cancel Booking              !")
        print("!            Press 3 For Change Password             !")
        print("!            Press 4 For Logout                      !")
        print("******************************************************")
        ch=int(input("enter your choice"))
        print("******************************************************")
        return ch
        



