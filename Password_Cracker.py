'''
Andrew Perreault
CSC371L Lab Cybersecurity
Python Password Cracking
Canisius College Computer Science

'''
import zipfile
import os
import time
from itertools import product

'''
This is the fuction which will open a dictionary file.
It simply opens and returns the opened file.
Uses a try except block to make sure the file opening doesn't fail
'''
def open_dict_file():
    #function returns type file
    print()
    while True:
        inp = input("Type dictionary file name: ")
        try:
            dictFile = open(inp)
            print("Opening file of name:", inp)
            return dictFile
        except:
            print("Invalid file name. Try again.")

'''
This is a function which opens a zip folder.
The idea is we have a zip folder which contains password protected files
which are then to be cracked by our python cracker.

'''
def open_zip_file():
    #function returns zipFile name
    print()
    while True:
        inp = input("Type Zip with locked files: ")
        try:
            zipr = zipfile.ZipFile(inp,'r') 
            print("Opening zipFile with name:", inp)
            return zipr
        except:
            print("Invalid zip file name. Try again.")


'''
This function runs the brute force attack.
Essentially, it is looking for the password needed to extract all these files. W
Since a "Bad Password" is an error...We need a try:, except: block to make sure if we see a bad password error, we should try another one.
Once the correct password hits, we print out the pw, and the time it took to guess it.
'''
def brute_force_attack(zf):

    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    
    st = time.process_time() #get start time
    for i in range(1,9): #loop which goes from 1-8 ascii chars
        for x in product(ascii_lowercase, repeat=i):
            pw = ''.join(x) #creates pw string
            try:
                zf.extractall(pwd = bytes(pw, 'utf-8')) #tries this password
                fin = time.process_time() #if pw didn't error, we get the time it finished at
                print(pw, "was the correct password") 
                print("Answer found in", fin - st, "seconds") #start time - fin time = total process time (in seconds).
                return True
            except:
                #if you want ( for testing ) you could include a print statement here...however it heavily increses time...
                None
    print("Password not found using 8 lowercase ascii chars.")
    return False

'''
This function runs a dictionary attack.
The dictionary file is a file with a password to try on each new line.
It repeatedly tests each word in the dictionary, until it runs out of words to try, or it opens successfully.
'''
def dictionary_attack(zf, df):
    
    st = time.process_time() #get start time
    for line in df:
        pw = line.strip() #takes the newline character off the end of the line.
        try:
            zf.extractall(pwd = bytes(pw, 'utf-8')) #tries this password
            fin = time.process_time() #if pw didn't error, we get the time it finished at
            print(pw, "was the correct password") 
            print("Answer found in", fin - st, "seconds") #start time - fin time = total process time (in seconds).
            return True
        except:
            None 
    print("The password was not found in the dictionary provided.")
    return False


'''
Main function which runs on a while loop to use the menu system.
Pretty standard format for a menu system

'''
def main():
    inp = ''

    #while the input isn't q we loop. First block defines main menu system
    while inp != 'q' and inp != 'Q':
        print("Welcome to the Python Password Cracker, please pick an option below")
        print("1. Brute Force Crack")
        print("2. Dictionary Attack")
        print("3. Both")
        print("Type q to quit.")
        print()
        inp = input("Please choose an option: ")
        print()

        #This block now checks the input and execute it. If input is invalid, it tells the user
        if inp == "1":
            zf = open_zip_file()
            brute_force_attack(zf) #will run brute force attack
            zf.close()
        elif inp == "2":
            zf = open_zip_file()
            df = open_dict_file()
            dictionary_attack(zf, df) #will run dictionary attack function 
            zf.close()
            df.close()
        elif inp == "3":
            zf = open_zip_file()
            df = open_dict_file()
            if dictionary_attack(zf,df) == False:
                brute_force_attack(zf)
            df.close()
            zf.close()
        elif inp != 'q' and inp !='Q':
            print("Sorry that is not a valid input!") #prints this then a new line if input is invalid
            print()


main()
