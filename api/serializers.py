from rest_framework import serializers

from api  import models

class HelloSerializers(serializers.Serializer):
	name = serializers.CharField(max_length=10)

class StudSerializers(serializers.ModelSerializer):
	class Meta:
		model = models.Stud
		fields = ['id', 'name', 'email', 'password']
		extra_kwargs = {
			'password': {
				'write_only': True,
				'style': {
					'input_type': 'password'
				}
			}
		}

	def create(self, validated_data):
		user = models.Stud.objects.create_user(
			name = validated_data['name'],
			email = validated_data['email'],
			password = validated_data['password'],)
		return user

class StudProfileSerializers(serializers.ModelSerializer):
	class Meta:
		model = models.StudProfile
		fields = ['id', 'user_profile', 'status_text']
		extra_kwargs = {
			'user_profile': {'read_only': True}
		}