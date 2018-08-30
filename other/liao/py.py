#Windows python3
# -*- coding: utf-8 -*-

鱼c论坛


movies = [
    "The holy grail","Terry Jones & Terry Gilliam",
        ["Graham Chapam",
            ["Michael Palin","Jhon","Cleese","Terry Gilliam","Eric Idle","Terry Jones"]],"The life of brain","the meaning of life"]
import nester
nester.printl(movies)



"""
import sys

def printl(the_list,indent=False,level=0,output=sys.stdout):
    for i in the_list:
        if isinstance(i,list):
            printl(i,indent,level+1,output)
        else:
            if indent==True:
                for tab_stop in range(level):
                    print("\t",end='',file=output)
            print(i,file=output)
printl(movies,indent=True)
"""
