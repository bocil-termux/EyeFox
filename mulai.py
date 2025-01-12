import os
import time
from cryptography.fernet import Fernet
import subprocess
import sys
import colorama
from colorama import init, Fore, Style
import ntplib

ENCRYPTION_KEY = b"hw1FLWARO3YJ3tF8wQOvRuuBr-YUDuhNEwSmKiXpYG8="
TOKEN_EXPIRY_TIME = 30 * 24 * 60 * 60

def get_ntp_time():
    """Mengambil waktu dari server NTP"""
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3)
        return response.tx_time
    except Exception as e:
        print(f"Jaringan Internet Tidak Terdeteksi")
        if '[Errno -3]' in str(e):
            sys.exit("Aktifkan Jaringan Internet Anda dan Coba Lagi..")
        return None

def decrypt_content(encrypted_content):
    fernet = Fernet(ENCRYPTION_KEY)
    try:
        decrypted_content = fernet.decrypt(encrypted_content)
        return decrypted_content.decode()
    except Exception:
        return None

def get_file_content(file_path):
    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        decrypted_content = decrypt_content(file_data)
        return decrypted_content
    except Exception:
        return None

def is_token_valid():
    token_path = ".main/.token_autentikasi"

    if not os.path.exists(token_path):
        return False

    try:
        with open(token_path, "rb") as token_file:
            token_data = token_file.read().split(b'\n')
            encrypted_token = token_data[0]
            creation_time = int(token_data[1])

        decrypted_token = decrypt_content(encrypted_token)
        if not decrypted_token:
            return False

        current_time = get_ntp_time()
        if current_time is None:
            return False

        if current_time - creation_time > TOKEN_EXPIRY_TIME:
            return False

        return True
    except Exception:
        return False

def run_tools():
    if is_token_valid():
        content = get_file_content(".main/a")
    else:
        content = get_file_content(".main/login")

    if content:
        try:
            exec(content, globals())
        except KeyboardInterrupt:
            print("\nProses dihentikan oleh pengguna.")
    else:
        print("Gagal membaca atau mendekripsi file.")

if __name__ == "__main__":
    run_tools()
