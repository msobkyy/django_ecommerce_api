from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'categorys', views.CategorysViewSet, basename='categorys')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('products/', views.ProductGenericView.as_view(), name='products'),
    path('categorys/', views.CategorysGenericView.as_view(), name='categorys'),

]
