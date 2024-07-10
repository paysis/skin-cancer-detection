import concurrent.futures
import zipfile
import shutil
import os
import time
import concurrent
from concurrent.futures import ThreadPoolExecutor

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

def process_chunk(id, start_index, count, zip_path, extract_to, drive_base_path):
    extract_to = extract_to + str(id)
    unzip_partial(zip_path, extract_to, start_index, count)
    copy_to_drive(extract_to, drive_base_path)
    delete_local_files(extract_to)


def unzip_multithread(zip_path, extract_to, drive_path, start_index=0, count=100000):
    with ThreadPoolExecutor() as executor:
        futures = []
        total_files=len(zipfile.ZipFile(zip_path).namelist())
        for id, start_index in enumerate(range(0, total_files, count)):
            futures.append(executor.submit(process_chunk, id, start_index, count, zip_path, extract_to, drive_path))

        concurrent.futures.wait(futures)

def unzip_singlethread(zip_path, extract_to, drive_path, start_index=0, count=10000):
    total_files=len(zipfile.ZipFile(zip_path).namelist())

    while start_index < total_files:
        unzip_partial(zip_path, extract_to, start_index, count)
        copy_to_drive(extract_to, drive_path)
        delete_local_files(extract_to)
        start_index += count