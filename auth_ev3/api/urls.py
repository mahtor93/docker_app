from django.urls import path

from api.views import deleteUser, user, users


urlpatterns = [
    path('login/', ''),
    path('logout/', ''),
    path('register/', ''),

    path('user/<int:id>/', user, name='getUserById'),
    path('users/', users, name='getAllUsers'),
    path('user/delete/<int:id>/', deleteUser, name='deleteUserById'),
]
