from django.urls import path
from . import views
urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('article/detail/<int:pk>',views.postDetail.as_view(),name='postDetail'),
]