from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.StudentV.as_view()),
    path('<int>:id',views.StudentID.as_view()),

]
