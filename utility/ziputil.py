import zipfile
import shutil
import os
import time

def unzip_partial(zip_path, extract_to, start_index=0, count=10000):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        all_files = zip_ref.namelist()
        selected_files = all_files[start_index: start_index + count]
        for file in selected_files:
            zip_ref.extract(file, extract_to)

def copy_to_drive(local_path, drive_path):
    shutil.copytree(local_path, drive_path, dirs_exist_ok=True)
    

def delete_local_files(local_path):
    shutil.rmtree(local_path)

def unzip(zip_path, extract_to, drive_path, start_index=0, count=10000):
    total_files=len(zipfile.ZipFile(zip_path).namelist())

    while start_index < total_files:
        unzip_partial(zip_path, extract_to, start_index, count)
        copy_to_drive(extract_to, drive_path)
        delete_local_files(extract_to)
        start_index += count