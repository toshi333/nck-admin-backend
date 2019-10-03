from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'code', 'name', 'category', 'customer', 'team', 'description', 'estimate_price', 'estimate_date', 'closed_flg')
        read_only_fields = ('created_at', 'updated_at')
        