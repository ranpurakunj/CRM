from django.urls import path

from . import views

# /api/profile/
urlpatterns = [
    path('', views.profile_list_create_view, name='profile-list-create'),
    path('<int:pk>/', views.profile_detail_view, name='profile-detail'),
    path('<int:pk>/update/', views.profile_update_view, name="profile-edit"),
    path('<int:pk>/delete/', views.profile_delete_view)
]
