from django.urls import path, include

# Define the main URL patterns for the backend project
urlpatterns = [
    path('api/', include('api.urls')),
]