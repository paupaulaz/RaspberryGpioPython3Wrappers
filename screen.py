from utils.RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

class Screen :
    """
    This class is a wrapper to use an LCD 1602 screen on a Raspberry Pi.
    It assumes that the pins of connection to the gpio boards are consistent with the arguments of the constructor. Note that ports are to be understood here in GPIO.BOARD mode.
    """

    def __init__(self) :
        self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    
    def clear(self):
        self.lcd.clear()

    def display(self, message):
        self.lcd.clear()
        self.lcd.write_string(str(message))

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    screen = Screen()
    screen.clear()
    screen.display("Hello world!")