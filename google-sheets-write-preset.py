import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds
from recieve_data import main

def get_service_simple():
    return build('sheets', 'v4', developerKey=creds.api_key)


def get_service_sacc():

    creds_json = os.path.dirname(__file__) + "/creds/credentials.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


sheet = get_service_sacc().spreadsheets()
sheet_id = "1O9DPL0Ph5RcSk2rGCwfVdjr2QTOuLXSCF1zH-XcXyhY"

resp = sheet.values().update(
    spreadsheetId=sheet_id,
    range="Лист",
    valueInputOption="RAW",
    body={'values' : main()}).execute()

print(resp)