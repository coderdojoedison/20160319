import time
import RPi.GPIO as GPIO
#Author - Jaydeep J Vyas, March 14th 2016

MORSE_PIN = 13

# 2 seconds duration for Dah
DAH_DURATION = 1.5
DAH = "-"

# 1 second duration for Dit
DIT_DURATION = 0.5
DIT = "."

SPACE_DURATION = 0.1

END_CHAR = ";"
END_WORD = "\n"

morse_dict = {'a':'.-'};
morse_dict['b'] = "-...";
morse_dict['c'] = "-.-.";
morse_dict['d'] = "-..";
morse_dict['e'] = ".";
morse_dict['f'] = "..-.";
morse_dict['g'] = "--.";
morse_dict['h'] = "....";
morse_dict['i'] = "..";
morse_dict['j'] = ".---";
morse_dict['k'] = "-.-";
morse_dict['l'] = ".-..";
morse_dict['m'] = "--";
morse_dict['n'] = "-.";
morse_dict['o'] = "---";
morse_dict['p'] = ".--.";
morse_dict['q'] = "--.-";
morse_dict['r'] = ".-.";
morse_dict['s'] = "...";
morse_dict['t'] = "-";
morse_dict['u'] = "..-";
morse_dict['v'] = "...-";
morse_dict['w'] = ".--";
morse_dict['x'] = "-..-";
morse_dict['y'] = "-.--";
morse_dict['z'] = "--..";

morse_dict['1'] = ".----";
morse_dict['2'] = "..---";
morse_dict['3'] = "...--";
morse_dict['4'] = "....-";
morse_dict['5'] = ".....";
morse_dict['6'] = "-....";
morse_dict['7'] = "--...";
morse_dict['8'] = "---..";
morse_dict['9'] = "----.";
morse_dict['0'] = "-----";

def dah():
    GPIO.output(MORSE_PIN, True)
    print(DAH),
    time.sleep(DAH_DURATION)
    GPIO.output(MORSE_PIN, False)
    time.sleep(SPACE_DURATION)

def dit():
    GPIO.output(MORSE_PIN, True)
    print(DIT),    
    time.sleep(DIT_DURATION)
    GPIO.output(MORSE_PIN, False)
    time.sleep(SPACE_DURATION)

def sendChar(stringOfDahDits):
    for d in stringOfDahDits:
        if d == DAH:
            dah()
        else:
            dit()
    #print END_CHAR,

def sendWord(sWord):
    sWord = sWord.lower()
    for schar in sWord:
        dchar = morse_dict.get(schar,':')
        if dchar != ':':
            sendChar(dchar)
    print END_WORD

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MORSE_PIN,GPIO.OUT)

sendWord("coderdojo")

GPIO.cleanup()
