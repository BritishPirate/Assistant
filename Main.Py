from __future__ import print_function

import os.path

from ListManager import ListManager as lm
from SpeechRecognitionManager import SpeechRecognitionManager as srm
from CalendarManager import CalendarManager
from Authenticator import Authenticator
from datetime import datetime, timezone, date
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#TODO:
# Pick a list service. 

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

authenticator = Authenticator() # Selecting an instance of the class
authenticator.authenticateGoogle()

calendarManager = CalendarManager() # Selecting the class

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    print(date(2023, 2, 15).isoformat())
    print(datetime(2023, 2, 15, 15, 25, 13).isoformat())

    lm().addTask(content='TestContent', projectId='2307738756')

    # tasks = lm().getTasks(projectId='2307738756')
    # for task in tasks:
    #     print(task)
    #     print()
    # creds = authenticator.creds
    """
    try:
        service = build('calendar', 'v3', credentials=creds)
        attendees = ['nur10000@gmail.com']
        reminders = [
            ('popup', 24 * 60),
            ('email', 24 * 60 * 2)
        ]
        event = calendarManager.newEvent('eventSummary', 'Narnia', 'EventDescription', datetime(2023, 2, 9, 15, 00, 00), datetime(2023, 2, 9, 16, 00, 00), None, None, reminders)

        #event = calendarManager.addEvent(service, event)

        #delEvent = calendarManager.deleteEvent(service, event['id'])

        events = calendarManager.findEvents(service=service, searchText='apple')

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
    
    except HttpError as error:
        print('An error occurred: %s' % error)
    """

if __name__ == '__main__':
    main()
