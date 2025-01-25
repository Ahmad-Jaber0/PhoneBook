from rest_framework import serializers
from django.core.validators import RegexValidator, EmailValidator
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = serializers.EmailField(validators=[EmailValidator(message="Invalid email address.")])
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'email', 'created_at']

    def validate_email(self, value):
        value = value.lower()
        if Contact.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_phone_number(self, value):
        if Contact.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        return value


    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value
