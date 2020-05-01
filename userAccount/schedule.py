from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import json

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("credentials_new.json", scopes=scopes)

credentials = flow.run_console()

pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
creedentials = pickle.load()
credentials = "ya29.a0Ae4lvC0l9zNOYduT1MYLv7cyBIJPKjnwGTLPkeRCealknOlBrvugepda4I-kgw6iMeRUJsa-p6cpmb2Yzfi2pq8YKN6FooW7OfLreqYRRC9bZW6eJeeOmsWhKlo8AlEQJ3aD_vL_blScFkalEILaI1aPA7biMfIdqdQr"
service = build("calendar", "v3", credentials=credentials)

# copied_code = "4/zAFCrKrt5DZg1Dp7zx6fxwqLazVQUQe-sYzR8TB4uEmHqLhSCPcQc8M"

result = service.calendarList().list().execute()
print(credentials)

# print(result['items'][0])
calendar_id = result['items'][0]['id']
print(result['items'])
result = service.events().list(calendarId=calendar_id, timeZone="America/New_York").execute()

for i in result['items']:
    print(i)
with open('schedule.json', 'w') as outfile:
    json.dump(result['items'], outfile)
# print(result['items'])
