from django.urls import path
from .views import get_all_blogs, get_blog_by_id, post_blog, update_blog

"""
URL patterns for the blog app.

- /blogs/ : Get all blogs
- /blogs/<int:blog_id>/ : Get blog by ID
- /blogs/ : Post a new blog
- /blogs/<int:blog_id>/ : Update a blog by ID
"""

urlpatterns = [
    path("blogs/", get_all_blogs),
    path("blogs/<int:blog_id>/", get_blog_by_id),
    path("blogs/", post_blog),
    path("blogs/<int:blog_id>/", update_blog),
]
