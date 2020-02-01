#frontend

from tkinter import *
import tkinter.messagebox
#import stdDatabase_backend

class student:
    def init (self,root):
        self.root*root
        self.root.title("SCHOOL ALUMNI MANAGEMENT SYSTEN")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="blue")

        stdId=StringVar()
        name=StringVar()
        dob=StringVar()
        age=StringVar()
        gender=StringVar()
        mobile=StringVar()
        passoutyear=StringVar()

        #===============================function

        def iExit():
            iExit=tkinter.messagebox.askyesno("school alumni management system","confirm if you want to exit")
            if iExit>0
            root.destroy()
            return
        def clearData():
            self.txtstdId.delete(0,END)
            self.txtname.delete(0,END)
            self.txtdob.delete(0,END)
            self.txtage.delete(0,END)
            self.txtgender.delete(0,END)
            self.txtmob.delete(0,END)
            self.txtpoy.delete(0,END)

         def addData():
             if(len(stdId.get())!=0):
                 stdDatabase_Backend.addStdRec(stdId.get(),name.get(),dob.get(),age(),gender.get(),mobile.get(),passoutyear.get()):
                     studentlist.delete(0,END)
                     studentlist.insert(END,(stdId,get(),name.get(),dob.get(),age(),gender.get(),mobile.get(),passoutyear.get()))

         def DisplayData():
             studentlist.delet(0,END)
             for row in StdDatabase_Backend.viewData()
             studentlist.insert(END,row,sttr(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            
            self.txtstdId.delete(0,END)
            self.txtstdId.insert(END,sd[1])
            self.txtname.delete(0,END)
            self.txtname.insert(END,sd[2])
            self.txtdob.delete(0,END)
            self.txtdob.insert(END,sd[3])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[4])
            self.txtgender.delete(0,END)
            self.txtgender.insert(END,sd[5])
            self.txtmob.delete(0,END)
            self.txtmob.insert(END,sd[6])
            self.txtpoy.delete(0,END)
            self.txtpoy.insert(END,sd[7])

        def DeleteData():
            if(len(stdId.get())!=0):
                stdDatabase_Backend.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_Backend.searchData(stdId.get(),name.get(),dob.get(),age.get(),gender.get(),mobile.get(),passoutyear.get())
            studentlist.insert(END,row,str(""))

        def update():
            if(len(stdId,get())!=0):
                stdDatabase_Backend.deleteRec(sd[0])
            if(len(stdId()!=0):
                stdDatabase_Backend.addStdRec(stdId.get(),name.get(),dob.get(),age.get(),gender.get(),mobile.get(),passoutyear.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(stdId.get(),name.get(),dob.get(),age.get(),gender.get(),mobile.get(),passoutyear.get())
                

            
                

        #===============================frame
        MainFrame=frame(self.root,bg="blue")
        MainFrame.grid()

        TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg="white",relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame,font=('arial',47,'bold'),text="SCHOOL ALUMNI MANAGEMENT SYSTEM",bg="white")
        self.lblTit.grid()

        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="white",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=2,width=1350,height=400,padx=20,relief=RIDGE,bg="blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3, relief=RIDGE ,bg="white",
                                  font=('arial',20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="white",
                                  font=('arial',20,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #============================================labels
        self.lblstdId=Label(DataFrameLEFT,font=('arial',20,'bold'),text='student id:',padx=2,pady=2,bg="ghost white")
        self.lblstdId.grid(row=0,column=0,sticky=w)
        self.txtstdId=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.txtstdId.grid(row=0,column=1)

        self.lblfna=Label(DataFrameLeft,font=('arial',20,'bold'),text='name:',padx=2,pady=2,bg="ghost white")
        self.lblfna.grid(row=1,column=0,sticky=w)
        self.lblfna=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lblfna.grid(row=1,column=1)

        self.lbldob=Label(DataFrameLeft,font=('arial',20,'bold'),text='dob:',padx=2,pady=3,bg="ghost white")
        self.lbldob.grid(row=2,column=0,sticky=w)
        self.lbldob=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lbldob.grid(row=2,column=1)

        self.lblage=Label(DataFrameLeft,font=('arial',20,'bold'),text='age:',padx=2,pady=3,bg="ghost white")
        self.lblage.grid(row=3,column=0,sticky=w)
        self.lblage=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lblage.grid(row=3,column=1)

        self.gender=Label(DataFrameLeft,font=('arial',20,'bold'),text='gender:',padx=2,pady=2,bg="ghost white")
        self.lblgender.grid(row=4,column=0,sticky=w)
        self.lblgender=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lblgender.grid(row=4,column=1)

        self.lblmob=Label(DataFrameLeft,font=('arial',20,'bold'),text='mobile:',padx=2,pady=2,bg="ghost white")
        self.lblmob.grid(row=5,column=0,sticky=w)
        self.lblmob=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lblmob.grid(row=5,column=1)

        self.lblpoy=Label(DataFrameLeft,font=('arial',20,'bold'),text='passoutyear:',padx=2,pady=2,bg="ghost white")
        self.lblpoy.grid(row=6,column=0,sticky=w)
        self.lblpoy=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=stdId,width=39)
        self.lblpoy.grid(row=6,column=1)



        # ====================================listbox and scroll bar widget
        

        scrollbar=ScrollBar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist=Listbox(DataFrameRight,width=41.height=16,font=('arial',20,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<listboxselect>>',StudentRec)                           
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist,yview)

        #===============================================button widget
        self.btnAddData=Button(ButtonFrame,text="Add new",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0.column=0)

        self.btnDisplayData=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=displayData)
        self.btnDisplayData.grid(row=0.column=1)

        self.btnClearData=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClearData.grid(row=0.column=2)

        self.btnDeleteData=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0.column=3)

        self.btnSearchData=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0.column=4)

        self.btnUpdateData=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnUpdateData.grid(row=0.column=5)

        self.btnExitData=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4, command=iExit)
                    
        self.btnExitData.grid(row=0.column=6)


if __name__='__main__':
     root=Tk()
     application=Student(root)                             
                                   





        
        








        
        
        

                    
