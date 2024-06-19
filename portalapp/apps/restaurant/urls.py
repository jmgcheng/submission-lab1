from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurants-home'),
    path('/<int:pk>/', RestaurantDetailView.as_view(), name='restaurants-detail'),

    path('/new/', RestaurantCreateView.as_view(), name='restaurants-create'),

    path('/<int:pk>/update/', RestaurantUpdateView.as_view(),
         name='restaurants-update'),

    path('/<int:pk>/delete/', RestaurantDeleteView.as_view(),
         name='restaurants-delete'),
]
