from subprocess import call import speech_recognition as sr import serial
import RPi.GPIO as GPIO import os, time

# Initialize speech recognizer r = sr.Recognizer()

# Define GPIO pins led = 27
text = {} text1 = {}

# Set up GPIO warnings and mode GPIO.setwarnings(False) GPIO.setmode(GPIO.BCM)

# Set up GPIO pins as output GPIO.setup(led, GPIO.OUT) GPIO.setup(17, GPIO.OUT) GPIO.setup(22, GPIO.OUT) GPIO.setup(23, GPIO.OUT)

# Function to listen to microphone input def listen1():
with sr.Microphone(device_index = 2) as source: r.adjust_for_ambient_noise(source)
 

print("Say Something") audio = r.listen(source) print("got it")
return audio


# Function to recognize speech from audio input def voice(audio1):
try:
text1 = r.recognize_google(audio1) print("you said: " + text1)
return text1
except sr.UnknownValueError:
print("Google Speech Recognition could not understand") return 0
except sr.RequestError as e:
print("Could not request results from Google") return 0

# Function to process recognized speech commands def main(text):
print("you said: " + text)


# Commands for load one
if ('load one on' in text) or('load 1 on' in text) or ('load one ko chalu kar do' in text) or ('load 1 ko chalu kar do' in text) or ('load one on cheyi' in text) or ('load 1 on cheyi' in text):
GPIO.output(led, GPIO.HIGH) print("load1 on")
elif 'load one of' in text or 'load 1 of' in text or'load one ko band kar do' in text or'load 1 ko band kar do' in text or'load one of cheyi' in text or'load 1 of cheyi' in text:
GPIO.output(led, GPIO.LOW)
 

print("load1 Off")


# Commands for load two
if ('load two on' in text) or('load 2 on' in text) or ('load two ko chalu kar do' in text) or ('load 2 ko chalu kar do' in text) or ('load two on cheyi' in text) or ('load 2 on cheyi' in text):
GPIO.output(17, GPIO.HIGH)
print("load2 on")
elif 'load two of' in text or 'load 2 of' in text or'load two ko band kar do' in text or'load 2 ko band kar do' in text or'load two of cheyi' in text or'load 2 of cheyi' in text:
GPIO.output(17, GPIO.LOW)
print("load2 Off")


# Commands for load three
if ('load three on' in text) or('load 3 on' in text) or ('load three ko chalu kar do' in text) or ('load 3 ko chalu kar do' in text) or ('load three on cheyi' in text) or ('load 3 on cheyi' in text):
GPIO.output(22, GPIO.HIGH)
print("load3 on")
elif 'load three of' in text or 'load 3 of' in text or'load three ko band kar do' in text or'load 3 ko band kar do' in text or'load three of cheyi' in text or'load 3 of cheyi' in text:
GPIO.output(22, GPIO.LOW)
print("load3 Off")


# Commands for load four
if ('load four on' in text) or('load 4 on' in text) or ('load four ko chalu kar do' in text) or ('load 4 ko chalu kar do' in text) or ('load four on cheyi' in text) or ('load 4 on cheyi' in text):
GPIO.output(23, GPIO.HIGH)
print("load4 on")
elif 'load four of' in text or 'load 4 of' in text or'load four ko band kar do' in text
 

or'load 4 ko band kar do' in text or'load four of cheyi' in text or'load 4 of cheyi' in text:
GPIO.output(23, GPIO.LOW)
print("load4 Off")


# Commands for all loads
if ('loads on' in text) or ('loads ko chalu kar do' in text) or ('loads on cheyi' in text): GPIO.output(led, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH) GPIO.output(22, GPIO.HIGH) GPIO.output(23, GPIO.HIGH)
print("loads on")
elif 'loads of' in text or 'loads ko band kar do' in text or 'loads of cheyi' in text: GPIO.output(led, GPIO.LOW)
GPIO.output(17, GPIO.LOW) GPIO.output(22, GPIO.LOW) GPIO.output(23, GPIO.LOW)
print("loads Off") text = ""

# Main loop to continuously listen and process commands if  name	== ' main ':
while True:
audio1 = listen1()
text = str(voice(audio1)).lower() if 'google' in text:
main(text)
