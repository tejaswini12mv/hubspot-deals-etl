import requests

class HubSpotAPIService:
    BASE_URL = "https://api.hubapi.com"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_deals(self, limit=100, properties=None, after=None):
        url = f"{self.BASE_URL}/crm/v3/objects/deals"
        params = {
            "limit": limit,
            "properties": ",".join(properties) if properties else None,
            "after": after
        }
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"HubSpot API Error: {response.status_code} {response.text}")
        return response.json().get("results", [])
