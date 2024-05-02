from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/edit/<int:blog_id>/', views.edit, name='edit'),
    path('blog/update/<int:blog_id>/', views.update, name='update'),
    path('blog/delete/<int:blog_id>/', views.delete, name='delete'),
    path('blog/create_comment/<int:blog_id>', views.create_comment, name = 'create_comment'),
    path('blog/new_comment/<int:blog_id>', views.new_comment, name = 'new_comment'),
    path('profile/<int:profile_id>/', views.profile, name = 'profile'),
    path('profile/edit/<int:profile_id>/', views.edit_profile, name = 'edit_profile'),
    path('profile/update/<int:profile_id>/', views.update_profile, name = 'update_profile'),
    path('<int:blog_id>/like/', views.like, name='like'),
]