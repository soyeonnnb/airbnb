from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
