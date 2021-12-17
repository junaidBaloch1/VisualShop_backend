from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector
from .serialization import ProductSerializer
from .models import Product
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
# getting models
from .models import Product
# from rest_framework import BasicAuthentication
from visualshop.utility.request import Success
# Create your views here.
class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000



class GetProductsAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
class GetProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class GetProductByCategory(ListAPIView):
    serializer_class = ProductSerializer
    model = Product
    pagination_class = ProductPagination
    def get_queryset(self):
        uid = self.kwargs.get('pk')
        queryset = self.model.objects.filter(subCategoryId__categoryId=uid)
        return queryset
class GetProductBySubCategory(ListAPIView):
    serializer_class = ProductSerializer
    model = Product
    pagination_class = ProductPagination
    def get_queryset(self):
        category = self.kwargs.get('category')
        subcategory=self.kwargs.get('subcategory')
        queryset = self.model.objects.filter(subCategoryId=subcategory,subCategoryId__categoryId=category)
        return queryset

class GetProductByText(ListAPIView):
    serializer_class = ProductSerializer
    model = Product
    pagination_class = ProductPagination
    def get_queryset(self):
        text = self.kwargs.get('text')
        search_vector = SearchVector("tags__name",weight='A') + SearchVector('name', weight='B') + SearchVector('description', weight='C')
        search_query = SearchQuery(text)
        results = Product.objects.annotate(
            rank=SearchRank(search_vector, search_query)
        ).filter(rank__gte=0.3).order_by('-rank')
        return results