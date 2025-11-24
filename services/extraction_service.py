from .data_source import DataSource
from .hubspot_api_service import HubSpotAPIService

class ExtractionService:
    def __init__(self, token):
        self.api_service = HubSpotAPIService(token)
        self.data_source = DataSource(self.api_service)

    def start_scan(self, tenant_id, properties=None):
        deals = self.data_source.extract_deals(tenant_id, properties=properties)
        return {
            "scan_id": "uuid-placeholder",
            "status": "started",
            "deals": deals
        }
