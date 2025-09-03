"""
Etymology URLs for Veritas Radix application.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EtymologyAnalysisViewSet,
    ImageGenerationViewSet,
    BookmarkViewSet,
    analyze_etymology,
    featured_words
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'analyses', EtymologyAnalysisViewSet, basename='etymology-analysis')
router.register(r'images', ImageGenerationViewSet, basename='image-generation')
router.register(r'bookmarks', BookmarkViewSet, basename='bookmarks')

urlpatterns = [
    # Custom endpoints for frontend compatibility
    path('analyze/', analyze_etymology, name='analyze-etymology'),
    path('featured/', featured_words, name='featured-words'),
    
    # Include router URLs
    path('', include(router.urls)),
]