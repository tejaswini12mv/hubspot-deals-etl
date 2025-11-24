class DataSource:
    def __init__(self, api_service):
        self.api_service = api_service

    def extract_deals(self, tenant_id, properties=None):
        deals = self.api_service.get_deals(properties=properties)
        for deal in deals:
            deal["tenant_id"] = tenant_id
        return deals
