
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import shutil
os.environ["PATH"] += os.pathsep + "C:\Path_Programs"
from pydub import AudioSegment

""""
This program is written to only find aiff files currently, it must be modified ot work with other file types

This program also will not find some files, however the website has more files than the one file for each key that we need
Because of this, we actually do find each key at least once
"""
# specify the URL of the website to crawl
url = "https://theremin.music.uiowa.edu/MISpiano.html"

# create a folder to store the downloaded files
folder_name = "piano_aiff_files"
if not os.path.exists(folder_name):

    os.makedirs(folder_name)

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": os.path.abspath(folder_name)}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
# create a Chrome webdriver instance


# navigate to the website and get the page content
driver.get(url)
time.sleep(1)
content = driver.page_source

# parse the page content with BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# find all the links on the page
links = soup.find_all("a")
# Weirdly enough for our current usage, some of the files are listed twice and sometimes
# The file is not found
# Since there are 88 keys on the piano, I assume that each key ended up being downloaded in some fashion
# download each file linked on the website
not_found_files = []
for link in links:
    file_url = link.get("href")
    if file_url is not None and file_url.endswith(".aiff") and "piano" in link.text.lower():
        # simulate a click on the link to initiate the download
        try:
            driver.find_element(By.LINK_TEXT, link.text).click()
            time.sleep(1)
            # get the filename from the URL
            file_name = os.path.join(folder_name, file_url.split("/")[-1])
            # move the downloaded file to the folder
            shutil.move(os.path.join(os.path.abspath("Downloads"), file_url.split("/")[-1]), file_name)
            print(f"Downloaded {file_name}")
        except NoSuchElementException:
            print(f"No such element error: {file_url}")
            continue
        except FileNotFoundError:
            print(f"Download Initiated: {file_url}")
            continue
        not_found_files.append(file_url)
if not_found_files:
    print("\033[31m"+f"Missing files from download list: {not_found_files}")
# close the webdriver instance
driver.quit()

folder_path = os.path.abspath(folder_name)
new_folder_name = "piano_wav_files"
if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)
# set the folder path containing the AIFF files
#Enter the folder path to your piano_aiff_files
for filename in os.listdir(folder_path):
    # check if the file is an AIFF file
    if filename.endswith(".aiff"):
        # open the AIFF file with pydub
        aiff_file = AudioSegment.from_file(os.path.join(folder_path, filename), format="aiff")
        # create the new filename with a WAV extension
        wav_filename = os.path.splitext(filename)[0] + ".wav"
        # save the converted file as a WAV file in the same folder
        aiff_file.export(os.path.join(new_folder_name, wav_filename), format="wav")
print("aiff files converted to wav files, please use Audacity for editing")
