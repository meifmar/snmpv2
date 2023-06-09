#Import Requirements

from easysnmp import snmp_get
from tkinter import *
from tkinter import ttk

#TKInter GUI

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="SNMP Abfragen").grid(column=0, row=0)
    
entryIP = Entry(master=root, bg='white').grid(column=0, row=1)
#result = snmp_get('.1.3.6.1.2.1.1.1.0', hostname='ip', community='public', version=1)  #Diverses Abfrage
#result1 = snmp_get('.1.3.6.1.2.1.1.5.0', hostname='ip', community='public', version=1) #Hostname Abfrage
#result2 = snmp_get('.1.3.6.1.2.1.1.6.0', hostname='ip', community='public', version=1) #System-Aufenthalt Abfrage
#result3 = snmp_get('.1.3.6.1.2.1.1.3.0', hostname='ip', community='public', version=1) #Uptime Abfrage

ttk.Button(frm, text="Abfragen", command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text="Schliessen", command=root.destroy).grid(column=1, row=2)
root.mainloop()
