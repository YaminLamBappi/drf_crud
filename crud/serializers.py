from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=355)
    phone = serializers.IntegerField()
    address = serializers.CharField(max_length=56)
    
    def create(self, validate_data):
        return Family.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        
        return instance
    