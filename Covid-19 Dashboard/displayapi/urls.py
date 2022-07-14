
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('Country/<str:Country>', views.inner, name = "inner")
]
