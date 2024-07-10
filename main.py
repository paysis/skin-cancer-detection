from utility.ziputil import unzip_multithread

zip_path = "dataset.zip"
extract_to = "extracted"
drive_path = "drive"
unzip_multithread(zip_path, extract_to, drive_path, count=2)