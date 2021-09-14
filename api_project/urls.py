from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_project.views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView, ArticleViewSet

# ViewSets
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    # APIViews
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetailsAPIView.as_view()),

    # GenericViews
    path('generic/article/', GenericAPIView.as_view()),

    # ViewSets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
