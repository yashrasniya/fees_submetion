from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Student
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse


class student_login_serializers(ModelSerializer):

    class Meta:
        model = Student
        fields = ('mobile_number', 'password','father_name','batch','branch')


class student_data_serializers(ModelSerializer):
    token= serializers.SerializerMethodField()
    status = serializers.IntegerField(default=200)

    class Meta:
        model = Student
        fields = ('mobile_number', 'father_name', 'batch', 'branch', 'roll_number', 'status', 'email','token')
    def get_token(self,obj):
        refresh=RefreshToken.for_user(obj)
        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }