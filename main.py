from utility.ziputil import unzip

zip_path = "dataset.zip"
extract_to = "extracted"
drive_path = "drive"
unzip(zip_path, extract_to, drive_path, count=2)