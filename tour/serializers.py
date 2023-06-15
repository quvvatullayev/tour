from rest_framework import serializers
from .models import (
    Exclusive,
    About_company,
    News,
    Commit,
    Appeal,
    Contact,
    User,
)

class ExclusiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusive
        fields = '__all__'

class About_companySerializer(serializers.ModelSerializer):
    class Meta:
        model = About_company
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = '__all__'

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
