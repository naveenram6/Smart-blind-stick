import machine as m
import utime as u

trigger=m.Pin(0,m.Pin.OUT)
echo=m.Pin(1,m.Pin.IN,m.Pin.PULL_DOWN)
buzzer=m.Pin(3,m.Pin.OUT)
l=m.Pin(25,m.Pin.OUT)
 
while 1:
    l.on()
    trigger.low()
    u.sleep_us(2)
    trigger.high()
    u.sleep_us(5)
    trigger.low()
    while echo.value()== 0:
        send =u.ticks_us()
    while echo.value() == 1:
        rec=u.ticks_us()
    duration = rec - send
    distance =(duration*0.0343)/2
    print("distance=",distance)
    u.sleep(0.1)
    
    if distance <100:
        buzzer.on()
    else:
        buzzer.off()
   
