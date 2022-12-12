import json
import requests
from config import ACCESS_TOKEN, file_path, dropbox_file_path


class DropboxTest:
    def __init__(self):
        self.access_token = ACCESS_TOKEN
        self.file_path = file_path
        self.dropbox_file_path = dropbox_file_path

    def upload_file(self):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Dropbox-API-Arg': json.dumps({"path": self.dropbox_file_path,
                                           "mode": "add", "autorename": True, "mute": False, "strict_conflict": False}),
            'Content-Type': 'application/octet-stream'
        }
        with open(self.file_path, 'rb') as file:
            file_data = file.read()
        response = requests.post(url, headers=headers, data=file_data)
        return response

    def get_file_metadata(self):
        url = 'https://api.dropboxapi.com/2/files/get_metadata'
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        data = json.dumps({'path': self.dropbox_file_path})
        response = requests.post(url, headers=headers, data=data)
        return response

    def delete_file(self):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        data = json.dumps(
            {'path': self.dropbox_file_path})
        response = requests.post(url, headers=headers, data=data)
        return response
