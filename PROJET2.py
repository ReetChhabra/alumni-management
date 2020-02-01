import sqlite3

#backend

def studentData():
    con=sqlite3.connect("")
    cur.execute("CREATE TABLE IF NOT EXISTS students(id integer PRIMARY KEY,stdId text,name test,dob text , age text , gender text , mobile text , passout year text)")
    con.commit()
    con,close()

def addStdRec(stdId,name,dob,age,gender,mobile,passoutyear):
    con=sqlite3.connect("")
    cur.execute("INSERT INTO _____ values (NULL,,,,,,,,)",stdId,name,dob,age,gender,mobile,passoutyear))
    con.commit()
    con.close()

def viewDate():
    con=sqlite3.connect("")
    cur=con.cursor(*)
    cur.execute("SELECT * FROM ")
    row=cur.fetchall()
    con.close
    return rows

def deleteRec():
    con=sqlite3.connect("")
    cur=con.cursor(*)
    cur.execute("DELETE * FROM___ WHWRE id=?",(id,))
    con.commit()
    con.close

def searchData(stdId="",name="",dob="",age="",gender="",mobile="",passoutyear""):
    con=sqlite3.connect("")
    cur=con.cursor()
    cur.execute("SELECT * FROM ____ WHERE stdId=? or name=? or dob=? or age=? or gender=? , mobile=? , passoutyear=?",(stdId,name,dob,age,gender,mobile,passoutyear))
    rocur.fetchall()
    con.close()
    return rows

def dataUpdate(id,stdId="",name="",dob="",age="",gender="",mobile="",passoutyear=""):
    con=sqlite3.connect("")
    cur=con.execute()
    cur.execute("UPDATE ____ SET stdId=?,name=?,dob=?,age=?,gender=?,mobile=?,passoutyear=?" ,\
                (stdId,name,dob,age,gender,mobile,passoutyear))
    com.commit()
    con.close()
