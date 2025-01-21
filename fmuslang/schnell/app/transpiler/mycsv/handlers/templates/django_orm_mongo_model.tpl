from django import forms

class __TEMPLATE_MODELNAME_CASE__Form(forms.ModelForm):
	class Meta:
		model = __TEMPLATE_MODELNAME_CASE__()
		fields = ['title', 'image']
		fields = ('title', 'image')
		fields = '__all__'


from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
__TEMPLATE_MODEL_FIELDS__

class __TEMPLATE_MODELNAME_CASE__Serializer(serializers.ModelSerializer):
	class Meta:
		model = __TEMPLATE_MODELNAME_CASE__
		fields = '__all__'


__IMPORTS__

class __TEMPLATE_MODELNAME_CASE__(models.Model):
__TEMPLATE_MODEL_FIELDS__

  class Meta:
	app_label = '__TEMPLATE_MODELNAME_LOWER__'
	db_table = '__TEMPLATE_MODELNAME_LOWER__s'

  def __str__(self):
	return "{}".format(self.__COLNAME__)
