from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Order
        fields=('user')
        #Todo: add products and quantity