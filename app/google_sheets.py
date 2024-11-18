from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

from config.config import Config

def load_google_sheet(sheet_id, range_name):
    credentials = service_account.Credentials.from_service_account_file(
        Config.GOOGLE_SHEETS_CREDENTIALS_PATH
    )
    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    data = result.get("values", [])
    return pd.DataFrame(data[1:], columns=data[0])
