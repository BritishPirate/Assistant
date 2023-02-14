import os.path

import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow



class Authenticator:
    creds = None
    def authenticateGoogle(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'GoogleCredentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        self.creds = creds
        return creds
    
    def authenticateTodoist(self):

        # Step 2: Use the access token to authenticate with Todoist

        headers = {
            "Authorization": f"Bearer {open('token.json', 'w')}",
        }

        response = requests.get("https://api.todoist.com/sync/v8/sync", headers=headers)

        # The response will contain the user's Todoist data, which you can use to access the Todoist API.
        return