from rest_framework import serializers
from api.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
'''
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = "__all__"
'''
class UserSerializer(serializers.ModelSerializer):
    '''def validated_password(self, value):
        return make_password(value)
'''

    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_fields = 'profile'

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
        )

        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user = user,
            selfie_image = profile_data['selfie_image'],
            bio = profile_data['bio'],
            headline = profile_data['headline']
            
        )

        return user

