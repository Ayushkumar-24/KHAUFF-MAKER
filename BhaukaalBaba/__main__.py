# MightyXSpam

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from BhaukaalBaba.utils import load_plugins
import logging
from telethon import events
from . import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, Mig11, Mig12, Mig13, Mig14, Mig15, Mig16, Mig17, Mig18, Mig19, Mig20, Mig21, Mig22, Mig23, Mig24, Mig25, Mig26, Mig27, Mig28, Mig29, Mig30, Mig31, Mig32, Mig33, Mig34, Mig35, Mig36, Mig37, Mig38, Mig39, Mig40

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "BhaukaalBaba/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("BhaukaalBaba Successfully Deployed !!")

if len(argv) not in (1, 3, 4):
    try:
        Mig.disconnect()
    except Exception as e:
        pass
    try:
        Mig2.disconnect()
    except Exception as e:
        pass
    try:
        Mig3.disconnect()
    except Exception as e:
        pass
    try:
        Mig4.disconnect()
    except Exception as e:
        pass
    try:
        Mig5.disconnect()
    except Exception as e:
        pass
    try:
        Mig6.disconnect()
    except Exception as e:
        pass
    try:
        Mig7.disconnect()
    except Exception as e:
        pass
    try:
        Mig8.disconnect()
    except Exception as e:
        pass
    try:
        Mig9.disconnect()
    except Exception as e:
        pass
    try:
        Mig10.disconnect()
    except Exception as e:
        pass
    try:
        Mig11.disconnect()
    except Exception as e:
        pass
    try:
        Mig12.disconnect()
    except Exception as e:
        pass
    try:
        Mig13.disconnect()
    except Exception as e:
        pass
    try:
        Mig14.disconnect()
    except Exception as e:
        pass
    try:
        Mig15.disconnect()
    except Exception as e:
        pass
    try:
        Mig16.disconnect()
    except Exception as e:
        pass
    try:
        Mig17.disconnect()
    except Exception as e:
        pass
    try:
        Mig18.disconnect()
    except Exception as e:
        pass
    try:
        Mig19.disconnect()
    except Exception as e:
        pass
    try:
        Mig20.disconnect()
    except Exception as e:
        pass
    try:
        Mig21.disconnect()
    except Exception as e:
        pass
    try:
        Mig22.disconnect()
    except Exception as e:
        pass
    try:
        Mig23.disconnect()
    except Exception as e:
        pass
    try:
        Mig24.disconnect()
    except Exception as e:
        pass
    try:
        Mig25.disconnect()
    except Exception as e:
        pass
    try:
        Mig26.disconnect()
    except Exception as e:
        pass
    try:
        Mig27.disconnect()
    except Exception as e:
        pass
    try:
        Mig28.disconnect()
    except Exception as e:
        pass
    try:
        Mig29.disconnect()
    except Exception as e:
        pass
    try:
        Mig30.disconnect()
    except Exception as e:
        pass
    try:
        Mig31.disconnect()
    except Exception as e:
        pass
    try:
        Mig32.disconnect()
    except Exception as e:
        pass
    try:
        Mig33.disconnect()
    except Exception as e:
        pass
    try:
        Mig34.disconnect()
    except Exception as e:
        pass
    try:
        Mig35.disconnect()
    except Exception as e:
        pass
    try:
        Mig36.disconnect()
    except Exception as e:
        pass
    try:
        Mig37.disconnect()
    except Exception as e:
        pass
    try:
        Mig38.disconnect()
    except Exception as e:
        pass
    try:
        Mig39.disconnect()
    except Exception as e:
        pass
    try:
        Mig40.disconnect()
    except Exception as e:
        pass
else:
    try:
        Mig.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mig40.run_until_disconnected()
    except Exception as e:
        pass
