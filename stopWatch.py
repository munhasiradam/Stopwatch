#https://docs.python.org/3/library/tkinter.html

try:
    import tkinter as tk
    import tkinter.font as font
    from tkinter import messagebox as mB
    import os 
    import math
    from datetime import date as dT
    import importerror
except ImportError as IE:
    os.system('color 4f')
    print('IMPORT ERROR... \n ->', IE)
else:
    introduction_msg = '''
        Firstly I'a junior(beginner) in Python and if u wanna point out. I'M open to comments from relevant experts on the subject.
    '''
    print(introduction_msg)
finally:
    print(' Creat | 2023.02.15 \n Today |', dT.today())


labelArray = []

labelRange = range(14)

labelint_Numb = int(0)
labelPos = int(0)
canvasWidth = int(600)
canvasHeight = int(350)

time, hours, minutes, seconds = float(0), float(0), float(0), float(0)

running = False

mainWindow = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
canvas = tk.Canvas(mainWindow, width=canvasWidth, height=canvasHeight, background='#0D0D0D')
stopWatch_text = tk.Label(canvas, text='00:00:00', font=('Courier', 69))


if __name__ == '__main__':
    
    class MaFuncs():
        
        @staticmethod
        def LabelAppendFunc():

            global labelint_Numb
            global labelArray
            global labelPos
            global labelRange

            for j in labelRange:
                labelArray.append(str(j))
                labelArray[j] = tk.Label(canvas, text=str(j), font=('Courier', 1), background='white', foreground='black')
                labelArray[j].place(relx=0, rely=labelPos / 350)
                labelPos += 25


        def LabelFunc(btnName):
            
            os.system('cls')
            os.system('color 02')
            global labelint_Numb
            global labelArray
            global labelRange

            if(labelint_Numb > 13):
                for a in labelRange:
                    labelArray[a].config(text=str(a), font=('Courier', 1))
                labelint_Numb = 1
                labelArray[0].config(text=str(btnName), font=('Courier', 10))
                print('selected -> ', labelArray[0].cget("text"), '\n', 'labeintNumb -> ', labelint_Numb)
            else:
                for i in labelRange:
                    if str(labelint_Numb) == labelArray[i].cget("text"):
                        labelArray[i].config(text=str(btnName), font=('Courier', 10))
                        labelint_Numb+=1
                        print('selected -> ', labelArray[i].cget("text"), '\n', 'labeintNumb -> ', labelint_Numb)
                        break

            print('_' * 35)
            
            loopV = 0
            while loopV <= len(labelArray) -1:
                print(loopV, '- ' , labelArray[loopV].cget("text"))
                loopV +=1


        def Update():
            
            global time, hours, minutes, seconds
            time += 1
            seconds = time % 60
            minutes = ( time / 60 ) % 60
            hours = (time / 60 / 60) % 24

            hours_str = '{0}'.format(math.trunc(hours)) if hours >= 10 else '0{0}'.format(math.trunc(hours))
            minutes_str = '{0}'.format(math.trunc(minutes)) if minutes >= 10 else '0{0}'.format(math.trunc(minutes))
            seconds_str = '{0}'.format(math.trunc(seconds)) if seconds >= 10 else '0{0}'.format(math.trunc(seconds))

            stopWatch_text.config(text='{0}:{1}:{2}'.format(hours_str, minutes_str, seconds_str))
            
            global update_time
            update_time = stopWatch_text.after(1000, MaFuncs.Update)


        def StartBtnFunc():
            MaFuncs.LabelFunc('Start')
            global running
            if not running:
                MaFuncs.Update()
                running = True

        def PauseBtnFunc():
            MaFuncs.LabelFunc('Pause')
            global running
            if running:
                stopWatch_text.after_cancel(update_time)
                running = False
                

        def ResetBtnFunc():
            MaFuncs.LabelFunc('Reset')
            global running
            if running:
                stopWatch_text.after_cancel(update_time)
                running = False
                
            global time, hours, minutes, seconds
            time, hours, minutes, seconds = float(0), float(0), float(0), float(0)

            stopWatch_text.config(text='00:00:00')


        def QuitBtnFunc():
            quitBox = mB.askquestion(title='Quit', message='Do u wanna quit ?')
            if(quitBox == 'yes'):
                mainWindow.destroy()


    class GUI():
        
        def Start():
            #Tk class reference variable set implementation
            global mainWindow

            #variables 
            global canvasWidth
            global canvasHeight
            myFont = font.Font(family='Courier', size=18, weight='bold')

            #mainWindow
            mainWindow.title('_stopWatch_')
            mainWindow.geometry("600x400")
            mainWindow.configure(background='#1F1F1F', borderwidth=5)
            mainWindow.minsize(width=canvasWidth, height=400)
            mainWindow.resizable(True, True)
            mainWindow.state('normal')
            mainWindow.wm_attributes('-alpha', 0.95)

            #others
            try:
                icon = tk.PhotoImage(file='munhasiradam-ico.png')
                mainWindow.iconphoto(False, icon)
            except tk.TclError as tclErr:
                print('icon error-> ', tclErr)

            #canvas
            global canvas
            canvas.place(relx=0, rely=0, relwidth=1, relheight=1) #If u want to be stable -> #canvas.pack(side='top')

            #buttons
            startBtn = tk.Button(canvas, text='Start', width=5, height=4, relief=tk.RIDGE, background='#329f48', activebackground='#044e13', foreground='white', border=0, command=MaFuncs.StartBtnFunc)
            startBtn['font'] = myFont
            startBtn.place(relx=0.225, rely=0.5, relheight=0.35, relwidth=0.15, anchor='nw') #If u want to be stable -> x=canvas.winfo_reqwidth() /3 - startBtn.winfo_reqwidth() / 2, y=canvas.winfo_reqheight() / 2 + (canvas.winfo_reqheight() / 2 - startBtn.winfo_reqheight()) / 2

            pauseBtn = tk.Button(canvas, text='Pause', width=5, height=4, relief=tk.RIDGE, background='#b9ad09', activebackground='#6b6405', foreground='white', border=0, command=MaFuncs.PauseBtnFunc)
            pauseBtn['font'] = myFont
            pauseBtn.place(relx=0.425, rely=0.5, relheight=0.35, relwidth=0.15, anchor='nw')

            resetBtn = tk.Button(canvas, text='Reset', width=5, height=4, relief=tk.RIDGE, background='#a60808', activebackground='#6b0000', foreground='white', border=0, command=MaFuncs.ResetBtnFunc)
            resetBtn['font'] = myFont
            resetBtn.place(relx=0.625, rely=0.5, relheight=0.35, relwidth=0.15, anchor='nw')

            quitBtn = tk.Button(mainWindow, text='Quit', width=5, height=1, relief=tk.RIDGE, background='#a60808', activebackground='#6b0000', foreground='white', border=0, command=MaFuncs.QuitBtnFunc)
            quitBtn['font'] = myFont
            quitBtn.place(relx=0.425, rely=0.9, relheight=0.05, relwidth=0.15, anchor='nw')

            #stopWatch_text
            global stopWatch_text
            stopWatch_text.place(relx=0.05, rely=0.05, relheight=0.4, relwidth=0.9, anchor='nw')

            MaFuncs.LabelAppendFunc()

            #event loop
            mainWindow.mainloop()
        Start()
else:
    pass