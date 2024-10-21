import sys
import base64
from loguru import logger

logger.remove()

logger.add(sink=sys.stdout, level="INFO", format="<light-white>{time:YYYY-MM-DD HH:mm:ss}</light-white>"
                                                  " | <level>{level}</level>"
                                                  " | <light-white><b>{message}</b></light-white>")

logger.add("tonxdao.log", level="ERROR", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

logger = logger.opt(colors=True)

# Helper functions
def info(text):
    return logger.info(text)

def debug(text):
    return logger.debug(text)

def warning(text):
    return logger.warning(text)

def error(text):
    return logger.error(text)

def critical(text):
    return logger.critical(text)

def success(text):
    return logger.success(text)

def encode_base64(data: bytes) -> str:
    return base64.b64encode(data).decode()

def decode_base64(data: str) -> str:
    return base64.b64decode(data).decode()
