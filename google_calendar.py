# google_calendar.py
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    service = build("calendar", "v3", credentials=creds)
    return service

def create_event():
    service = get_calendar_service()
    event = {
        'summary': 'Doctor Appointment',
        'start': {'dateTime': '2025-04-14T10:00:00+08:00', 'timeZone': 'Asia/Manila'},
        'end': {'dateTime': '2025-04-14T10:30:00+08:00', 'timeZone': 'Asia/Manila'}
    }
    service.events().insert(calendarId='primary', body=event).execute()