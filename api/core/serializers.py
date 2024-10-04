from rest_framework import serializers
from .models import Cut, Roll



class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'

class CutSerializer(serializers.ModelSerializer):
    rolls = RollSerializer(many=True)
    class Meta:
        model = Cut
        fields = '__all__'
        
    def create(self, validated_data):
        print(f"validated_data:{validated_data}")
        rolls_data = validated_data.pop('rolls', None)
        cut = Cut.objects.create(**validated_data)
        roll_to_save = []
        if rolls_data:
            for roll_data in rolls_data:
                roll_to_save.append(Roll(cut=cut, **roll_data))
            Roll.objects.bulk_create(roll_to_save)
            
        return cut
        

        
