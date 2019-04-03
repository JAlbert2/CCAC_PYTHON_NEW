#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:36:47 2019

Jonah Albert
4/2/19
Python 1-DAT 119-Spring 2019
Week 8 Homework code
To do list application
"""

print('Begin\n')
#Initalizing empty lists
to_do = []
done = []

def view(to_do, done):
    print("To do: ")
    #Print if list is empty
    if(len(to_do) == 0):
        print('Nothing to do. Hooray‽')
    else: #Print all items in to do list
        for num in range(len(to_do)):
            print(to_do[num])
    print('\nDone: ')
    #Print is done list is empty
    if(len(done) == 0):
        print('Nothing is done. Get to work.')
    else: #Print all items in done list
        for num in range(len(done)):
            print(done[num])

    input("Press enter when done viewing")
    main(to_do, done)#Return to menu


def add(to_do, done):
    usr_add = input('What would you like to add? ')
    to_do.append(usr_add)#Add what the user entered to the to do list
    print(usr_add,"has been added to the to do list.")#Notify user of what was entered
    main(to_do, done)#Return to menu


def mark_done(to_do, done):
    for num in range(len(to_do)):#Prints all items in to do list with user numbers in front
        print(num+1,') ',to_do[num],sep='')
    usr_done = input("Enter a number of which you would like to mark as done(0 for cancel): ")
    done_int = 0#Initalized due to UnboundLocalError
    try: #Try except block found in book code 7-4
        done_int = int(usr_done[0])
    except ValueError:#Runs if user did not enter a number
        print("You didn't enter a valid number.\n")
        mark_done(to_do, done)#Restart the mark_done function

    if(done_int == 0):#Escape case
        main(to_do, done)#Return to menu
    elif(done_int > len(to_do) or done_int < 0):#User enters a negative or over the length of list
        print("You didn't enter a valid number.\n")
        mark_done(to_do, done)#Return to menu
    else:
        item = to_do[done_int-1]#Converts user number to python and puts the string into a holder
        done.append(item)#Adds the holder item to the done list
        to_do.remove(item)#Removes the same item from the to do list
        print(item,'was moved to the done list.')#Notifies user of actions

    if(done_int != 0):#Added to ensure that menu does not re-appear when trying to quit
        main(to_do, done)#Return to menu


def exit_app(to_do, done):
    usr_end = input("Are you sure you want to quit?(Nothing is saved)[y/n] ")
    usr_end = usr_end.lower()#Convers the user's answer to lower case

    if ('n' in usr_end):#If the user enters a 'n' anywhere, return to menu
        main(to_do, done)#Return to menu


def main(to_do, done):
    choice = 0#Initalized due to UnboundLocalError
    loop = True#Runs the try block the first time
    print("\nMenu")
    print("1) View to do/done lists")
    print("2) Add on to the to do list")
    print("3) Mark something done")
    print("4) Exit the application")
    usr_input = input("Enter a number to enter a menu: ")
    while (loop):
        try:#Try except block found in book code 7-4
            choice = int(usr_input[0])#Takes the first item in the string and converts to an int
            #Solves my float error from class
            loop = False#If a valid input is entered, the loop will not run again
        except ValueError:#Runs if user did not enter a number
            print("You didn't enter a valid number.")
            #main(to_do, done)#Restart the main function

    if(choice == 1):
        #print('\n')#No input function, adds new line for display formatting
        view(to_do, done)#Calls the view function
    elif(choice == 2):
        add(to_do, done)#Calls the add function
    elif(choice == 3):
        mark_done(to_do, done)#Calls the mark_done function
    elif(choice == 4):
        exit_app(to_do, done)#Calls the exit function
    else:
        print("You didn't enter a valid number.")
        main(to_do, done)#Restart the menu


if __name__ == "__main__":
    main(to_do, done)
print('\nEnd')