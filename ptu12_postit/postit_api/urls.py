from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/like/', views.PostLikeCreateDestroy.as_view()),
    path('<int:post_pk>/comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('comment/<int:pk>/like/', views.CommentLikeCreateDestroy.as_view()),
]
