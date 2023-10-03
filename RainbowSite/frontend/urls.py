
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('gallery', views.gallery, name = 'gallery' ),
    path('result', views.results, name = 'result' ),
    path('user-home/', views.user_home, name = 'user_home' ),
    path('blog/', views.my_blog, name = 'blog' ),
    path('delete/<int:id>', views.delete, name = 'delete' ),
    path('deactivate/', views.deactivateView, name = 'deactivateView' ),
    path('activate/', views.activateView, name = 'activateView' ),
    path('delete/', views.deleteResult, name = 'deleteResult' ),
]
