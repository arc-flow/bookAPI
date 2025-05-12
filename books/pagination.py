from rest_framework.pagination import (
    LimitOffsetPagination,
)


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 20


class BookSearchOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5
