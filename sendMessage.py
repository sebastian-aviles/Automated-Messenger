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
        "STATUS REPORT: Upload your transcripts please :)"
        ]
        # Edit message here
        message = 'Brother {}\n{} STATUS REPORT: I am collecting the classes brothers have taken and will take next semester to create a database. This will help not only yourself (if you ever need help in a class a brother has already taken) but it will also help future brothers. In order to do this, I need your unofficial transcript. Below I have included a link for you to submit the unofficial transcript (it also includes the steps to download it). I would recommend that you download the transcript on a computer using google chrome. I need it in PDF form (NO screenshots). \nI also sent it to your email, if I had an email on file; if you didn't receive one and would prefer to open the link on you email, reply with your email. Thank you brother.
Send STOP to cancel.
jk that won't work. Fill out this link'.format(row[1], random.choice(phrases),row[2])
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
