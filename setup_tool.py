import os
import subprocess
import zipfile

def unzip_and_setup():
    source_folder = '.main/tools/'

    gf_dir = os.path.expanduser("~/.gf")
    os.makedirs(gf_dir, exist_ok=True)

    if os.path.exists(source_folder):
        for zip_file in os.listdir(source_folder):
            if zip_file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(source_folder, zip_file), 'r') as zip_ref:
                    zip_ref.extractall(source_folder)

    os.system("chmod +x .main/* > /dev/null 2>&1")
    os.system("chmod +x .main/tools/* > /dev/null 2>&1")

    subprocess.run([
        "sudo", "apt", "install", "-y",
        "python3-cryptography", "toilet", "toilet-fonts", "python3-ntplib", "python3-colorama"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    zip_file_path = "gf-pattern.zip"
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(gf_dir)

    print("Selesai")

if __name__ == "__main__":
    unzip_and_setup()
