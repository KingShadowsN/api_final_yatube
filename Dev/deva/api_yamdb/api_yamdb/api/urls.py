from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, sign_up,
                       token)

app_name = 'api'

router = SimpleRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')

router.register(
    r'categories',
    CategoryViewSet,
    basename='сategories'
)
router.register(
    r'genres',
    GenreViewSet,
    basename='genres'
)
router.register(
    r'titles',
    TitleViewSet,
    basename='titles'
)
router.register(
    r'users',
    UserViewSet,
    basename='users'
)

auth_patterns = [
    path('signup/', sign_up),
    path('token/', token),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_patterns)),
]
