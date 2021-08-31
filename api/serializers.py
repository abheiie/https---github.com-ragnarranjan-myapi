from rest_framework import fields, serializers
from .models import Course
from rest_framework import serializers

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'        


    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, course, validated_data):
        course.Name = validated_data.get('Name',course.Name)
        course.Price = validated_data.get('Price',course.Price)
        course.Discount = validated_data.get('Discount',course.Discount)
        course.Duration = validated_data.get('Duration',course.Duration)
        course.AuthorName = validated_data.get('AuthorName',course.AuthorName)
        course.save()
        return course