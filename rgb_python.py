import serial.tools.list_ports
import serial
import PySimpleGUI as sg
ser = None  #Global tanımlanmalı

def serial_ports():
    ports = serial.tools.list_ports.comports()
    print(ports)
    seri_port = []
    for p in ports:
        print(p.device)
        seri_port.append(p.device)
    print(seri_port)
    return seri_port
########################
def serial_baglan():
    com_deger = value[0]
    baud_deger = value[1]
    print("Baud Deger", value[1])
    global ser
    ser = serial.Serial(com_deger, baud_deger, timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)
    window["-BAGLANDI_TEXT-"].update('Bağlandı...')

sg.theme("Reddit")

layout =[ [sg.Text("Port Seçiniz:"), sg.Combo(serial_ports(), size=(10,1)),
            sg.Text("Baud Seçiniz:"), sg.Combo(["110","300","600","1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000", "256000"], default_value=9600), 
            sg.Button(button_text="Bağlan", key="-BAGLAN-", size=(10,1)) ],
            [sg.Text("", size=(10,1), key="-BAGLANDI_TEXT-")],
            [sg.Text("Kırmızı:"), sg.Slider(range=(0,255), default_value=0, resolution=1, key="kirmizi"), sg.Text("Yeşil:"), sg.Slider(range=(0,255), default_value=0, resolution=1, key="yesil"), 
            sg.Text("Mavi:"), sg.Slider(range=(0,255), default_value=0, resolution=1, key="mavi"), sg.Button(button_text="AYARLA", key="ayarla") ]
        ]

window = sg.Window("Python RGB Kontrol", layout)

while True:
    event, value = window.read(timeout=1000) 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break    
    if event == "-BAGLAN-":
        if (value[0] == ""):
            sg.popup("Bir Port Seçiniz!", title="Hata", custom_text="Tamam") 
        elif (value[1] == ""):
            sg.popup("Baud Oranını Seçiniz!", title="Hata", custom_text="Tamam")
        else:
            serial_baglan()
    if event == "ayarla":
        kirmizi = int(value['kirmizi'])
        yesil = int(value['yesil'])
        mavi = int(value['mavi'])
        kirmizi = format(kirmizi, "03d") 
        yesil = format(yesil, "03d") 
        mavi = format(mavi, "03d") 
        veri = kirmizi + yesil + mavi 
        print(veri)
        ser.write(veri.encode('Ascii'))
   
window.close()