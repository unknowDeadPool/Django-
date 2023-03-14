from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S', read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'author', 'created_at', 'text')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['test_fields'] = 'Hello Makers!!!'
        representation['images'] = PostImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation 

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)

        else:
            url = ""
        return url
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


