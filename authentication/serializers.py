from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name', max_length=150, required=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'email': {'required': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists() or User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        name = validated_data.get('first_name', '')
        password = validated_data['password']
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        data['user'] = user
        return data
