from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_or_post),
    path('<int:id>/',views.get_or_put_or_delete)
]