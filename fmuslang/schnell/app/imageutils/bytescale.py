# https://www.bytescale.com/dashboard/docs/file-api/GetFileDetails
# https://www.bytescale.com/dashboard/settings
# https://www.bytescale.com/dashboard/security/api_keys

import requests
import json
from typing import Optional

# Constants for base URLs
BASE_UPLOAD_URL = "https://api.bytescale.com/v2/accounts/{account_id}/uploads"
BASE_FILE_URL = "https://upcdn.io/{account_id}/raw"
BASE_FILE_DETAILS_URL = "https://api.bytescale.com/v2/accounts/{account_id}/files/details"

class BytescaleClient:
    def __init__(self, api_key: str, account_id: str):
        """
        Initialize the BytescaleClient with API key and account ID.
        """
        self.api_key = api_key
        self.account_id = account_id
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def upload_file_binary(self, file_path: str, mime_type: str, file_name: Optional[str] = None) -> dict:
        """
        Upload a file using binary data.
        
        :param file_path: Local path of the file to be uploaded.
        :param mime_type: MIME type of the file.
        :param file_name: Optional. File name for the uploaded file.
        :return: JSON response from the API.
        """
        url = BASE_UPLOAD_URL.format(account_id=self.account_id) + "/binary"
        headers = {**self.headers, "Content-Type": mime_type}
        with open(file_path, 'rb') as f:
            response = requests.post(url, headers=headers, data=f)

        return response.json()

    def upload_file_multipart(self, file_path: str) -> dict:
        """
        Upload a file using multipart/form-data.

        :param file_path: Local path of the file to be uploaded.
        :return: JSON response from the API.
        """
        url = BASE_UPLOAD_URL.format(account_id=self.account_id) + "/form_data"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, headers=self.headers, files=files)
        
        return response.json()

    def upload_file_from_url(self, file_url: str) -> dict:
        """
        Upload a file from an external URL.
        
        :param file_url: URL of the file to upload.
        :return: JSON response from the API.
        """
        url = BASE_UPLOAD_URL.format(account_id=self.account_id) + "/url"
        headers = {**self.headers, "Content-Type": "application/json"}
        data = {"url": file_url}
        response = requests.post(url, headers=headers, json=data)
        
        return response.json()

    def download_file(self, file_path: str, save_as: Optional[str] = None) -> bytes:
        """
        Download a file from Bytescale.
        
        :param file_path: The remote file path on Bytescale.
        :param save_as: Optional. Local file path to save the downloaded file.
        :return: The raw file content.
        """
        url = BASE_FILE_URL.format(account_id=self.account_id) + file_path
        response = requests.get(url, headers=self.headers)
        
        if save_as:
            with open(save_as, 'wb') as f:
                f.write(response.content)
        
        return response.content

    def get_file_details(self, file_path: str) -> dict:
        """
        Get metadata and details of a file.
        
        :param file_path: The remote file path on Bytescale.
        :return: JSON response with file details.
        """
        url = BASE_FILE_DETAILS_URL.format(account_id=self.account_id)
        params = {"filePath": file_path}
        response = requests.get(url, headers=self.headers, params=params)
        
        return response.json()
