from django.urls import path,include
from apps.api import views
urlpatterns = [
    path('', include(views.router.urls)),
]
