from django.urls import path


from api.views import deleteUser, user, users, user_login, user_logout, register_user, user_verification


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
    path('verify/', user_verification, name='verify'),

    path('user/<int:id>/', user, name='getUserById'),
    path('users/', users, name='getAllUsers'),
    path('user/delete/<int:id>/', deleteUser, name='deleteUserById'),
]
