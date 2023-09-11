#Import Requirements

from easysnmp import snmp_get
from tkinter import *
from tkinter import ttk

#TKInter GUI

#ip_address = "0.0.0.0"

fenster = Tk()
fenster.title("SNMP Monitor")
    
#entryIP = Entry(master=root, bg='white').grid(column=0, row=1)
#result = snmp_get('.1.3.6.1.2.1.1.1.0', hostname='ip', community='public', version=1)  #Diverses Abfrage
#result1 = snmp_get('.1.3.6.1.2.1.1.5.0', hostname='ip', community='public', version=1) #Hostname Abfrage
#result2 = snmp_get('.1.3.6.1.2.1.1.6.0', hostname='ip', community='public', version=1) #System-Aufenthalt Abfrage
#result3 = snmp_get('.1.3.6.1.2.1.1.3.0', hostname='ip', community='public', version=1) #Uptime Abfrage


def funcGet():
    ip_address = "0.0.0.0"
    #if (entry_ip.size()>0):
    ip_address = entry_ip.get()
    if ip_address <= "0":
        print ("Bitte geben Sie eine neue IP Adresse ein")
        label_result.config(text="Bitte geben Sie eine neue IP Adresse ein")

    else:
        snmp_result = snmp_get('.1.3.6.1.2.1.1.5.0', hostname=ip_address, community='public', version=1)
        snmp_result1 = snmp_get('.1.3.6.1.2.1.1.6.0', hostname=ip_address, community='public', version=1)
        snmp_result2 = snmp_get('.1.3.6.1.2.1.1.3.0', hostname=ip_address, community='public', version=1)
        snmp_result3 = snmp_get('.1.3.6.1.2.1.1.1.0', hostname=ip_address, community='public', version=1)
        label_result.config(text=(snmp_result.value+"= Hostname"))
        label_result1.config(text=(snmp_result1.value+"= System Aufenthalt"))
        label_result2.config(text=(snmp_result2.value+"= Uptime"))
        label_result3.config(text=(snmp_result3.value+"= Betriebssystem"))
        print (snmp_result.value, "= Hostname")
        print (snmp_result1.value, "= System Aufenthalt")
        print (snmp_result2.value, "= Uptime")
        print (snmp_result3.value, "= Betriebssystem")


button_abfrage = Button(fenster, text="SNMP Get ausführen", command=funcGet, width=40)
entry_ip = Entry(fenster, bd=5, width=40)
label_result = Label(fenster, text="Leer")
label_result1 = Label(fenster, text="Leer")
label_result2 = Label(fenster, text="Leer")
label_result3 = Label(fenster, text="Leer")

button_abfrage.grid(row=1, column=0)
entry_ip.grid(row=0,column=0)
label_result.grid(row=2, column=0)
label_result1.grid(row=3, column=0)
label_result2.grid(row=4, column=0)
label_result3.grid(row=5, column=0)



fenster.mainloop()
