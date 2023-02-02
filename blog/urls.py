from django.urls import path
from . import views

urlpatterns = [
    path('/search/<str:q>/', views.PostSearch.as_view()),
    path('/tag/<str:slug>/', views.tag_page),
    path('/<int:pk>/new_comment/', views.new_comment),
    path('/update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('/create_post/', views.PostCreate.as_view()),
    path('/<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]