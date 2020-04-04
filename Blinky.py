Import RPi.GPIO as gpio # fetching the GPIO library
From time import sleep # fetching sleep function
gpio.setmode(gpio.BOARD) # This define how we address pins
gpio.setup(10, GPIO.OUT) # Set the pin mode as output

for x in range(15):
    gpio.output(10, gpio.HIGH) # High voltage that means LED on
    Sleep(2)
    gpio.output(10, gpio.LOW) # LOW voltage, LED off.
    sleep(1)

GPIO.cleanup() # remove all the setup and defined pinmodes.
