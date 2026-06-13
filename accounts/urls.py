from django.urls import path, include


app_name = 'accounts'
urlpatterns = [
    # Додаємо URL авторизації за замовчуванням
    path('', include('django.contrib.auth.urls'))
]
