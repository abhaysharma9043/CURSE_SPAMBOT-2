import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30 , STRING31 , STRING32 , STRING33 , STRING34 , STRING35 , STRING36 , STRING37 , STRING38 , STRING39 , STRING40 , STRING41 , STRING42 , STRING43 ,
STRING44 , STRING45 , STRING46 , STRING47 , STRING48 , STRING49 , STRING50
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
one = STRING
two = STRING2
three = STRING3
four = STRING4
five = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleven = STRING11
twelve = STRING12
thirteen = STRING13
fourteen = STRING14
fifteen = STRING15
sixteen = STRING16
seventeen = STRING17
eighteen = STRING18
nineteen = STRING19
twenty = STRING20
twentyone = STRING21
twentytwo = STRING22
twentythree = STRING23
twentyfour = STRING24
twentyfive = STRING25
twentysix = STRING26
twentyseven = STRING27
twentyeight = STRING28
twentynine = STRING29
thirty = STRING30
thirtyone = STRING31
thirtytwo = STRING32
thirtythree = STRING33
thirtyfour = STRING34
thirtyfive = STRING35
thirtysix = STRING36
thirtyseven = STRING37
thirtyeight = STRING38
thirtynine = STRING39
fourty = STRING40
fourtyone = STRING41
fourtytwo = STRING42
fourtythree = STRING43
fourtyfour = STRING44
fourtyfive = STRING45
fourtysix = STRING46
fourtyseven = STRING47
fourtyeight = STRING48
fourtynine = STRING49
fifty = STRING50

bot01 = ""
bot02 = ""
bot03 = ""
bot04 = ""
bot05 = ""
bot06 = ""
bot07 = ""
bot08 = ""
bot09 = ""
bot10 = ""
bot11 = ""
bot12 = ""
bot13 = ""
bot14 = ""
bot15 = ""
bot16 = ""
bot17 = ""
bot18 = ""
bot19 = ""
bot20 = ""
bot21 = ""
bot22 = ""
bot23 = ""
bot24 = ""
bot25 = ""
bot26 = ""
bot27 = ""
bot28 = ""
bot29 = ""
bot30 = ""
bot31 = ""
bot32 = ""
bot33 = ""
bot34 = ""
bot35 = ""
bot36 = ""
bot37 = ""
bot38 = ""
bot39 = ""
bot40 = ""
bot41 = ""
bot42 = ""
bot43 = ""
bot44 = ""
bot45 = ""
bot46 = ""
bot47 = ""
bot48 = ""
bot49 = ""
bot50 = ""


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)

async def start_curse():
global bot01
global bot02
global bot03
global bot04
global bot05
global bot06
global bot07
global bot08
global bot09
global bot10
global bot11
global bot12
global bot13
global bot14
global bot15
global bot16
global bot17
global bot18
global bot19
global bot20
global bot21
global bot22
global bot23
global bot24
global bot25
global bot26
global bot27
global bot28
global bot29
global bot30
global bot31
global bot32
global bot33
global bot34
global bot35
global bot36
global bot37
global bot38
global bot39
global bot40
global bot41
global bot42
global bot43
global bot44
global bot45
global bot46
global bot47
global bot48
global bot49
global bot50

if one:
        session_name = str(one)
        print("String 1 Found")
        bot01 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await bot01.start()
            botme = await Bot01.get_me()
            await bot01(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot01(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            bot01 = "one"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        bot01 = TelegramClient(session_name, a, b)
        try:
            await bot01.start()
        except Exception as e:
            pass

if two:
        session_name = str(two)
        print("String 2 Found")
        bot02 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await bot02.start()
            await bot02(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot02(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot02.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        bot02 = TelegramClient(session_name, a, b)
        try:
            await bot02.start()
        except Exception as e:
            pass

if three:
        session_name = str(three)
        print("String 3 Found")
        bot03 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await bot03.start()
            await bot03(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot03(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot03.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        bot03 = TelegramClient(session_name, a, b)
        try:
            await bot03.start()
        except Exception as e:
            pass

if four:
        session_name = str(four)
        print("String 4 Found")
        bot04 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await bot04.start()
            await bot04(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot04(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot04.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        bot04 = TelegramClient(session_name, a, b)
        try:
            await bot04.start()
        except Exception as e:
            pass
