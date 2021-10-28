from django.urls import path

from .views import TaggedItemListView, TaggItemDetailView


urlpatterns = [
    path('', TaggedItemListView.as_view()),
    path('<slug:tag>/', TaggItemDetailView.as_view()),
]