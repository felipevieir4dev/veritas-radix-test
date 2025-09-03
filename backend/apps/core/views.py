from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckView(APIView):
    """Health check endpoint."""
    
    def get(self, request):
        return Response({
            'status': 'ok',
            'message': 'Veritas Radix API is running'
        }, status=status.HTTP_200_OK)