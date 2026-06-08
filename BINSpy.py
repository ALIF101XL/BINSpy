#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################
# BINSpy | People tracker on the Internet #
###########################################

from core.utils import utils
from core.BINSpy import BINSpy
from core.db import Database
from time import sleep
try:
    import flask
    import flask_socketio
    import os
except:
    utils.Go("\t\nPlease install requirements.txt libraries, you can do it executing:")  #
    utils.Go("\t\npip install -r requirements.txt") 
    
# We generalize the main class of <BINSpy>
trackPeople = BINSpy()

# call class database
generateData = Database()
if generateData.firstTime:
    utils.Go("\033[H\033[J")         
    utils.Go("\t" + utils.Color['white'] + "--" + " " + "v" + utils.Color['redBold'] + "2.0" + utils.Color['white'] + " " + "--" + "\n" + utils.Color['white'])
    utils.Go(utils.Color['whiteBold'] + "WELCOME " + utils.Color['greenBold'] + os.uname()[1].upper() + utils.Color['whiteBold'] + " TO BINSpy" + utils.Color['white'])
    utils.Go("------")
    utils.Go("This is a exclusive version for researchers, or professionals \nwho are dedicated to research, we hope you enjoy." + "\n")
    utils.Go(utils.Color['whiteBold'] + "DISCLAIMER" + utils.Color['white'])
    utils.Go("------")
    utils.Go("This is a monitoring and research tool " + utils.Color['whiteBold'] + "OSINT" + utils.Color['white'] + ", which is distributed \nfor educational and investigative purposes, the person who has bought \nor uses this tool is responsible for its proper use or actions committed, \n" + utils.Color['whiteBold'] + "ALIF XAVIER LEOPARTA" + utils.Color['white'] + " (" + utils.Color['blue'] + "@ALIF101XL" + utils.Color['white'] + ") is not responsible for the use Or the scope that people can have \nthrough this software." + "\n")
    utils.Go(utils.Color['whiteBold']+ "CREATOR" + utils.Color['white'])
    utils.Go("------")
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "NAME: " + utils.Color['white'] + "ALIF XAVIER LEOPARTA" + " " + utils.Color['white'])
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "DESCRIPTION: " + utils.Color['white'] + "Hacker recognized by large technology companies")
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "GITHUB: " + utils.Color['white'] + "https://github.com/ALIF101XL")
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "TWITTER: " + utils.Color['white'] + "https://x.com/ALIF101XL" + utils.Color['white'] + "\n")
    sleep(3)
    utils.Go("Press enter to Continue...")
    raw_input()

# check OS
trackPeople.loadCheck()

# Request root home to run <BINSpy> with all permissions
trackPeople.rootConnection()

# Call the creation of the database when you open this file.
generateData.loadDatabase()

if __name__ == "__main__":
    try:
        # General expression this is expressed after the root
        trackPeople.main()
    except Exception as error:
        # Result of error
        utils.Go(utils.Color['whiteBold'] + "[" + utils.Color['redBold'] + "x" + utils.Color['whiteBold'] + "]" + utils.Color['redBold'] + " " + "ERROR: " + utils.Color['white'] + "%s" % error)
