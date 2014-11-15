from django.forms import widgets
from rest_framework import serializers
from calc.models import Calc

class CalcSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Calc
    fields = ('value', 'number', 'occurencies', 'created_on', 'updated_on')

