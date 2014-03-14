'''
Final project of Introduction to Programmming
Python v2.7.6, sqlite3 v2.6.0, sqlite3 sqlite v3.6.21
Copyright Yifei Ren

In this program I create/modify exsisting database and allow users
1. Insert new data or modify existing data in database
2. Delete data from the database
3. Search data based on a criteria
4. Browse all existing data in the database
by typing the operation number.
'''



#Sqlite3 is imported for database.
import sqlite3


#I create global variables for database processing.


#createDb = sqlite3.connect('test.db')
createDb = sqlite3.connect(':memory:')#test version, create database in memory and can be easily deleted.
queryCurs = createDb.cursor()

#Create database: time is in format YYYYMMDDHH and the following are environment stations containing geomagnetic values as integers.
def createTable():
    queryCurs.execute('''CREATE TABLE geo
(id INTEGER PRIMARY KEY, time INTEGER, kev INTEGER, mas INTEGER, kil INTEGER)''')

#Insert data after getting new geomagnetic activity data.
def addReco(time,kev,mas,kil):
    queryCurs.execute('''INSERT INTO geo (time,kev,mas,kil)
    VALUES(?,?,?,?)''',(time,kev,mas,kil))

#Here is the main function.
def main():
    #At first call createTable() to input our data.
    createTable()
    #Here are example data.
    addReco(2013121620, 30,26,23)
    addReco(2013121621, 16,7,6)
    addReco(2013121622, 5,4,4)
    #Commet change.
    createDb.commit()

    #Here I provide user several operation choices and user can choose by entering number.
    print('''Dear user, you have accessed to Geomagnetic Activity in Finland.
You can choose:
1.Insert new data
2.Modify existing data in database
3.Delete data from the database
4.Search data based on a criteria
5.Browse all existing data in the database
0.Exit program''')
    op = input("Type number to choose your operation: ")

    #The four functions are implemented in WHILE loop and boolean as the condition.
    #Only 0 will break the loop, 1-4 are functional signal and others will return error message for user.
    while True:
        
        #Operation 0: End the database operation.
        if op==0:
            print "You have exit the program!"            
            break
        
        #Operation 1. Insert data after getting new geomagnetic activity data.
        elif op==1:
            time=raw_input("Time: (YYYYMMDDHH, eg.2013121515 is 2013-12-15 15:00:00)")
            kev=input("KEV: ")
            mas=input("MAS: ")
            kil=input("KIL: ")
            addReco(time,kev,mas,kil)
            createDb.commit()
            print "You have add one record!"
            
        #Operation 2. User can change the geomagnetic activity record of station according to the datetime.
        elif op==2:
            #Ask which row user want to change.
            r=input("Which record you want to change: ")
            #Get how many records in the database.
            queryCurs.execute('SELECT * FROM geo')
            records=len(queryCurs.fetchall())

            #Check whether database has the r row.
            if r<=records:
                #Choose the colomn user want to change and manage by numbers.
                c=input("You want to change 1.time 2.KEV 3.MAS 4.KIL :")
                if c==1:#change time
                    nTime=raw_input("New time is :")
                    queryCurs.execute('UPDATE geo SET time='+nTime+' WHERE id ='+str(r))
                elif c==2:#change KEV
                    nKev=raw_input("New value of KEV is :")
                    queryCurs.execute('UPDATE geo SET kev='+nKev+' WHERE id ='+str(r))
                elif c==3:#change MAS
                    nMas=raw_input("New value of MAS is :")
                    queryCurs.execute('UPDATE geo SET mas='+nMas+' WHERE id ='+str(r))
                elif c==4:#change KIL
                    nKil=raw_input("New value of KIL is :")
                    queryCurs.execute('UPDATE geo SET kil='+nKil+' WHERE id ='+str(r))
                else:
                    print "Out of record!"
                createDb.commit()
            #The case database doesn't have the r row.
            else:
                print "Out of record!"

        #Operation 3. Delete a row of data from database.
        elif op==3:
            #Get how many records in the database.
            queryCurs.execute('SELECT * FROM geo')
            records=len(queryCurs.fetchall())

            #Get the row user want to delete.
            delete=input("Type in the record ID you want to delete: ")
            #Check whether database has this row.
            if delete<=records:
                queryCurs.execute('DELETE FROM geo WHERE id='+str(delete))
                print "You have delete the "+str(delete)+" record!"
                createDb.commit()
            else:
                print "Out of record!"

        #Operation 4. Search data based on a criteria
        elif op==4:
            #Ask which row user want to search.
            r=input("Which record you want to search: ")
            #Get how many records in the database.
            queryCurs.execute('SELECT * FROM geo')
            records=len(queryCurs.fetchall())

            #Check whether database has the r row.
            if r<=records:
                #Choose the colomn user want to select and manage by numbers.
                c=input("You want to select 1.time 2.KEV 3.MAS 4.KIL :")
                if c==1:#select time
                    queryCurs.execute('SELECT time FROM geo WHERE id='+str(r))
                    print queryCurs.fetchall()
                elif c==2:#select KEV
                    queryCurs.execute('SELECT kev FROM geo WHERE id='+str(r))
                    print queryCurs.fetchall()
                elif c==3:#select MAS
                    queryCurs.execute('SELECT mas FROM geo WHERE id='+str(r))
                    print queryCurs.fetchall()
                elif c==4:#select KIL
                    queryCurs.execute('SELECT kil FROM geo WHERE id='+str(r))
                    print queryCurs.fetchall()
                else:
                    print "Out of record!"                                                               
            else:
                print "Out of record!"

        #Operation 5. Explore all existing data.
        elif op==5: 
            queryCurs.execute('SELECT * FROM geo')
            print (queryCurs.fetchall())

        #Other number. Show error message for asking a validate number.
        else: 
            print "Type a validate number for operation or 0 for exit."

        #Do the loop again to ask for more operations.
        op = input("Type number to choose your operation: ")

    #Close the query cursor.
    queryCurs.close()
