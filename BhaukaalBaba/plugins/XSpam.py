async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from BhaukaalBaba import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, Mig11, Mig12, Mig13, Mig14, Mig15, Mig16, Mig17, Mig18, Mig19, Mig20, Mig21, Mig22, Mig23, Mig24, Mig25, Mig26, Mig27, Mig28, Mig29, Mig30, Mig31, Mig32, Mig33, Mig34, Mig35, Mig36, Mig37, Mig38, Mig39, Mig40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import MightyX1


# spam

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Mighty) == 2:
            message = str(Mighty[1])
            counter = int(Mighty[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Mighty[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Mighty[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(mighty) == 2:
            message = str(mighty[1])
            counter = int(mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#delayspam

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Mighty = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Mightysexy = Mighty[1:]
        if len(Mightysexy) == 2:
            message = str(Mightysexy[1])
            counter = int(Mightysexy[0])
            sleeptime = float(Mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Mightysexy[0])
            sleeptime = float(Mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Mightysexy[0])
            sleeptime = float(Mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

#abuse

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        Mightysexy = mighty[1:]
        smex = await e.get_reply_message()
        if len(Mightysexy) == 2:
            user = str(Mightysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in MightyX1:
                return
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(Mightysexy[1])
                counter = int(mighty[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(Mightysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in MightyX1:
                return
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(mighty[0])
                 await e.reply("😈 Dm Spam Started 😈")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(Mightysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in MightyX1:
                return
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(mighty[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )       

