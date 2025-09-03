from django.http import JsonResponse
from django.core.cache import cache
import time


class RateLimitMiddleware:
    """Simple rate limiting middleware."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get client IP
        client_ip = self.get_client_ip(request)
        
        # Check rate limit
        cache_key = f"rate_limit_{client_ip}"
        requests = cache.get(cache_key, 0)
        
        if requests >= 100:  # 100 requests per minute
            return JsonResponse(
                {'error': 'Rate limit exceeded'}, 
                status=429
            )
        
        # Increment counter
        cache.set(cache_key, requests + 1, 60)  # 1 minute
        
        response = self.get_response(request)
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip