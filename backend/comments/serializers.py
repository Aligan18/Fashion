from rest_framework import serializers

from comments.models import Comments


class CreateCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class AboutCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'