# -*- coding: utf-8 -*-
i = 0
numbers = []
#while i < 6:
for i in range(0, 6):
    print "at the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "numbers now: ", numbers
    print "at the bottom i is %d" % i


print "the numbers: "

for num in numbers:
    print num


#the_count = [1, 2, 3, 4, 5]
#fruits = ['apples', 'oranges', 'pears', 'apricots']
#change = [1, 'pannies', 2, 'dims', 3, 'quarters']
##this
#for number in the_count:
#    print "this is conunt %d" % number
#
# #same
#for fruit in fruits:
#    print "a fruit of type: %s" % fruit
#
##also
##notice
#for i in change:
#    print "i got %r" % i
#    
##we
#elements = []
#
##then
#for i in range(0, 6):
#    print "adding %d to the list." % i
#    #append
#    elements.append(i)
#    
##now
#for i in elements:
#    print "element was: %d" % i 
#



#print "you enter a dark room with two doors. do you go through door #1 or door #2?"
#door = raw_input("> ")
#
#if door == "1":
#    print "there's a giant bear here eating a cheese cake. what do you do?"
#    print "1. take the cake."
#    print "2. scream at the bear."
#
#    bear = raw_input("> ")
#
#    if bear == "1":
#        print "the bear eats your face off. good job!"
#    elif bear == "2":
#        print "the bear eats your legs off. good job!"
#    else:
#        print "well, doing %s is probably better. bear run away." % bear
#
#elif door == "2":
#    print "you stare into the endless abyss at cthulhu's retina."
#    print "1. blueberries."
#    print "2. yellow jacket clothepins."
#    print "3. understanding revolvers yelling melodies."
#
#    insanity = raw_input("> ")
#
#    if insanity == "1" or insanity =="2":
#        print "your body survives powered by a mind of jello. good job!"
#    else:
#        print "the insanity rots your eyes into a pool of muck. good job!"
#
#else:
#    print "you stumble around and fall on a knife and die. good job!"
#



#people = 30
#cars = 15
#buses = 15
#
#if cars > people:
#    print "we should take the cars."
#elif cars < people:
#    print "we should not take the cars."
#else:
#    print "we cant decide."
#
#if buses > cars:
#    print "that's too many buses."
#elif buses < cars:
#    print "maybe we could take the buses."
#else:
#    print "we still can't decide."
#
#if people > buses:
#    print "alright, let's just take the buses."
#else:
#    print "fine, let's stay home then."







#people = 20
#cats = 30
#dogs = 15
#
#if people < cats:
#    print "too many cats! the world is doomed!"
#
#if people > cats:
#    print "not many cats! the world is saved!"
#
#if people < dogs:
#    print "the world is drooled on!"
#
#if people > dogs:
#    print "the world is dry!"
#
#
#dogs += 5
#
#if people >= dogs:
#    print "people are greater than or equal to dogs."
#
#if people <= dogs:
#    print "people are less than or equal to dogs."
#
#
#if people == dogs:
#    print "people are dogs."
#


#def break_words(stuff):
#    """this function will break up words for us."""
#    words = stuff.split(' ')
#    return words
#
#def sort_words(words):
#    """sorts the words."""
#    return sorted(words)
#
#def print_first_word(words):
#    """prints the first word after popping it off."""
#    word = words.pop(0)
#    print word
#
#def print_last_word(words):
#    """prints the last word after popping it off."""
#    word = words.pop(-1)
#    print word
#
#def sort_sentence(sentence):
#    """takes in a full sentence and returns the sorted words."""
#    words = break_words(sentence)
#    return sort_words(words)
#
#def print_first_and_last(sentence):
#    """prints the first and last words of the sentence."""
#    words = break_words(sentence)
#    print_first_word(words)
#    print_last_word(words)
#
#def print_first_and_last_sorted(sentence):
#    """sorts the words then print the first and last one."""
#    words = sort_sentence(sentence)
#    print_first_word(words)
#    print_last_word(words)







#print "let's practice everything."
#print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#poem = """
#\tthe lovely world
#with logic so firmly planted
#cannot discern \n the needs of love
#nor comprehend passion from intuition
#and requires an expanation
#\n\t\twhere there is none.
#"""
#
#print "-----------"
#print poem
#print "-----------"
#
#
#five = 10 - 2 + 3 - 6
#print "this should be five: %s" % five
#
#def secret_formula(standard):
#    jelly_beans = standard * 500
#    jars = jelly_beans / 1000
#    crates = jars / 100
#    return jelly_beans, jars, crates
#
#
#start_point = 10000
#beans, jars, crates = secret_formula(start_point)
#
#print "with a starting point of: %d" % start_point
#print "we'd have %d beans, %d jars, %d crates." % (beans, jars, crates)
#
#start_point = start_point / 10
#
#print "we can also do that this way:"
#print "we'd have %d beans, %d jars, %d crates." % (beans, jars, crates)




