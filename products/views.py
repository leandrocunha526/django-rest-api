from .serializers import ProductSerializer, ImageSerializer
from .models import Product, Image
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filterset_fields = ('category',)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_releated('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_releated('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_releated('sites')

        if is_expanded(self.request, 'sites.company'):
            queryset = queryset.prefetch_releated('sites.company')

        if is_expanded(self.request, 'sites.productsize'):
            queryset = queryset.prefetch_releated('sites.productsize')

        return queryset


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
