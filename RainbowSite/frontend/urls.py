
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('gallery', views.gallery, name = 'gallery' ),
    path('result', views.result, name = 'result' ),
    path('user-home/', views.user_home, name = 'user_home' ),
    path('blog/', views.my_blog, name = 'blog' ),
    path('delete/<int:id>', views.delete, name = 'delete' ),
]
