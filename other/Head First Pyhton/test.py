#!/bin/python3
#

#类继承
class NameList(list):
    def __init__(self,aname):
        list.__init__([])
        self.name = aname
johnny = NameList("John Paul Jones")


class Athletelist(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(i) for i in self]))[0:3])

#类
def sanitize(time_string):	#fuction　把'-' ':'　转换成'.'　保持格式一致
	if '-' in  time_string:
		spliter	= '-'
	elif ':' in time_string:
		spliter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(spliter)
	return(mins + '.' + secs)

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(i) for i in self.times]))[0:3])
    def add_time(self,add_time_value):
        self.times.append(add_time_value)
    def add_times(self,add_time_list):
        self.times.extend(add_time_list)


def got_data(filename):
	try:
		with open(filename,'r') as f:
			data = f.readline().strip('\n')
			datal = (data.strip('').split(','))
			#datad = {'Name':datal.pop(0),'Date':datal.pop(0),'Times':str(sorted(set([sanitize(i) for i in datal]))[0:3])}
			return(Athlete(datal.pop(0),datal.pop(0),datal))

	except IOError as err:
		print('IOError' + str(err))
		return(None)

import os
os.chdir('chapter6')
sarahd = got_data('sarah2.txt')
#print(sarahd['Name'] + 'fastest times is：' + sarahd['Times'])
print(sarahd.name,sarahd.dob,sarahd.times)

#
class Athlete:
    def __init__(self,value=0):
        # the code to Initialized a "Athlete" object.
        self.thing = value
    def how_big(self):
        return(len(self.thing))
d = Athlete("Holy grail")
d.how_big()

#--
a = Athlete()
b = Athlete()
c = Athlete()
d = Athlete()

class Athlete:
   def __init__(self,a_name,a_dob=None,a_times=[]):
            self.name = a_name
            self.dob = a_dob
            self.times = a_times
   def top3(self):
   		return(sorted(set([sanitize(i) for i in self.times])))


def sanitize(time_string):	#fuction　把'-' ':'　转换成'.'　保持格式一致
	if '-' in  time_string:
		spliter	= '-'
	elif ':' in time_string:
		spliter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(spliter)
	return(mins + '.' + secs)

def got_data(filename):
	try: song
		with open(filename,'r') as f:
			data = f.readline().strip('\n')
			datal = (data.strip('').split(','))
			#datad = {'Name':datal.pop(0),'Date':datal.pop(0),'Times':str(sorted(set([sanitize(i) for i in datal]))[0:3])}
			return(Athlete(datal.pop(0),datal.pop(0),datal))

	except IOError as err:
		print('IOError' + str(err))
		return(None)

import os
os.chdir('chapter6')


sarahd = got_data('sarah2.txt')
#print(sarahd['Name'] + 'fastest times is：' + sarahd['Times'])
print(sarahd.name)#,sarahd.self.dob,sarahd.self.times)
'''
class Athlete:
   def __init__(self,a_name,a_dob=None,a_times=[]):
            self.name = a_name
            self.dob = a_dob
            self.times = a_times

james = Athlete('James Jones')
sarah = Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
'''


'''----字典

def sanitize(time_string):	#fuction　把'-' ':'　转换成'.'　保持格式一致
	if '-' in  time_string:
		spliter	= '-'
	elif ':' in time_string:
		spliter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(spliter)
	return(mins + '.' + secs)

def got_data(filename):
	try:
		with open(filename,'r') as f:
			data = f.readline().strip('\n')
			datal = (data.strip('').split(','))
			return({'Name':datal.pop(0),'Date':datal.pop(0),'Times':str(sorted(set([sanitize(i) for i in datal]))[0:3])})

	except IOError as err:
		print('IOError' + str(err))
		return(None)

import os
os.chdir('chapter6')


sarahd = got_data('sarah2.txt')
print(sarahd['Name'] + 'fastest times is：' + sarahd['Times'])




#sarah = got_data('sarah2.txt')
#sarahd = {'Name':sarah.pop(0),'Date':sarah.pop(0)}
#print(sarahd['Name'] + "'s fastest time is:" + str(sorted(list(set([sanitize(i) for i in sarah])))[0:3]))

'''




