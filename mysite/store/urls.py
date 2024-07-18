from django.urls import path
from .views import CategoryViewSet, ProductViewSet, CommentViewSet


urlpatterns = [
    path('category', CategoryViewSet.as_view({'get':'list', 'post':'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'post':'update', 'delete': 'destroy'}), name='category_detail'),

    path('product', ProductViewSet.as_view({'get': 'list'}), name='product_list'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product_detail'),

    path('comment/', CommentViewSet.as_view({'get':'list', 'post':'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'post':'update', 'delete': 'destroy'}), name='comment_detail'),

]