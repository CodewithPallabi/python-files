#Modules in python such as pyjokes,pytttsx3,dhjango,flask,matplotlib,seaborn,pandas,numpy,scipy,sklearn and lot more.(there are 2 types of modules in python built-in modules and external modules)
#to import a module we use our code terminal and install the module using pip command and then we can import the module in our code and use its functions and methods.

import pyttsx3 #pyttsx3 is a text to speech conversion library in python. It is used to convert text to speech in python.

jarvis = pyttsx3.init()
jarvis.say("Hello, I am Jarvis. How can I help you?")
jarvis.runAndWait()