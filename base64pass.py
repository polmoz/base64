#!/usr/bin/python

__author__ = 'mmaslows'

import base64

def base64pass_gen():
    usr_name = raw_input("What's your username? >>> ")
    usr_pass = raw_input("What's your password to be converted? >>> ")
    base64_usr_pass = base64.b64encode(str(usr_name)+":"+str(usr_pass))
    print "\n"
    print "Your converted (base64) password is: " + base64_usr_pass
    print "\n"

if __name__ == '__main__':
    base64pass_gen()