#def add(a,b):
#    print "adding %d + %d" % (a, b)
#    return a + b
#
#def subtract(a, b):
#    print "subtracting %d - %d" % (a, b)
#    return a - b
#
#def multiply(a, b):
#    print "multiplying %d * %d" % (a, b)
#    return a * b
#
#def dividie(a, b):
#    print "dividing %d / %d" % (a, b)
#    return a / b
#
#print "let's do some math with just functions!"
#
#age = add(30, 5)
#height = subtract(78, 4)
#weight = multiply(90, 2)
#iq = dividie(100, 2)
#
#print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)
#
#
##
#print "here is the pazzle."
#
#what = add(age, subtract(height, multiply(weight, dividie(iq, 2))))
#
#print "that becomes: ", what, "can you do it by hand?"



#from sys import argv
#script, input_file = argv
#
#def print_all(f):
#    print f.read()
#
#def rewind(f):
#    f.seek(0)
#
#def print_a_line(line_count, f):
#    print line_count, f.readline()
#
#current_file = open(input_file)
#
#print "first let's print the whole file:\n"
#
#print_all(current_file)
##print current_file.read()
#
#print "now let's rewind, kind of like a tape."
#
#rewind(current_file)
#
#print "let's print three lines:"
#
#current_line = 1
#print_a_line(current_line, current_file)
#
#current_line = current_line + 1
#print_a_line(current_line, current_file)
#
#current_line = current_line + 1
#print_a_line(current_line, current_file)



#def cheese_and_crackers(cheese_count, boxex_of_crackers):
#    print "you have %d cheeses!" % cheese_count
#    print "you have %d boxes of cracers!" % boxex_of_crackers
#    print "man that's enaough for a party!"
#    print "get a blanket.\n"
#amount_of_cheese = int(raw_input("how much cheese?"))
#amount_of_crackers = int(raw_input("how many crackers?"))
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#print "we can just give the function numbers directly:"
#cheese_and_crackers(20, 30)
#
#
#print "or, we can use variables from our script:"
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#
#print "we can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)
#
#
#print "and we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
    
    


# this one is like your scripts with argv
#def print_two(*args):
#    arg1, arg2 = args
#    print "arg1: %r, arg2: %r" % (arg1, arg2)
#
##ok, that *args is actually pointless, we can just do this
#def print_two_again(arg1, arg2):
#    print "arg1: %r, arg2: %r" % (arg1, arg2)
#
##this just takes one argument
#def print_one(arg1):
#    print "arg: %r" % arg1
#
##this one takes no arguments
#def print_none():
#    print "i got nothing"
#
#print_two("zed", "shaw")
#print_two_again("zed", "shaw")
#print_one("first!")
#print_none()



#from sys import argv
#from os.path import exists
#
#script, from_file, to_file = argv
#
#print "copying from %s to %s" % (from_file, to_file)
#
#indata = open(from_file).read()#此时不用close
##input = open(from_file)
##indata = input.read()
#
#print "the input file is %d bytes long" % len(indata)
#
#print "does the output file exist? %r" % exists(to_file)
#print "ready, hit return to continue, ctrl-c to abort."
#raw_input("?")
#
#output = open(to_file, 'w')
#output.write(indata)
#
#print "alright, all done"
#
#output.close()
#input.close()






#from sys import argv
#
#script, filename = argv
#
#print "we're going to erase %r" % filename
#print "if you dont want that, hit CTRL-C(^C)."
#print "if you do want that, hit RETURN."
#
#raw_input("?")
#
#print "opening the file..."
#target = open(filename, 'w')
#
#print "truncating the file. good bye!"
#target.truncate()
#
#print "now im going to ask you for three lines."
#
#line1 = raw_input("line 1: ")
#line2 = raw_input("line 2: ")
#line3 = raw_input("line 3: ")
#
#print "im going to weite these to the file."
#
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#
#print "and finally, we close it."
#target.close()
#
#target = open(filename)
#print target.readline(5)





#from sys import argv
#
#script, filename = argv
#
#txt = open(filename)
#
#print "here's your file %r:" % filename
#print txt.read()
#
#print "type the filename again:"
#file_again = raw_input(">")
#
#txt_again = open(file_again)
#
#print txt_again.read()




#from sys import argv
#
#script, user_name = argv
#prompt = ">"
#
#print "hi %s, i'm the %s script." % (user_name, script)
#print "i'd like to ask you a few questions."
#print "do you like me %s?" % user_name
#likes = raw_input('>')
#
#print "where do you live %s?" % user_name
#lives = raw_input(prompt)
#
#print "what kind of computer do you have?"
#computer = raw_input(prompt)
#
#print """
#alright, so you said %r about liking me.
#you live in %r. not sure where that is.
#and you have a %r computer. nice
#""" % (likes, lives, computer)


#运行时先打开cmd，进入代码所在目录，输入：python xxx.py first second third 即可运行
#from sys import argv
#
#script, first, second, third = argv
#
#print "the script is called:", script
#print "your first variable is:", first
#print "your second variable is:", second
#print "you third variable is:", third