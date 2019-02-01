#!/usr/bin/env python3

from itertools import combinations
import os
from tqdm import tqdm
import re

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!',
              '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
              '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t']


def console():
    isDone = False
    draw()
    while isDone == False:
        result = int(input(
            "Pick an option\n[1] Create a normal wordlist\n[2] Create a unique wordlist\n[3] Help\n[4] Quit program\n>>> "))
        if result == 1:
            isFinished = False
            while isFinished == False:
                limit = int(input("How many passwords would you like in this wordlist? (Do not exceed 10,000,000): "))
                if limit > 10000000:
                    print('[-] Limit too high')
                else:
                    default_wordlist(limit)
                    isFinished = True
        elif result == 2:
            patterns = []
            wifi_name = raw_input("Wifi network name: ")
            while True:
                pattern = input("Input pattern of possible passwords, type 'done' when done: ")
                if pattern == 'done':
                    break
                else:
                    patterns.append(pattern)
                    continue
            print('[+] Preparing wordlist...')
            wordlistPrep(wifi_name, patterns)
            print('[+] Thank you for using WordGen!')
            isDone = True
        elif result == 3:
            help()

        elif result == 4:
            print('[+] Thank you for using WordGen!')
            isDone = True
        else:
            print("[-] Invalid option")


def default_wordlist(limit):
    with open(os.getcwd() + '/default-wordlist.txt', 'r') as file:
        listing = file.readlines()
        text = ''
        counter = 0
        for i in listing:
            if counter < limit:
                i = i.rstrip()
                i = i[:-1]
                i = i + '\n'
                text += i
                counter += 1
            else:
                break
    cwd = os.getcwd()
    dist = '/dist'
    path = cwd + dist
    try:
        os.mkdir(path)
        os.chdir(path)
        file = open(path + '/new-wordlist.txt', 'w')
        file.write(text)
        print('[+] Wordlist saved in ' + path + ' as new-wordlist.txt')
    except:
        os.chdir(path)
        file = open(path + '/default-wordlist.txt', 'w')
        file.write(text)
        print('[+] Wordlist saved in ' + path + ' as default-wordlist.txt')


def wordlistPrep(patterns):
    pass_counter = 0
    strings = ''
    text = ''

    for w in tqdm(patterns):
        pattern = re.compile(r'{}'.format(w))
        for x in list(combinations(characters, 5)):
            j = ''.join(x)
            strings += j
            pass_counter += 1

    listing = pattern.findall(strings)
    for i in listing:
        text += i + '\n'

    print("[+] Wordlist created")
    saveFile(text)


def saveFile(text):
    counter = 0
    cwd = os.getcwd()
    dist = '/dist'
    path = cwd + dist
    while True:
        try:
            os.mkdir(path)
            os.chdir(path)
            file = open(path + '/wordlist.txt', 'w')
            file.write(text)
            print('[+] Wordlist saved in ' + path + ' as wordlist.txt')
            break
        except:
            counter += 1
            path += counter


def draw():
    print("""
    *************************************************
    *                                               *
    *                  Welcome to                   *
    *                                               *
    *                    WordGen                    *
    *                                               *
    *************************************************
    """)


def help():
    print("""
    **************
    *            *
    *    Help    *
    *            *
    **************

    Limits:
    - This will show the amount of passwords in the wordlist
    - Ex. A limit of 100,000 would generate a wordlist with 100,000 passwords

    Patterns:
    - This gives the generated passwords structure, and you can give multiple patterns
    - Patterns must be inputted with keywords and periods
    - Ex. '....example...'
        - This gives a bunch of random passwords with random characters replacing the dots

    """)


console()