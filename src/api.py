import aiohttp
import json
from config import BASE_URL, TOKEN
from ssl_utils import create_ssl_context
from utils import prepare_form_data, prepare_detect_type_params

class KataAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.ssl_context = create_ssl_context()
        self.headers = {"Authorization": f"Bearer {TOKEN}"}

    async def scan_file(self, payload):
        """Uploads a file for scanning."""
        url = f"{self.base_url}/scans"
        data = prepare_form_data(payload)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, ssl=self.ssl_context, headers=self.headers) as response:
                return await response.text()

    async def delete_file(self, payload):
        """Deletes a scanned file."""
        url = f"{self.base_url}/scans/{payload['file_no']}"

        async with aiohttp.ClientSession() as session:
            async with session.delete(url, ssl=self.ssl_context, headers=self.headers) as response:
                return await response.json()

    async def get_scan_state(self):
        """Retrieves the state of scans."""
        url = f"{self.base_url}/scans/state"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=self.ssl_context, headers=self.headers) as response:
                return await response.json()

    async def detect_type(self, payload):
        """Detects the type of an object."""
        url = f"{self.base_url}/detects"
        params = prepare_detect_type_params(payload)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, ssl=self.ssl_context, headers=self.headers) as response:
                return await response.json()

    async def get_object_restrictions(self):
        """Retrieves object restrictions."""
        url = f"{self.base_url}/scans/filters"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=self.ssl_context, headers=self.headers) as response:
                return await response.json()
