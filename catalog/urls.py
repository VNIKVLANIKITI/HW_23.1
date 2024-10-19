from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('blog', ArticleListView.as_view(), name='articles_list'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('blog/create', ArticleCreateView.as_view(), name='articles_create'),
    path('blog/<int:pk>/update/', ArticleUpdateView.as_view(), name='articles_update'),
    path('blog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles_delete')
]
