from django.urls import path
from . import views
from .views import BlogViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', BlogViewset, base_name='blogviewset')

urlpatterns = [
    #path('',views.post_list ,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('api/<int:pk>', views.BlogDetail.as_view()),
    path('apilist/<int:pk>', views.BlogList.as_view()),

] + router.urls

