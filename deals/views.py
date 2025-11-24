from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def start_scan(request):
    return Response({
        "scan_id": "uuid",
        "status": "started",
        "message": "ETL scan initiated successfully"
    })

@api_view(['GET'])
def get_scan_results(request, scan_id):
    return Response({
        "scan_id": scan_id,
        "status": "completed",
        "total_records": 1,
        "deals": [
            {
                "deal_id": 12345,
                "deal_name": "Test Deal 1",
                "amount": 1000.0,
                "pipeline": "default",
                "stage": "closedwon",
                "owner_id": 111,
                "created_at": "2025-11-01T10:00:00Z",
                "closed_at": "2025-11-15T12:00:00Z"
            }
        ]
    })
