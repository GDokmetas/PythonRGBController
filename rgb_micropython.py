from machine import *
kirmizi = machine.Pin(1)
yesil = machine.Pin(2)
mavi = machine.Pin(3)

kirmizi.off()
yesil.off()
mavi.off()

kirmizipwm = machine.PWM(kirmizi)
yesilpwm = machine.PWM(yesil)
mavipwm = machine.PWM(mavi)


kirmizipwm.duty_u16(0)
yesilpwm.duty_u16(0)
mavipwm.duty_u16(0)

uart = UART(1, 9600, tx = Pin(8), rx = Pin(9))

while True:
    rx = bytes()
    while uart.any() > 0:
        rx += uart.read(10)
    
    rx = rx.decode('Ascii')
    if(rx != ""):
        print(rx)
        kirmizi_deger = int((rx[0:3]))
        yesil_deger = int((rx[3:6]))
        mavi_deger = int((rx[6:9]))
        parlaklik = int(rx[9])
        print(parlaklik)
        print(kirmizi_deger, yesil_deger, mavi_deger)
        kirmizi_deger = kirmizi_deger << parlaklik
        yesil_deger = yesil_deger << parlaklik
        mavi_deger = mavi_deger << parlaklik
        kirmizipwm.duty_u16(kirmizi_deger)
        yesilpwm.duty_u16(yesil_deger)
        mavipwm.duty_u16(mavi_deger)
    