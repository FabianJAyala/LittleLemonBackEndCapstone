from django.urls import path
from .views import index, MenuView, BookingView, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('booking/', BookingView.as_view()),
    path('menu-items', MenuView.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]