from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer


@api_view(["GET"])
def get_all_blogs(request):
    """
    Retrieve all blogs.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The HTTP response object containing serialized blog data.
    """
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_blog_by_id(request, blog_id):
    """
    Retrieve a blog by its ID.

    Parameters:
    - request: The HTTP request object.
    - blog_id: The ID of the blog to retrieve.

    Returns:
    - Response: The HTTP response object containing serialized blog data.
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(["POST"])
def post_blog(request):
    """
    Create a new blog.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The HTTP response object containing serialized blog data if successful,
                or error messages if the request data is invalid.
    """
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_blog(request, blog_id):
    """
    Update an existing blog.

    Parameters:
    - request: The HTTP request object.
    - blog_id: The ID of the blog to update.

    Returns:
    - Response: The HTTP response object containing serialized blog data if successful,
                or error messages if the request data is invalid.
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
