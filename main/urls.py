from django.urls import path
from main import views


urlpatterns = [
### Первый способ ###

    path('categories/', views.categories, name='categories-list'),

### Второй способ ###

    path('posts/', views.PostListView.as_view(), name='posts-list'),

### Третий способ ###

    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='posts-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='posts-create'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='posts-update'),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view(), name='posts-delete'),

### Четвёртый способ ###
]
