from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import MultipleFieldLookupMixin
from .models import *
from .pagination import BookLimitOffsetPagination, BookSearchOffsetPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    BookCreateUpdateSerializer,
    BookListSerializer,
    BookDetailSerializer,
)


# Create your views here.
class CreateBookAPIView(APIView):
    """
    Book:
        Creates a new Book instance. Returns created Book data

        parameters: [title, body, description, image]
    """

    queryset = Books.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = BookCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListBookAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing Books
    """

    queryset = Books.objects.all().order_by('pk')
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BookLimitOffsetPagination


class DetailBookAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a Book instance. Searches Book using pk field.

    put:
        Updates an existing Book. Returns updated Book data

        parameters: [title, body, description, image]

    delete:
        Delete an existing Book

        parameters = [pk]
    """

    queryset = Books.objects.all()
    lookup_field = "pk"
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SearchView(ListAPIView):
    """
    get:
        Returns a list of all searched Books
    """
    serializer_class = BookListSerializer
    pagination_class = BookSearchOffsetPagination

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        q = self.request.query_params.get("q")
        if q:
            search_vector = SearchVector("title", weight="A") + SearchVector("author", weight="B") + SearchVector(
                "publisher", weight="C")

            search_query = SearchQuery(q)
            return Books.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(
                search=q).order_by(
                '-rank')
