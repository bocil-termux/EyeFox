import os
import subprocess

def unzip_and_setup():
    source_folder = '.main/tools/'
    if os.path.exists(source_folder):
        for zip_file in os.listdir(source_folder):
            if zip_file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(source_folder, zip_file), 'r') as zip_ref:
                    zip_ref.extractall(source_folder)

    os.system("chmod +x .main/* > /dev/null 2>&1")
    os.system("chmod +x .main/tools/* > /dev/null 2>&1")

    subprocess.run([
        "sudo", "apt", "install", "-y", 
        "python3-cryptography", "python3-ntplib", "python3-colorama"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Selesai")

if __name__ == "__main__":
    import zipfile
    unzip_and_setup()
