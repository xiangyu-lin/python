#!/bin/python
#
2018-01-31 Wed


2018-01-30 Tue
import sys
    def readline(filename):
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]


class SchoolMember():
    def _init__(self,name,age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name
    def tell(self):
        print 'Name:"%s" Age:"%s"' % (self.name,self.age),
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember._init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'salary: "%d"' % self.salary
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember._init__(self,name,age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'marks: ""%d"' % self.marks
s = Student('Swaroop',22,75)
t = Teacher('Mrs. Shrividya', 40, 30000)
print

members = [t,s]
for i in members:
    i.tell()



#
class Person():
    '''Represents a person.'''
    population = 0
    def __init__(self,name):
        self.name = name
        print '(Initialized %s)' % self.name
        Person.population += 1
    def __del__(self):
        '''I am dying.'''
        print '%s say bye.''' % self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population
    def sayHi(self):
        print 'hi , my name is %s' % self.name
    def howMany(self):
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d person here.' % Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

class Person():
    def sayHi(self):
        print 'Hello,how are you?'

class Person():
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print 'Hello my name is', self.name


class FirstClass():
    spam = 30
    def display(self):
        print self.spam

x = FirstClass()
x.display()

2018-01-29 Mon
#
class SchoolMember:
    '''Represent any SchoolMember.'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % (self.name,self.name)

class Teacher(SchoolMember):
    """Represent a Teacher."""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "%d"' self.salary

class Student(SchoolMember):
    '''Represents a Student'''
    def SchoolMember.__init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.marks



#
class Person:
    '''Represents a Person.'''
    population = 0

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializes %s)' % self.name
        #when this persion is created,he/she
        #adds to the population
        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye' %self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.',Person.population

    def sayhi(self):
        '''Greeting by the persion.

        really,that's all it does.'''
        print 'Hi my name is %s.' % self.name

    def howmany(self):
        '''print the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population

Swaroop = Person('Swaroop')
Swaroop.sayhi()
Swaroop.howmany()

kalam = Person('Abdul kalam')
kalam.sayhi()
kalam.howmany()

Swaroop.sayhi()
Swaroop.howmany()


#
class Person:
    def __init__(self,name):
        self.name = name
    def sayhi(self):
        print 'hello,my name is',self.name
p = Person('Swaroop')
p.sayhi

#
class Person:
    def sayhi(self):
        print 'Hello,how are you?'

p = Person()
p.sayhi()

#!/bin/python backup v3
import os
import time
#1.The files and directories to be backed up are specified in a list.
source = ['/tmp/swaroop/','/home/xylin/working/']
#2.The backup must be stored in a mian backup directory.
note = raw_input('give update some note:')
target_dir = '/tmp/backup/' + time.strftime('%Y%m%d')   #remember to change this to want you will be using
#3.The files are backup into a zip file.
#4.The name of the zip archive is the current data and time
target = target_dir + os.sep + time.strftime('%H%M%S') + note + '.zip'
#5.We use the zip command (in Unix/linux) to put the file in a zip archive
zip_command = "zip -qr '%s' %s" % (target,' '.join(source))
#run backup
if not os.path.exists(target_dir):
    os.mkdir(target_dir) #make directory
    print 'Successfully created directory',target_dir
if os.system(zip_command) == 0:
    print 'Successful backup to',target
else:
    print 'backup failed'

#!/bin/python backup v2
import os
import time
#1.The files and directories to be backed up are specified in a list.
source = ['/tmp/swaroop/','/home/xylin/working/']
#2.The backup must be stored in a mian backup directory.
target_dir = '/tmp/backup/' + time.strftime('%Y%m%d')  #remember to change this to want you will be using
#3.The files are backup into a zip file.
#4.The name of the zip archive is the current data and time
target = target_dir + os.sep + time.strftime('%H%M%S') + '.zip'
#5.We use the zip command (in Unix/linux) to put the file in a zip archive
zip_command = "zip -qr '%s' %s" % (target,' '.join(source))
#run backup
if not os.path.exists(target_dir):
    os.mkdir(target_dir) #make directory
    print 'Successfully created directory',target_dir
if os.system(zip_command) == 0:
    print 'Successful backup to',target
else:
    print 'backup failed'


#!/bin/python backup v1
import os
import time
#1.The files and directories to be backed up are specified in a list.
source = ['/tmp/swaroop/','/home/xylin/working/']
#2.The backup must be stored in a mian backup directory.
target_dir = '/tmp/backup/backup' #remember to change this to want you will be using
#3.The files are backup into a zip file.
#4.The name of the zip archive is the current data and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
#5.We use the zip command (in Unix/linux) to put the file in a zip archive
zip_command = "zip -qr '%s' %s" % (target,' '.join(source))
#run backup
if os.system(zip_command) == 0:
    print 'Successful backup to',target
else:
    print 'backup failed'
#

name = 'Swaroop'  #this is a string object
if name.startswith('Swa'):
    print 'Yes,the string startswith "Swa"'
if a in name:
    print 'yes,is contains the string "a"'
if name.find('war') != -1:
    print 'yes,it contains the string "war"'
delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print delimiter.join(mylist)

#
shoplist = ['apple','mango','carrot','banana']
#indexing or 'Subscription' opreation
print 'Item 0 is',shoplist[0]
print 'Item 1 is',shoplist[1]
print 'Item 2 is',shoplist[2]
print 'Item 3 is',shoplist[3]
print 'Item -1 is',shoplist[-1]
print 'Item -2 is',shoplist[-2]

#Slicing on a list
print 'Item 1 to 3 is',shoplist[1:3]
print 'Item 2 to end',shoplist[2:]
print 'Item 1 to -1 is',shoplist[1:-1]
print 'Item start to end is',shoplist[:]

#Slicing on a string
name = 'Swaroop'
print 'characters 1 to 3 is',name[1:3]
print 'characters 2 to end is',name[2:]
print 'characters 1 to -1 is'name[1:-1]
print 'characters start to end is',name[:]

#
#'ab' is short for 'a'ddress'b'ook
ab = {  'Swaroop'   :   'Swaroopch@qq.com',
        'Larry'     :   'Larry@qq.com'
        'Matsumoto' :   'Matsumoto@163.com'
        'goldendog' :   'goldendog@qq.com'
     }
print "Swaroop's address is %s" %s ab['Swaroop']
#Adding a key/value pair
ab['beigou'] = 'guido@python.org'
#delete a key/value pair
del ab['goldendog']

print '\nThere are %d contactd in the address-book\n' % len(ab)
for name,address in ab.items():
    print 'contact %s at %s' % (name,address)
if 'guido' in ab: # OR ab.has_key('guido')
    print "\nguido's address is %s" % ab['guido']

#
age = '22.3'
name = 'Swaroop'
print '%s is %d years old' % (name,float(age))

#
zoo = ('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)

new_zoo = ('mokey','dolphin',zoo)
print 'Number of in new_zoo is',len(new_zoo)
print 'All animals in new_zoo are',new_zoo
print 'animals brought from old are',new_zoo[2]
print 'Last animals brought from old zoo is',new_zoo[2][2]
#
#This is my shopping list
shoplist = ['apple','mango','carrot','banana']
print 'I have',len(shoplist),'items to purchase.'
print 'These items are:',
for i in shoplist:
    print i
print '\n I also have to buy rice.'
shoplist.append('rice')
print 'My shoplist is now:',shoplist

print 'I will sort my list now\n'
shoplist.sorted()
print 'Sorted shoplist is:',shoplist

print 'the first item i will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shoplist is now',shoplist

#
def sayhi():
    print 'Hi,this is mymodule speaking.'

version = '0.1'
#End of mymodule.py

#
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another modules'

#
import sys

print 'The command line argument are:'
for i in sys.argv:
    print i

print '\n \nThe Python PATH is :',sys.path,'\n'
#
def printMax(x,y):
    '''Print the maximum of two numbers.

    the two num must be int'''
    x = int(x) #convert to integers,if possible
    y = int(y)
    if x > y:
        print x,'is max!'
    else:
        print y,'is maximum!'

printMax(3,5)
print printMax.__doc__
