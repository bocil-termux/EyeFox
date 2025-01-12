import os
import subprocess

def unzip_and_setup():
    # Langkah 1: Ekstrak file ZIP
    source_folder = '.main/tools/'
    if os.path.exists(source_folder):
        for zip_file in os.listdir(source_folder):
            if zip_file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(source_folder, zip_file), 'r') as zip_ref:
                    zip_ref.extractall(source_folder)

    # Langkah 2: Ubah permission file dengan chmod +x
    os.system("chmod +x .main/* > /dev/null 2>&1")
    os.system("chmod +x .main/tools/* > /dev/null 2>&1")

    # Langkah 3: Instal paket menggunakan apt
    subprocess.run([
        "sudo", "apt", "install", "-y", 
        "python3-cryptography", "python3-ntplib", "python3-colorama"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Langkah 4: Cetak selesai
    print("Selesai")

if __name__ == "__main__":
    import zipfile
    unzip_and_setup()
