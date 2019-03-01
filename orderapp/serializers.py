from rest_framework import serializers
from orderapp.models import Menu, UserObjects
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        #url = serializers.HyperlinkedIdentityField(view_name='menu-list', read_only=True)
        fields = ('item', 'price','image')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserObjects
        user = serializers.ReadOnlyField(source='owner.username')
        fields = ('item', 'user', 'like_status', 'date_liked')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        #quantity = serializers.ReadOnlyField()
        fields =('item', 'price')

"""

class UserSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=True, queryset=Menu.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'menu')

"""