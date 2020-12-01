# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:19:28 2020

@author: susmitha.kancharla
"""


import time

d={}

def create(key,value,timeout=0):
    if key in d:
        print("Key already exist.")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Memory Limit > 1024 MB")
        else:
            print("Keyname not valid")
        
def read(key):
    if key not in d:
        print("Key not found in databse.")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("Key",key,"expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in d:
        print("Key not found in databse.")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("Key deleted")
            else:
                print("Key",key,"expired") 
        else:
            del d[key]
            print("Key deleted")

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Key not found in databse.") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Key",key,"expired") 
    else:
        if key not in d:
            print("Key not found in databse.")  
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
            
create("susmitha",10)
create("susmitha",5)
create("susmitha1",70,3600) 
read("susmitha")
read("susmitha1")
modify("susmitha",99)
delete("susmitha")


