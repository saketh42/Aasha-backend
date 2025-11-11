from rest_framework import serializers
from .models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['username', 'password', 'email']


class PostingSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Posting
        fields = ['name','age', 'email', 'problem','amount','image','upi']
    
