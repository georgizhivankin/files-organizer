'''
Created on 16 May 2016

@author: Djgeorgie
'''
import threading

def printit():
    threading.Timer(1.0, printit).start()
    t = threading.Timer
    t.daemon = True
    print "Hello, World!"

printit()

print "Exiting..."

# continue with the rest of your code


 
