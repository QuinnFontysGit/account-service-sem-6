from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        return instance
