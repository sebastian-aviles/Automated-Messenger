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
        message = 'Brother {}, \nWe need you to vote for FIU SGA positions. You should be able to do it right from your phone but if you have any trouble please reach out. When you vote make sure you are selecting the candidates you want to vote for. Make sure you go through all the candidates. Our brothers (myself included) are running under "The Future is You" party. Below is the link to see all of the various candidates to vote. {}'.format(row[1], row[2])
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
