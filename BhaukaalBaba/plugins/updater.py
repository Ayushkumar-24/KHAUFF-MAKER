import asyncio
import os
import sys
from telethon import events
from BhaukaalBaba import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, Mig11, Mig12, Mig13, Mig14, Mig15, Mig16, Mig17, Mig18, Mig19, Mig20, Mig21, Mig22, Mig23, Mig24, Mig25, Mig26, Mig27, Mig28, Mig29, Mig30, Mig31, Mig32, Mig33, Mig34, Mig35, Mig36, Mig37, Mig38, Mig39, Mig40, DEV
from .. import CMD_HNDLR as hl


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig11.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig12.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig13.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig14.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig15.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig16.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig17.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig18.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig19.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig20.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig21.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig22.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig23.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig24.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig25.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig26.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig27.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig28.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig29.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig30.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig31.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig32.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig33.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig34.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig35.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig36.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig37.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig38.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig39.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@Mig40.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
async def update(e):
    if e.sender_id in DEV:
        text = "**Updating Your BHAUKAAL BABA**\n`Please Wait... 🌚`"
        await e.reply(text, link_preview=None)
        try:
            await Mig.disconnect()
        except Exception:
            pass
        try:
            await Mig2.disconnect()
        except Exception:
            pass
        try:
            await Mig3.disconnect()
        except Exception:
            pass
        try:
            await Mig4.disconnect()
        except Exception:
            pass
        try:
            await Mig5.disconnect()
        except Exception:
            pass
        try:
            await Mig6.disconnect()
        except Exception:
            pass
        try:
            await Mig7.disconnect()
        except Exception:
            pass
        try:
            await Mig8.disconnect()
        except Exception:
            pass
        try:
            await Mig9.disconnect()
        except Exception:
            pass
        try:
            await Mig10.disconnect()
        except Exception:
            pass
        try:
            await Mig11.disconnect()
        except Exception:
            pass
        try:
            await Mig12.disconnect()
        except Exception:
            pass
        try:
            await Mig13.disconnect()
        except Exception:
            pass
        try:
            await Mig14.disconnect()
        except Exception:
            pass
        try:
            await Mig15.disconnect()
        except Exception:
            pass
        try:
            await Mig16.disconnect()
        except Exception:
            pass
        try:
            await Mig17.disconnect()
        except Exception:
            pass
        try:
            await Mig18.disconnect()
        except Exception:
            pass
        try:
            await Mig19.disconnect()
        except Exception:
            pass
        try:
            await Mig20.disconnect()
        except Exception:
            pass
        try:
            await Mig21.disconnect()
        except Exception:
            pass
        try:
            await Mig22.disconnect()
        except Exception:
            pass
        try:
            await Mig23.disconnect()
        except Exception:
            pass
        try:
            await Mig24.disconnect()
        except Exception:
            pass
        try:
            await Mig25.disconnect()
        except Exception:
            pass
        try:
            await Mig26.disconnect()
        except Exception:
            pass
        try:
            await Mig27.disconnect()
        except Exception:
            pass
        try:
            await Mig28.disconnect()
        except Exception:
            pass
        try:
            await Mig29.disconnect()
        except Exception:
            pass
        try:
            await Mig30.disconnect()
        except Exception:
            pass
        try:
            await Mig31.disconnect()
        except Exception:
            pass
        try:
            await Mig32.disconnect()
        except Exception:
            pass
        try:
            await Mig33.disconnect()
        except Exception:
            pass
        try:
            await Mig34.disconnect()
        except Exception:
            pass
        try:
            await Mig35.disconnect()
        except Exception:
            pass
        try:
            await Mig36.disconnect()
        except Exception:
            pass
        try:
            await Mig37.disconnect()
        except Exception:
            pass
        try:
            await Mig38.disconnect()
        except Exception:
            pass
        try:
            await Mig39.disconnect()
        except Exception:
            pass
        try:
            await Mig40.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
