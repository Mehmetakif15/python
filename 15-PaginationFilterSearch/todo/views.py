from rest_framework.viewsets import ModelViewSet

from .serializers import Todo, TodoSerializer

from .paginations import (CustomPageNumberPagination, CustomLimitOffsetPagination,CustomCursorPagination)

# from rest_framework.pagination import PageNumberPagination
# from rest_framework.pagination import LimitOffsetPagination


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoView(ModelViewSet):
    queryset = Todo.objects.all().order_by('-id') # Default ordering
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Pagination Setting.
    # Filtreleme Modülleri:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # Local Filter Setting.
    # Filter: Birebir eşleştirme:
    filterset_fields = ['id', 'priority', 'is_done'] # for django_filters module
    # Search: İçinde arama:
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    search_fields = ['title', 'description']
    # Ordering: Sıralama:
    ordering_fields = ['id', 'title'] # '__all__'
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class TodoView(ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     pagination_class = CustomPageNumberPagination
#     # pagination_class = LimitOffsetPagination
#     # pagination_class = CustomLimitOffsetPagination
#     # pagination_class = CustomCursorPagination


    # Alternatif yontem
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'adet'  # URL ile
    # PageNumberPagination.page_query_param = 'sayfa'

'''
    def get_queryset(self):
        # URL'den parametre değerini yakala:
        title = self.request.query_params.get('title')
        if title is None:
        # Arama yapma (parametre yok)
            return super().get_queryset()
        else:
        # Arama yap:
            # queryset içinde ara:
            return self.queryset.filter(title__contains=title)
'''