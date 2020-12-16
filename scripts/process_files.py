import os
import sys
import shutil
import logging
import time

DEFAULT_FILES_DIR = "/app/share"
DEFAULT_RESULT_FILE = "/app/files/result.txt"

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler('app.log'), 
        logging.StreamHandler()
    ], 
    format='%(name)s - %(levelname)s - %(message)s')

search_str = "Test file search string."

def found_file(file_name):
    with open(DEFAULT_RESULT_FILE, "a") as out:
        out.write(f"{file_name}\n")

def process_file(file_path):
    fname = os.path.basename(file_path)
    logging.info(f"Processing file: {fname}")
    with open(file_path) as input:
        if search_str in input.read():
            logging.info(f"Required string found in file {fname}")
            found_file(fname)
        else:
            logging.info(f"Required string not found in file {fname}")
    os.remove(file_path)

def process_files(dir_path=DEFAULT_FILES_DIR):
    if not os.path.isdir(dir_path):
        logging.error("Directory invalid.")
        exit()
    
    for fname in os.listdir(dir_path):
        if not fname.endswith(".txt"):
            continue
        logging.info(f"Found file: {fname}")
        process_file(os.path.join(dir_path, fname))

def main(args):
    logging.info("Starting processor.")
    while True:
        process_files()
        time.sleep(5)


if __name__ == "__main__":
    main(sys.argv)