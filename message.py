import random
import os
import argparse
import csv

#use file to send texts
default_phone_number = "3059048596"
with open('listOfBrothers.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        ##########
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", dest="number", action="store", help="phone number", default=default_phone_number)
        args = parser.parse_args()
        phone_number = row[0]
        # Add phrases here
        phrases = [
        "STATUS REPORT: If you got this message then my automated texts are working, please reply to confirm you received this. Send STOP to cancel. \njk that won't work.",
        "STATUS REPORT: If you got this message then my automated texts are working, please reply to confirm you received this. Send STOP to cancel. \njk that won't work."
        ]
        # Edit message here
        message = 'Brother {}\n{}'.format(row[1], random.choice(phrases))
        file_path = os.path.realpath(__file__)
        print(file_path)
        file_path = file_path.split(os.path.basename(__file__))[0]
        print(file_path)
        bash_command = 'osascript sendMessage.applescript {} "{}"'.format(
            phone_number, message
        )
        os.system(bash_command)
        ##########
    print('Processed {} lines'.format(line_count))
#osascript sendMessage.applescript 9548030254 testing123