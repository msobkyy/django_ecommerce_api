from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, ProductSerializer, CategorysSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import mixins
from .models import Product, Categorys
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint : view, edit
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response(products)

    def post(self, request):
        return Response({'data': request.data})


class ProductGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, **args):
        return self.list(request,**args)

    def post(self, request, **args):
        return self.create(request,**args)

class CategorysGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorysSerializer

    def get(self, request, **args):
        return self.list(request,**args)

    def post(self, request, **args):
        return self.create(request,**args)