# -*- coding: utf-8 -*-
import os
import json
import base64
import requests
import http.client
from dotenv import load_dotenv


class NaverAI:
    def __init__(self):
        load_dotenv()

        self._host = os.getenv("HOST")
        self._api_key = os.getenv("API_KEY")
        self._api_key_primary_val = os.getenv("API_KEY_PRIMARY_VAL")
        self._gateway_key = os.getenv("GATEWAY_KEY")
        self._request_id = os.getenv("REQUEST_ID")

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            # 'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }
        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/testapp/v1/completions/LK-B', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()

        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['text']
        else:
            return f"{res['status']['code']}"


