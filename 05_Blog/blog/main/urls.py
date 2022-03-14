from django.urls import path
from . import views
urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('article/create',views.postCreate.as_view(),name='postCreate'),
    path('article/detail/<int:pk>',views.postDetail.as_view(),name='postDetail'),
    path('article/update/<int:pk>',views.postUpdate.as_view(),name='postUpdate'),
    path('article/delete/<int:pk>',views.postDelete.as_view(),name='postDelete'),
]