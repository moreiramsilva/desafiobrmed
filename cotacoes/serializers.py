from rest_framework import serializers

class BrlSerializer(serializers.Serializer):
    date = serializers.DateField()
    base = serializers.CharField() 
    brl = serializers.FloatField()
    
class EurSerializer(serializers.Serializer):
    date = serializers.DateField()
    base = serializers.CharField() 
    eur = serializers.FloatField()
    
class JpySerializer(serializers.Serializer):
    date = serializers.DateField()
    base = serializers.CharField() 
    jpy = serializers.FloatField()
    
