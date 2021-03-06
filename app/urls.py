from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/blog',views.BlogListView.as_view(),name='blog'),
    path('/blog/<int:pk>',views.BlogDetailView.as_view(),name='blog_detail')
]
