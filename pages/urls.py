from django.urls import path
from .views import (
    PageListView, PageDetailView,
    PageCreateView, PageUpdateView, PageDeleteView,
)

app_name = 'pages'
urlpatterns = [
    path('', PageListView.as_view(), name='list'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
]
