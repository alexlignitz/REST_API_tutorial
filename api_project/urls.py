from django.urls import path

from api_project.views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]
