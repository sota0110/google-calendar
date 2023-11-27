from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from ..config.authorization import my_google_account
from ..config.id_dic import id_dic


class Gapi:
    def create_event(self, summary: str, start_time, end_time, all_day: bool) -> None:
        creds = service_account.Credentials.from_service_account_file('calapp/config/google_key.json')
        service = build('calendar', 'v3', credentials=creds)
        date_key = 'date' if all_day else 'dateTime'
        # date_format = '%Y-%m-%d' if all_day else '%Y-%m-%dT%H:%M:%S'
        event = {
            'summary': summary,
            'start': {
                date_key: start_time,
                'timeZone': 'Asia/Tokyo',
            },
            'end': {
                date_key: end_time,
                'timeZone': 'Asia/Tokyo',
            },
        }
        try:
            event = service.events().insert(calendarId=my_google_account, body=event).execute()
            print(f'Event created: {summary}')
            key_dic = max([int(i) for i in id_dic.keys()]) + 1 if len(id_dic) > 0 else 0
            id_dic[f"{key_dic}"] = event.get("id")
            with open('calapp/config/id_dic.py', 'w') as f:
                f.write(f'{id_dic = }')
        except HttpError as error:
            print(f'An error occurred: {error}')
            event = None
    
    def delete_event(self, index: str, event_id: str) -> None:
        creds = service_account.Credentials.from_service_account_file('calapp/config/google_key.json')
        service = build('calendar', 'v3', credentials=creds)
        try:
            service.events().delete(calendarId=my_google_account, eventId=event_id).execute()
            print(f'Event deleted: {index}')
        except HttpError as error:
            print(f'id: {index} not found')
            event = None
