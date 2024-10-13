from rest_framework import serializers
from .models import DataEntry

class DataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = '__all__'
        read_only_fields = ('id', 'processed_data', 'status', 'created_at', 'updated_at')

# serializer for Processing Request, if you have a separate endpoint to trigger processing.

class ProcessDataSerializer(serializers.Serializer):
    data_id = serializers.IntegerField()








      