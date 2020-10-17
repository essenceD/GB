from itertools import cycle
import tkinter as tk
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        root = tk.Tk()
        labe_1 = tk.Label(text='My TrafficLight', font=('Fixedsys', 30, 'bold'))
        labe_1.config(bd=0, bg='#B0C4DE')
        labe_1.pack()
        root.title('MyTrafficLight v.1.0')
        c = tk.Canvas(root, width=400, height=600, bg='#D3D3D3')
        c.pack()
        c.create_oval(150, 100, 250, 200, width=5, fill='#FFC0CB', tag='red')
        c.create_oval(150, 200, 250, 300, width=5, fill='#F0E68C', tag='yel')
        c.create_oval(150, 300, 250, 400, width=5, fill='#90EE90', tag='gre')
        btn = tk.Button(root, text="STOP IT!", command=root.destroy)
        btn.pack()
        btn.bind('<Button-1>')
        for i in cycle(self._TrafficLight__color):
            if i == 'red':
                c.itemconfig('red', fill='red')
                root.update()
                time.sleep(1)
                c.itemconfig('red', fill='#FFC0CB')
                root.update()
            elif i == 'yellow':
                c.itemconfig('yel', fill='yellow')
                root.update()
                time.sleep(1)
                c.itemconfig('yel', fill='#F0E68C')
                root.update()
            else:
                c.itemconfig('gre', fill='green')
                root.update()
                time.sleep(1)
                c.itemconfig('gre', fill='#90EE90')
                root.update()
        root.mainloop()


a = TrafficLight()
TrafficLight.running(a)


