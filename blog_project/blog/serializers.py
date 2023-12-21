from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Blog model.

    Serializes the Blog model fields into JSON format.

    Attributes:
        model (Blog): The Blog model class.
        fields (list): The list of fields to be serialized.

    """

    class Meta:
        model = Blog
        fields = ["id", "title", "description", "date", "category"]

    def validate_title(self, value):
        """
        Validate the title field.

        Args:
            value (str): The title value to be validated.

        Returns:
            str: The validated title.

        Raises:
            serializers.ValidationError: If the title is empty or contains invalid characters.
        """
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        """
        Validate the description field.

        Args:
            value (str): The description value to be validated.

        Returns:
            str: The validated description.

        Raises:
            serializers.ValidationError: If the description is empty or exceeds a certain length.
        """
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        if len(value) > 500:
            raise serializers.ValidationError("Description is too long.")
        return value

    def validate_category(self, value):
        """
        Validate the category field.

        Args:
            value (str): The category value to be validated.

        Returns:
            str: The validated category.

        Raises:
            serializers.ValidationError: If the category is not one of the allowed choices.
        """
        allowed_categories = [
            "Tech",
            "Travel",
            "Food",
        ]
        if value not in allowed_categories:
            raise serializers.ValidationError(
                f"Invalid category. Allowed categories: {', '.join(allowed_categories)}"
            )
        return value