'''
def sanitize(time_string):	#fuction　把'-' ':'　转换成'.'　保持格式一致
	if '-' in  time_string:
		spliter	= '-'
	elif ':' in time_string:
		spliter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(spliter)
	return(mins + '.' + secs)

def got_data(filename):
	try:
		with open(filename,'r') as f:
			data = f.readline().strip('\n')
			return(data.strip('').split(','))
	except IOError as err:
		print('IOError' + str(err))
		return(None)

import os
os.chdir('chapter6')


sarah = got_data('sarah2.txt')
sarahd = {'Name':sarah.pop(0),'Date':sarah.pop(0)}
print(sarahd['Name'] + "'s fastest time is:" + str(sorted(list(set([sanitize(i) for i in sarah])))[0:3]))
'''

'''
sarah = got_data('sarah2.txt')
(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
print(sarah_name + "'s fastest time are:" + str(sorted(list(set([sanitize(i) for i in sarah])))[0:3]))
'''




'''
cleese['Birthplace'] = "Weston-super-Mare,North Somerest,England"
palin['Birthplace'] = "Broomhill,Sheffield,England"
cleese['Occupations'][1]
palin['Name']
palin = {'Name':'Michael Palin','Occupations':['comedian','actor','writer','tv']}
cleese['Occupations'] = ['actor','comedian','writer','film producer']
cleese['Name'] = 'John Cleese'
type(palin)
cleese = {}
palin = dict()
'''

#--------------------------------------------5
'''
def sanitize(time_string):	#fuction　把'-' ':'　转换成'.'　保持格式一致
	if '-' in  time_string:
		spliter	= '-'
	elif ':' in time_string:
		spliter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(spliter)
	return(mins + '.' + secs)

import os
os.chdir('chapter5')


def got_data(filename):
	try:
		with open(filename,'r') as f:
			data = f.readline().strip('\n')
			return(data.strip('').split(','))
	except IOError as err:
		print('IOError' + str(err))
		return(None)

jamesl = got_data('james.txt')
juliel = got_data('julie.txt')
mikeyl = got_data('mikey.txt')
sarahl = got_data('sarah.txt')

#推导列表
print(sorted(list(set([sanitize(i) for i in jamesl]))[0:3]))
print(sorted(list(set([sanitize(i) for i in juliel]))[0:3]))
print(sorted(list(set([sanitize(i) for i in mikeyl]))[0:3]))
print(sorted(list(set([sanitize(i) for i in sarahl]))[0:3]))



clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for i in jamesl:
	clean_james.append(sanitize(i))
for i in juliel:
	clean_julie.append(sanitize(i))
for i in mikeyl:
	clean_mikey.append(sanitize(i))
for i in sarahl:
	clean_sarah.append(sanitize(i))



#dist = set(clean_james)
#print(list(dist)[0:3])



# 去重打印前三项
unique_jame = []
for i in clean_james:
	if i not in unique_jame:
		unique_jame.append(i)

print(unique_jame[0:3])


#james.txt  julie.txt  mikey.txt  sarah.txt


import sys
def printl(the_list,indent=False,level=0,output=sys.stdout):
    for i in the_list:
        if isinstance(i,list):
            printl(i,indent,level+1,output)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=output)
            print(i,file=output)

import os

man = []
other = []

try:
	with open('sketch.txt') as data:
		for i in data:
			try:
				(role,spoken) = i.split(':',1)
				spoken = spoken.strip()
				if role == 'Man':
					man.append(spoken)
				else:
					other.append(spoken)
			except ValueError:
				pass

except IOError:
	print('the file do not exists')

import pickle
try:
	with open('man.pickle','wb') as outman,open('other.pinkle','wb') as outother:
		pickle.dump(man,outman)
		pickle.dump(other,outother)
except IOError as err:
	print('IOError' + str(err))
except pickle.PickleError as perr:
	print('pickleError' + str(perr))



newman = []
try:
	with open('man.pickle','rb') as outnewman:
		newman = pickle.load(outnewman)
except IOError as err:
	print('IOError' + str(err))
except pinkle.PickleError as perr:
	print('PickleError' + str(perr))

printl(newman)


try:
	with open('man.out','w') as outman,open('other.out','w') as outother:
		printl(man,indent=True,output=outman)
		printl(other,indent=True,output=outother)
except IOError as err:
	print('IOError' + str(err))



import sys

movies = [
    "The holy grail","Terry Jones & Terry Gilliam",
        ["Graham Chapam",
            ["Michael Palin","Jhon","Cleese","Terry Gilliam","Eric Idle","Terry Jones"]],"The life of brain","the meaning of life"]

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
'''
