from tkinter import *

class VideoInfo():

    def __init__(self,props):
        self.moduleid=1
        self.props=props
        self.root=Frame(self.props['root'],bg='darkslategray').grid()

    def Main(self):
        root=self.root
        MainLabel=Label(root,text='Titre : Ninhio Mon poto',padx=10,pady=10,font='fantasy',fg="darkslategray")
        MainLabel2=Label(root,text='Destination : F:\code\Projets',padx=10,pady=10,font='fantasy',fg="darkslategray")
        MainLabel3=Label(root,text='File Size : 22 Mo',padx=10,pady=10,font='fantasy',fg="darkslategray")

        MainButton2=Button(root,text='Change',width='10',border=0,bg="royalblue",activebackground='blue',fg='white',padx=10,pady=5,activeforeground='white',font="arial")
        MainButton=Button(root,text='Download',width='10',border=0,bg="royalblue",activebackground='blue',fg='white',padx=10,pady=5,activeforeground='white',font="arial")
        
        
        MainLabel.grid(row=3)
        MainLabel2.grid(row=4)
        MainButton2.grid(row=5)
        MainLabel3.grid(row=6)
        MainButton.grid(row=7)
        