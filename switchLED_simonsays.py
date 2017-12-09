# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from datetime import datetime

# einrichten des raspberry
GPIO.setmode(GPIO.BCM)
# Schalter PINS als Ausgabe (ohne Vorwiederstände) schalten. PIN muss auf GROUND gelegt
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_UP) # schalter 1 (rot) mit int. PullUp Res. (wie GPIO Treiber f Recall)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP) # schalter 2 (gelb) mit int. pullUp. Res 
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP) # schalter 3 (grün) mit int. PullUp Res. (wie GPIO Treiber f Recall)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP) # schalter 4 (blau) mit int. PullUp Res. (wie GPIO Treiber f Recall)

# LED PINS als Eingabe schalten
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Variablen setzen
aktuelleTaste = "keine"

# messen, ob schalter geschlossen ist und berührungen zählen
try:
    print "Zum Starten den Taster drücken..."
    while True:
        if GPIO.input(11)==False:
            print "rot"
            aktuelleTaste = "rot"
            GPIO.output(4, 1)
        else:
            GPIO.output(4, 0)
        if GPIO.input(5)==False:
            print "gelb"
            aktuelleTaste = "gelb"
            GPIO.output(18, 1)
        else:
            GPIO.output(18, 0)
        if GPIO.input(6)==False:
            print "grün"
            aktuelleTaste = "grün"
            GPIO.output(23, 1)
        else:
            GPIO.output(23, 0)
        if GPIO.input(13)==False:
            print "blau"
            aktuelleTaste = "blau"
            GPIO.output(24, 1)
        else:
            GPIO.output(24, 0)
      

# Eingaben und Ausgaben beim Raspberry aufraeumen
except KeyboardInterrupt:
    GPIO.cleanup()
