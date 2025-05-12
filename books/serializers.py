from rest_framework import serializers
from .models import Books


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            "title",
            "author",
            "publisher",
            "category",
            "image"
        ]

    def validate_title(self, value):
        if len(value) > 100:
            return serializers.ValidationError("Max title length is 100 characters")
        return value

    def validate_description(self, value):
        if len(value) > 200:
            return serializers.ValidationError(
                "Max description length is 200 characters"
            )
        return value


class BookListSerializer(serializers.ModelSerializer):
    # loans = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Books
        fields = [
            "pk",
            "title",
            "publisher",
            "image",
            "category",
            "rating",
        ]

        # def get_loans(self, obj):
        #     qs = Loans.objects.filter(book=obj).count()
        #     return qs


class BookDetailSerializer(serializers.ModelSerializer):
    # loans = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Books
        fields = "__all__"

    # def get_loans(self, obj):
    #     qs = Loans.objects.filter(parent=obj)
    #     try:
    #         serializer = LoansSerializer(qs, many=True)
    #     except Exception as e:
    #         print(e)
    #     return serializer.data


# class LoansSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Loans
#         fields = "__all__"


# class LoansCreateUpdateSerializer(serializers.ModelSerializer):
#     book = serializers.SlugRelatedField(slug_field='name')
#     class Meta:
#         model = Loans
#         fields = [
#             "book",
#         ]
