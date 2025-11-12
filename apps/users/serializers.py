from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'password',
            'email',
        ]
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            # full_name = validated_data.get('full_name', ""),
            # phone_number = validated_data.get('phone_number', '')
            # avatar = validated_data.get('avatar', None),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
