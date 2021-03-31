import random
import os
import argparse
import csv

#use file to send texts
default_phone_number = "XXXXXXXXXX"
with open('listOfContacts.txt') as csv_file:
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
        ""
        ]
        # Edit message here
        message = 'Brother {},\nTesting 123. Link below\n{}'.format(row[2],row[3])
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
##STATUS REPORT: Upload your transcripts please :)
