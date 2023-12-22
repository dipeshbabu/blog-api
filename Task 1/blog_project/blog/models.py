from django.db import models


class Blog(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the blog post.
        description (str): The description of the blog post.
        category (str): The category of the blog post.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.title
