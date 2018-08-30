#Windows python3
# -*- coding: utf-8 -*-



import os

def sanitize(time_string):
    if '-' in  time_string:
        spliter = '-'
    elif '-' in time_string:
        spliter = ':'
    else:
        return(time_string)
    (m,s) = time_string.split(spliter)
    return(m + '.' + s)

james = []
julie = []
mikey = []
sarah = []
try:
    os.chdir('Resources')
    with open('james.txt') as f:
        james = f.readline().strip().split(',')
    with open ('julie.txt') as f:
        julie = f.readline().strip().split(',')
    with open('mikey.txt') as f:
        mikey = f.readline().strip().split(',')
    with open ('sarah.txt') as f:
        sarah = f.readline().strip().split(',')
except IOError:
    print('the file is missing')



print(sorted(set([sanitize(i) for i in james]))[0:3])
print(sorted(set([sanitize(i) for i in julie]))[0:3])
print(sorted(set([sanitize(i) for i in mikey]))[0:3])
print(sorted(set([sanitize(i) for i in sarah]))[0:3])
