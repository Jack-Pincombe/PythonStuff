#!/usr/bin/env python

#script to open all of my usual morning browsers that I use
import webbrowser


print("Hello World!")


def load():
    webbrowser.open('https://outlook.live.com/owa/')
    webbrowser.open('https://www.facebook.com')
    webbrowser.open('https://eccouncil.learnondemand.net/User/Login?ReturnUrl=%2f')
    webbrowser.open('https://pymotw.com/3/')

if __name__ == '__main__':
    load()

    