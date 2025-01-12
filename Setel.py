import zipfile
import os

def unzip_files():
    source_folder = '.main/tools/'
    if not os.path.exists(source_folder):
        return
    for zip_file in os.listdir(source_folder):
        if zip_file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(source_folder, zip_file), 'r') as zip_ref:
                zip_ref.extractall(source_folder)
    print("Selesai")

if __name__ == "__main__":
    unzip_files()
