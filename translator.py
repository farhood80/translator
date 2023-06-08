#importing libarries and packages(modules)

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


#create a display window for user
show = Tk()
show.geometry('1080x720')
show.resizable(0,0)
show.config(bg = 'ghost white')

#we use tkinter library to create a window where text will be converted to voice
show.title("our project for second semester")
Label(show, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(show,text ="Project for team ALPHA", font = 'arial 22 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')


#create an Input-output text displayer (one for showing what we enetered one for trasnlated
Label(show,text ="Enter Text", font = 'arial 16 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(show,font = 'arial 16 bold', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)
Label(show,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(show,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

#define Combobox to a choose a language
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(show, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('input languages: ')
dests_lang = ttk.Combobox(show, values= language, width =22)
dests_lang.place(x=890,y=60)
dests_lang.set('output languages: ')

#This function will translate the message and give us the output.
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

#this function button is for translating
trans_btn = Button(show, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1',activebackground='sky blue')
trans_btn.place(x=490, y=180)
show.mainloop()
