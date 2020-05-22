import time
from neopixel import *


class LightController:
    def __init__(self, color):      
                      
        self.score_color = color
        self.celebrate_color = Color(127, 127, 127)
        self.clear_color = Color(0,0,0)
        
        self.default_celebrate_iterations = 40
        self.default_wait_ms = 50
                      
        # LED strip configuration:
        iLED_Count      = 42      # Number of LED pixels.
        iLED_Pin        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        iLED_Freq_Hz    = 800000  # LED signal frequency in hertz (usually 800khz)
        iLED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        iLED_Brightness = 255     # Set to 0 for darkest and 255 for brightest
        bLED_Invert     = False   # True to invert the signal (when using NPN transistor level shift)
        iLED_Channel    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    
        self.strip = Adafruit_NeoPixel(iLED_Count, iLED_Pin, iLED_Freq_Hz, iLED_DMA, bLED_Invert, iLED_Brightness, iLED_Channel)
        self.strip.begin()


    #turn off all lights
    def clear(self):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.clear_color)
            self.strip.show()
            time.sleep(self.default_wait_ms/1000.0)

    #flashing celebration
    def celebrate(self):
        """Movie theater light style chaser animation."""
        for j in range(self.default_celebrate_iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, self.celebrate_color)
                    iBrightness = 255 / (q+1)
                    self.strip.setBrightness(iBrightness)
                self.strip.show()
                time.sleep(self.default_wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)
                    
    def showScore(self, iscore):
        for i in range(iscore):
            self.strip.setPixelColor(i, self.score_color)
            self.strip.show()
            time.sleep(self.default_wait_ms/1000.0)
                    
                    

    



