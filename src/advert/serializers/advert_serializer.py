from rest_framework import serializers


class AdvertSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)
    city = serializers.CharField(source="city.name", read_only=True)
    views = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    is_deleted = serializers.BooleanField(read_only=True)
