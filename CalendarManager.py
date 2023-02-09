
from datetime import datetime, timezone

import pytz

class CalendarManager:

    def newEvent(self, summary, location, description, startTime, endTime, recurrance = None, attendees = None, reminders = None): 
        startTime = self.isoTime(startTime)
        endTime = self.isoTime(endTime)
        
        if(attendees != None):
            attendees = self.formatAttendees(attendees)
        if(reminders != None):
            reminders = self.formatReminders(reminders)
        
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': startTime,
                #'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': endTime,
                #'timeZone': 'America/Los_Angeles',
            },
            'recurrence': [
               recurrance #'RRULE:FREQ=DAILY;COUNT=2'
            ] if recurrance != None else None,
            'attendees': 
                attendees
                #{'email': 'lpage@example.com'},
                #{'email': 'sbrin@example.com'},
            if attendees != None else None,
            
            'reminders': {
                'useDefault': (not reminders),
                'overrides':
                    #{'method': 'email', 'minutes': 24 * 60},
                    #{'method': 'popup', 'minutes': 10},
                    reminders
               if reminders != None else None,
            },
        }
        return event

    def addEvent(self, service, event, calendarId = None):
        event = service.events().insert(calendarId=('primary' if calendarId == None else calendarId), body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        return event

    def deleteEvent(self, service, eventId, calendarId = None):
        event = service.events().delete(calendarId=('primary' if calendarId == None else calendarId), eventId = eventId).execute()
        return event

    def isoTime(self, datetime):
        #datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        
        ret = datetime.astimezone(pytz.timezone("Europe/London")).replace(microsecond=0).isoformat()
        return ret

    def formatReminders(self, reminders):
        ret = []
        for reminder in reminders:
            ret += {'method': reminder[0], 'minutes': reminder[1]},
        return ret

    def formatAttendees(self, attendees):
        ret = []
        for attendee in attendees:
            ret += {'email': attendee},
        return ret