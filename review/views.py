from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from book.models import Book

# Create your views here
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.request.query_params.get('book_id')
        if book_id is None:
            return Review.objects.none()

        try:
            # Filter reviews by the provided book ID
            queryset = Review.objects.filter(book_id=book_id)
        except Review.DoesNotExist:
            return Response({"message": "Reviews not found for the given book ID"}, status=status.HTTP_404_NOT_FOUND)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Ensure user is authenticated
        if not request.user.is_authenticated:
            return Response({"message": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch the book instance from the database
        book_id = request.data.get('book')
        try:
            book_instance = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already reviewed the book
        existing_review = Review.objects.filter(user=request.user, book=book_instance).exists()
        if existing_review:
            return Response({"message": "User has already reviewed this book"}, status=status.HTTP_400_BAD_REQUEST)

        # Assign the book instance to the review
        serializer.validated_data['book'] = book_instance

        # Assign the reviewer
        serializer.validated_data['user'] = request.user

        # Save the review
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)




