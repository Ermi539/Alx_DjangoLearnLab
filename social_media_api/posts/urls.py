from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('<int:post_id>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:post_id>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]