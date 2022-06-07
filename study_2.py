#Variables and Methods

print "Variables and Methods"
print "\n"
text = "India is my country. I love my country."
print "Real text is " 
print text
print len(text)
print text.upper()
print text.lower()
print text.title()

name = "Aneesh"
age = 23

print "My name is "+name+" and i am "+str(age)+" years old"
age += 1

print "Next year my age will be "+str(age)

birth = 5
age += birth

print "After 5 years my age will be "+str(age)
print "\n"
#Functions

print "Starting Function"

def mydata(place, distance):
	name = "Aneesh"
 	age = 25
	print "My name is "+name+" and i am "+str(age)+" years old and i am from "+place+" which is "+str(distance)+" km away from here."

mydata("Kallara", 15) 

print "\nMaths"

def math(x,y):
	return x+y, x-y, x*y, x/y, x%y, x//y

print(math(6,3))

print "\nConditional Statements"
def condition(age):
	if age >= 18:
		return "He is an adult"
	else:
		return "He is not an adult"

print(condition(19))

#print("Sentence split and join")
#sentence = "The way to get started is to quit talking and begin doing"
#print(sentence.split())
#sentence_spit = sentence.split()
#print(' '.join(sentence.split()))
#print('\n'.join(sentence.split()))

print "\n Vishnu R Nair"


