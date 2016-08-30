#!/usr/bin/env python3.4

#Import urllib to use parse functions to encode and decode Url's
import urllib.parse

#Import sys to use argv attributes
import sys

########################
##      Banner        ##
########################
 
      ## ########  #### ######## ######## ##       ######## 
      ## ##     ##  ##       ##       ##  ##       ##       
      ## ##     ##  ##      ##       ##   ##       ##       
      ## ##     ##  ##     ##       ##    ##       ######   
##    ## ##     ##  ##    ##       ##     ##       ##       
##    ## ##     ##  ##   ##       ##      ##       ##       
 ######  ########  #### ######## ######## ######## ######## 

#CommandLine Options:
encode = "-e"
decode = "-d"
Help = "-h"

#Global Variables
Option = sys.argv[1]
ES = "\r\nEncoded String: \r\n"
DS = "\r\nDecoded String: \r\n"

#Functions
def helpmenu():
    print("""
========================================================================================================
#   _   _ ____  _       _____                     _             ____                     _             #
#  | | | |  _ \| |     | ____|_ __   ___ ___   __| | ___ _ __  |  _ \  ___  ___ ___   __| | ___ _ __   #
#  | | | | |_) | |     |  _| | '_ \ / __/ _ \ / _` |/ _ \ '__| | | | |/ _ \/ __/ _ \ / _` |/ _ \ '__|  #
#  | |_| |  _ <| |___  | |___| | | | (_| (_) | (_| |  __/ |    | |_| |  __/ (_| (_) | (_| |  __/ |     #
#   \___/|_| \_\_____| |_____|_| |_|\___\___/ \__,_|\___|_|    |____/ \___|\___\___/ \__,_|\___|_|     #
#                                                                                                      #
========================================================================================================

DESCRIPTION
        This is a simple tool used to either URL encode or URL decode a string.

COMMAND LINE OPTIONS
       -h          Display the Help Menu              

       -e          This option is used to URL encode a string.

       -d          This option is used to URL decode a string.

EXAMPLE USES
        1. EncDec.py -e https://www.test.com/
        
        2. EncDec.py -d https%3A%2F%2Fwww.test.com%2F
        
""")

def ecode(encDecValue):
    newValue = urllib.parse.quote_plus(encDecValue)
    print(ES)
    print(newValue,'\r\n')

def dcode(encDecValue):
    newValue = urllib.parse.unquote_plus(encDecValue)
    print(DS)
    print(newValue,'\r\n')

#Main code
if Option == encode:
    ecode(sys.argv[2])       
elif Option == decode:
    dcode(sys.argv[2])        
elif Option == Help:
    helpmenu()
else:
    print("Whoops, no encoded or decoded string was found. See help \"-h\" option and try again!!")
