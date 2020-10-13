import RPi.GPIO as a
import time
import blynklib
a.setmode(a.BCM) 
a.setup(2,a.OUT)
a.setup(21,a.OUT)
a.setup(16,a.OUT)
a.setup(7,a.OUT)
a.setup(26,a.OUT)
a.setwarnings(False)
TRIG=4
ECHO=17
a.setup(TRIG,a.OUT)
a.setup(ECHO,a.IN)


con_ht=17.1
total_ht=14.3
BLYNK_AUTH = 'L56yKveGb3RxBE4vLGuwaDH25Tz6TOm3'
blynk = blynklib.Blynk(BLYNK_AUTH)
while(1):
        blynk.run()
	a.output(TRIG,True)
	time.sleep(0.00001)
	a.output(TRIG,False)
	while a.input(ECHO)==False:
		start=time.time()
	while a.input(ECHO)==True:
		end=time.time()
        sig_time=end-start
        distance=sig_time*17150
        water_ht= con_ht - distance
        water_level=(water_ht/total_ht)*100
        water_level=int(water_level)
        print('Water level:',water_level)
        if water_level<=30:
                a.output(26,a.HIGH)
                print('Low')
                a.output(2,a.HIGH)
                a.output(21,a.LOW)
                a.output(16,a.LOW)
                a.output(7,a.LOW)
                blynk.virtual_write(0,255)
                blynk.virtual_write(1,0)
                blynk.virtual_write(2,0)
                blynk.virtual_write(3,water_level)
                blynk.virtual_write(4,water_level)
                blynk.virtual_write(5,water_level)
                if water_level<=10:
                    blynk.notify("Underflow!!!!")
        elif water_level>30 and water_level<=70:
                a.output(26,a.HIGH)
                print('Medium')
                a.output(21,a.HIGH)
                a.output(2,a.LOW)
                a.output(16,a.LOW)

                a.output(7,a.LOW)
                blynk.virtual_write(0,0)
                blynk.virtual_write(1,255)
                blynk.virtual_write(2,0)
                blynk.virtual_write(3,water_level)
                blynk.virtual_write(4,water_level)
                blynk.virtual_write(5,water_level)
        elif water_level>70:
                a.output(26,a.HIGH)
                print('High')
                a.output(16,a.HIGH)
                a.output(2,a.LOW)
                a.output(21,a.LOW)
                blynk.virtual_write(1,0)
                blynk.virtual_write(2,255)
                blynk.virtual_write(3,water_level)
                blynk.virtual_write(4,water_level)
                blynk.virtual_write(5,water_level)
                if water_level>90:
                        print('Overflow!!!!')
			a.output(26,a.LOW)
			a.output(7,a.HIGH)
                        time.sleep(5)
			a.output(7,a.LOW)
                        
 
    	time.sleep(5)
     
a.cleanup()

