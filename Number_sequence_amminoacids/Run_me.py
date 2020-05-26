# -*- coding: utf-8 -*-
"""
This script takes an .txt sequence and assigns a number to the amminoacid
i.e. MFNK becomes 1-M 2-F 3-N 4-K
i.e. MetPheLysAsn 1-Met 2-Phe 3-Lys 4-Asn
"""

#gets path where sequence.txt is stored (inside the software folder) 
#this samse path will be used to save the NumberedSequence.txt
import os
pathCWD = os.getcwd()
#where my input sequence.txt file is
pathInp = pathCWD + "\\sequence.txt" 
#where my numbered output NumberedSequence.txt file is
pathOut = pathCWD + "\\NumberedSequence.txt" 

#returns true if character is an upper case and false if lower case
def check_upper(c):
    if c >= 'A' and c <= 'Z':
        return True
    else:
        return False
    
def sequence():
    
    #opens sequence.txt (input)
    i  = open(pathInp, "r") 
    #creates file where numbered sequence will be saved (output)
    o = open(pathOut,"w+")

    #counts in the while loop
    count = 0
    
    #use while loop to read all file characters
    while 1: 
        # read by character 
        char = i.read(1)           
        if not char:  
            break
        #check if it is an upper case, if function is true than block will be executed
        if check_upper(char):
            count = count +1
            o.write("\n")
            o.write("%d-" % count)
        #keep writing characters
        o.write(char)
                
          
        
    i.close() 
    o.close()

sequence()

