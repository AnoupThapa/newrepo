# script to generate a file for storing data from the posner test run in arduino:

#written by Andre Maia Chagas 24.06.2013
#contact: openeuroscience(at)gmail.com
#distributed under Creative Commons Attribution-ShareAlike 3.0 Unported License.

#this script opens the serial port and reads data coming from an arduino UNO.
#it also creates a folder and a file to store the read data, in case they don’t
#exist.

#import necessary libraries:
import os #library that enables system operations
import datetime #library to get the current date
import serial #import library to read/write serial port

#serial port address
portName=”/dev/ttyACM1″
#check to see if there are any devices connected to the serial port:
if os.path.exists(portName):
#create the serial comm object (first par is the serial port and the second,
#the baud rate, in this case 115200 bits per second)
ser = serial.Serial(portName, 115200)
serFlag=1
else:
serFlag=0
print(“no serial devices connected!”)
print(“continuing without serial communication \n”)

#get the current date
tmpNow=str(datetime.datetime.now())

#path of the file to open
folderPath=”/home/andre/Documents/code/Posner_test_micros/test/”

#set the subject name
subjectName=’test1′
#set the name of the file
print tmpNow[0:10]+”_”+subjectName+”.txt”
fileName=tmpNow[0:10]+”_”+subjectName+”.txt”
print fileName

#check to see if the folder where you want to create
#the file exists. if it doesn’t exist, create it:
if not os.path.exists(folderPath):
os.makedirs(folderPath)

#create/open file in the specified folder in append mode:
newFile=open(folderPath+fileName,”a+”)

#write the date and the subject name at the beggining of the appended part
newFile.write(tmpNow[0:19]+”_”+subjectName+” \n”)

#if there is a serial device connected:
if serFlag==1:
ardCheck=0
#write one byte to the arduino
ser.write(“1″)
#wait for a specific signal from the arduino
while ardCheck<0:
ardCheck=ser.readline(1)
#now that one received the signal from the arduino,
#reset the “ardCheck” flag
ardCheck=0
print “device connected”
#now make python read data undefinetly untill a “break” command is called:
while True:
tmpVar=ser.readline()
newFile.write(tmpVar+”\n”)
#if the termination flag “*999**” is found, send the break command
if tmpVar==”*999**\n”:
print “test done!”
break
else:
print “no serial port connected!”
newFile.write(“no serial port connected!”)

#Close the file
newFile.close()




