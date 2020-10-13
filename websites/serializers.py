from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryLink
    fields = ("category_name","category_img","parent")

class LinkListSerializer(serializers.ModelSerializer):
    link_category = CategorySerializer()
    link_logo = serializers.ImageField()
    class Meta:
      model = LinkModel
      fields = ("link_domain","link_title","link_category","link_logo","visited_people_number_on_last_month","created_time")