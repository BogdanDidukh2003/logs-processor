from codecs import open
from google_drive_downloader import GoogleDriveDownloader as gdd # package googledrivedownloader
import re


ENCODING = "iso-8859-15"
FILE_ID = "0B1k21nkk13PYZ0l5eUdkOUtOa2M"
FILE_NAME = "access_log_Jul95"


def main():
    gdd.download_file_from_google_drive(file_id=FILE_ID,
                                        dest_path="./res/{}.zip".format(FILE_NAME),
                                        unzip=True)
    file = open("./res/{}".format(FILE_NAME), "r", ENCODING)
    pattern = "\[01/Jul/1995:03:(39|4[0-9]|5[0-5]).*\]\s\"GET\s[^\s\"\.]+\.[gG][iI][fF]((\s[^\"]*)|(\s))?\"\s?200"
    matches_number = 0

    print("Processing...")
    for line in file:
        matched_log = re.search(pattern, line)
        if matched_log:
            matches_number += 1

    file.close()
    print("Done.")
    print("Number of gif files returned successfully from 03:39 to 03:55 01/Jul/1995:\n", matches_number, sep="")


main()
