from rest_framework import serializers

from info.models import Category
from info.models import Contact
from info.models import Comment
from info.models import New
from info.models import Subscription

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'



