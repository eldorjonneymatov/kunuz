from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (
    TextNewsList, TextNewsRetrieve,
    TextNewsCreate, TextNewsUpdate,
    TextNewsDestroy, AudioNewsList,
    AudioNewsRetrieve, AudioNewsCreate,
    AudioNewsUpdate, AudioNewsDestroy,
    NewsByCategory, NewsByRegion
)

app_name = 'news'

urlpatterns = [
    path('news/', TextNewsList.as_view(), name='news-list'),
    path('news/create/', TextNewsCreate.as_view(), name='news-create'),
    path('news/<int:pk>/', TextNewsRetrieve.as_view(), name='news-retrieve'),
    path('news/<int:pk>/delete/', TextNewsDestroy.as_view(), name='news-destroy'),
    path('news/<int:pk>/update/', TextNewsUpdate.as_view(), name='news-update'),

    path('audio/', AudioNewsList.as_view(), name='audio-list'),
    path('audio/create/', AudioNewsCreate.as_view(), name='audio-create'),
    path('audio/<int:pk>/', AudioNewsRetrieve.as_view(), name='audio-retrieve'),
    path('audio/<int:pk>/delete/', AudioNewsDestroy.as_view(), name='audio-delete'),
    path('audio/<int:pk>/update/', AudioNewsUpdate.as_view(), name='audio-update'),

    path('category/<str:category>/', NewsByCategory.as_view(), name='news-category'),
    path('region/<str:region>/', NewsByRegion.as_view(), name='news-region'),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name='news:schema'), name="swagger-ui"),
]