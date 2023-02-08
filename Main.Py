from __future__ import print_function


import os.path
import CalendarManager
import Authenticator

from datetime import datetime, timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

authenticator = Authenticator.Authenticator() # Selecting an instance of the class
authenticator.authenticate()

calendarManager = CalendarManager.CalendarManager() # Selecting the class

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    
    creds = authenticator.creds

    try:
        service = build('calendar', 'v3', credentials=creds)

        attendees = ['nur10000@gmail.com']

        reminders = [
            ('popup', 24 * 60),
            ('email', 24 * 60 * 2)
        ]

        event = calendarManager.newEvent('eventSummary', 'Narnia', 'EventDescription', datetime(2023, 2, 8, 15, 00, 00), datetime(2023, 2, 8, 16, 00, 00), None, None   , reminders)

        calendarManager.addEvent(service, event)

        # Call the Calendar API
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
