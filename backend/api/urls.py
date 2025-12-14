from django.urls import path
from .views import *

# Define URL patterns for the API endpoints
urlpatterns = [
   path('signup/', signup),
path('login/', login),
path('post/', create_post),
path('posts/', all_posts),
path('follow/', follow_user),
path('feed/<str:user_id>/', feed),
path('like/', like_post),
path('comment/', add_comment),
]