import datetime
from google.oauth2 import service_account
import gspread
import streamlit as st
import pandas as pd

google_cloud_secrets = st.secrets["google_api"]

creds = service_account.Credentials.from_service_account_info(
    {
        "type": google_cloud_secrets["type"],
        "project_id": google_cloud_secrets["project_id"],
        "private_key_id": google_cloud_secrets["private_key_id"],
        "private_key": google_cloud_secrets["private_key"].replace("\\n", "\n"),
        "client_email": google_cloud_secrets["client_email"],
        "client_id": google_cloud_secrets["client_id"],
        "auth_uri": google_cloud_secrets["auth_uri"],
        "token_uri": google_cloud_secrets["token_uri"],
        "auth_provider_x509_cert_url": google_cloud_secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": google_cloud_secrets["client_x509_cert_url"],
        "universe_domain": google_cloud_secrets["universe_domain"],
    },
    scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"],
)

client = gspread.authorize(creds)


def get_data(sheet):
    spreadsheet_id = "1S1cbT7RW2dBg-LYaG9FW08LttowjfyOftnY2R18PSPc"
    data = client.open_by_key(spreadsheet_id).worksheet(sheet).get_all_records()
    data = pd.DataFrame(data)
    return data


def input_data(date,nama,cmc):
    spreadsheet_id = "1S1cbT7RW2dBg-LYaG9FW08LttowjfyOftnY2R18PSPc"
    sheet = client.open_by_key(spreadsheet_id).worksheet("Data")
    sheet.append_row([date,nama,cmc])