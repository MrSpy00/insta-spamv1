# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
  _           _                                        
 (_)_ __  ___| |_ __ _       ___ _ __   __ _ _ __ ___  
 | | '_ \/ __| __/ _` |_____/ __| '_ \ / _` | '_ ` _ \ 
 | | | | \__ \ || (_| |_____\__ \ |_) | (_| | | | | | |
 |_|_| |_|___/\__\__,_|     |___/ .__/ \__,_|_| |_| |_|
                                |_|                    v1
                                (_)                      """

youtube_urls = [
    "Github => https://github.com/MrSpy00/",
    "Project => https://github.com/MrSpy00?tab=repositories ",
    "Please don't forget to star :)",
    "It's Beta Version...",
    "Projeler => https://github.com/MrSpy00?tab=repositories ",
    "Yıldız atmayı unutmayın :)"
    "Beta sürümüdür..."

    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Made by hack6m"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> İyi Şikayetler..   ~   Good Complaints..")
    print ("\n", "-> Notes:\n    " + choice(youtube_urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)

