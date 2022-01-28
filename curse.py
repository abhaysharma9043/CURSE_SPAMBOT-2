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

if five:
        session_name = str(five)
        print("String 5 Found")
        bot05 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await bot05.start()
            await bot05(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot05(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot05.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        bot05 = TelegramClient(session_name, a, b)
        try:
            await bot05.start()
        except Exception as e:
            pass

if six:
        session_name = str(six)
        print("String 6 Found")
        bot06 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await bot06.start()
            await bot06(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot06(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot06.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        bot06 = TelegramClient(session_name, a, b)
        try:
            await bot06.start()
        except Exception as e:
            pass

if seven:
        session_name = str(seven)
        print("String 7 Found")
        bot07 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bot07.start()
            await bot07(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot07(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot07.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bot07 = TelegramClient(session_name, a, b)
        try:
            await bot07.start()
        except Exception as e:
            pass

if eight:
        session_name = str(eight)
        print("String 8 Found")
        bot08 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await bot08.start()
            await bot08(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot08(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot08.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        bot08 = TelegramClient(session_name, a, b)
        try:
            await bot08.start()
        except Exception as e:
            pass
if nine:
        session_name = str(nine)
        print("String 9 Found")
        bot09 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await bot09.start()
            await bot09(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot09(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot09.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        bot09 = TelegramClient(session_name, a, b)
        try:
            await bot09.start()
        except Exception as e:
            pass

if ten:
        session_name = str(ten)
        print("String 10 Found")
        bot10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await bot10.start()
            await bot10(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot10(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        bot10 = TelegramClient(session_name, a, b)
        try:
            await bot10.start()
        except Exception as e:
            pass

if eleven:
        session_name = str(eleven)
        print("String 11 Found")
        bot11 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await bot11.start()
            await bot11(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot11(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        bot11 = TelegramClient(session_name, a, b)
        try:
            await bot11.start()
        except Exception as e:
            pass

if twelve:
        session_name = str(twelve)
        print("String 12 Found")
        bot12 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await bot12.start()
            await bot12(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot12(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        bot12 = TelegramClient(session_name, a, b)
        try:
            await bot12.start()
        except Exception as e:
            pass

if thirteen:
        session_name = str(thirteen)
        print("String 13 Found")
        bot13 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await bot13.start()
            await bot13(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot13(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        bot13 = TelegramClient(session_name, a, b)
        try:
            await bot13.start()
        except Exception as e:
            pass

if fourteen:
        session_name = str(fourteen)
        print("String 14 Found")
        bot14 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await bot14.start()
            await bot14(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot14(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        bot14 = TelegramClient(session_name, a, b)
        try:
            await bot14.start()
        except Exception as e:
            pass

if fifteen:
        session_name = str(fifteen)
        print("String 15 Found")
        bot15 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await bot15.start()
            await bot15(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot15(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        bot15 = TelegramClient(session_name, a, b)
        try:
            await bot15.start()
        except Exception as e:
            pass

if sixteen:
        session_name = str(sixteen)
        print("String 16 Found")
        bot16 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await bot16.start()
            await bot16(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot16(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        pass
        session_name = "startup"
        bot16 = TelegramClient(session_name, a, b)
        try:
            await bot16.start()
        except Exception as e:
            pass

if seventeen:
        session_name = str(seventeen)
        print("String 17 Found")
        bot17 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await bot17.start()
            await bot17(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot17(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        pass
        session_name = "startup"
        bot17 = TelegramClient(session_name, a, b)
        try:
            await bot17.start()
        except Exception as e:
            pass

if eighteen:
        session_name = str(eighteen)
        print("String 18 Found")
        bot18 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await bot18.start()
            await bot18(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot18(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        pass
        session_name = "startup"
        bot18 = TelegramClient(session_name, a, b)
        try:
            await bot18.start()
        except Exception as e:
            pass

if nineteen:
        session_name = str(nineteen)
        print("String 19 Found")
        bot19 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await bot19.start()
            await bot19(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot19(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        pass
        session_name = "startup"
        bot19 = TelegramClient(session_name, a, b)
        try:
            await bot19.start()
        except Exception as e:
            pass

if twenty:
        session_name = str(twenty)
        print("String 20 Found")
        bot20 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await bot20.start()
            await bot20(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot20(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        pass
        session_name = "startup"
        bot20 = TelegramClient(session_name, a, b)
        try:
            await bot20.start()
        except Exception as e:
            pass

if twentyone:
        session_name = str(twentyone)
        print("String 21 Found")
        bot21 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await bot21.start()
            await bot21(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot21(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot21.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        pass
        session_name = "startup"
        bot21 = TelegramClient(session_name, a, b)
        try:
            await bot21.start()
        except Exception as e:
            pass

if twentytwo:
        session_name = str(twentytwo)
        print("String 22 Found")
        bot22 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await bot22.start()
            await bot22(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot22(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "startup"
        bot22 = TelegramClient(session_name, a, b)
        try:
            await bot22.start()
        except Exception as e:
            pass

if twentythree:
        session_name = str(twentythree)
        print("String 23 Found")
        bot23 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await bot23.start()
            await bot23(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot23(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "startup"
        bot23 = TelegramClient(session_name, a, b)
        try:
            await bot23.start()
        except Exception as e:
            pass

if twentyfour:
        session_name = str(twentyfour)
        print("String 24 Found")
        bot24 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await bot24.start()
            await bot24(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot24(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "startup"
        bot24 = TelegramClient(session_name, a, b)
        try:
            await bot24.start()
        except Exception as e:
            pass

if twentyfive:
        session_name = str(twentyfive)
        print("String 25 Found")
        bot25 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await bot25.start()
            await bot25(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot25(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "startup"
        bot25 = TelegramClient(session_name, a, b)
        try:
            await bot25.start()
        except Exception as e:
            pass

if twentysix:
        session_name = str(twentysix)
        print("String 26 Found")
        bot26 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await bot26.start()
            await bot26(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot26(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "startup"
        bot26 = TelegramClient(session_name, a, b)
        try:
            await bot26.start()
        except Exception as e:
            pass

if twentyseven:
        session_name = str(twentyseven)
        print("String 27 Found")
        bot27 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await bot27.start()
            await bot27(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot27(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        bot27 = TelegramClient(session_name, a, b)
        try:
            await bot27.start()
        except Exception as e:
            pass

if twentyeight:
        session_name = str(twentyeight)
        print("String 28 Found")
        bot28 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await bot28.start()
            await bot28(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot28(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        bot28 = TelegramClient(session_name, a, b)
        try:
            await bot28.start()
        except Exception as e:
            pass

if twentynine:
        session_name = str(twentynine)
        print("String 29 Found")
        bot29 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await bot29.start()
            await bot29(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot29(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        bot29 = TelegramClient(session_name, a, b)
        try:
            await bot29.start()
        except Exception as e:
            pass

if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        bot30 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await bot30.start()
            await bot30(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot30(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        bot30 = TelegramClient(session_name, a, b)
        try:
            await bot30.start()
        except Exception as e:
            pass

if thirtyone:
        session_name = str(thirtyone)
        print("String 31 Found")
        bot31 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await bot31.start()
            await bot31(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot31(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "startup"
        bot31 = TelegramClient(session_name, a, b)
        try:
            await bot31.start()
        except Exception as e:
            pass
            
if thirtytwo:
        session_name = str(thirtytwo)
        print("String 32 Found")
        bot32 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 32")
            await bot32.start()
            await bot32(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT"))
            await bot32(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMBOT_SUPPORT"))
            botme = await bot32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "startup"
        bot32 = TelegramClient(session_name, a, b)
        try:
            await bot32.start()
        except Exception as e:
            pass











