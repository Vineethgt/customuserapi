from rest_framework import serializers
from api.models import User, Profile, Education, Experience, Feed

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    def validated_password(self, value):
        return make_password(value)

    profile = ProfileSerializer(required=True)
  
    class Meta:
        model = User
        fields = '__all__'
        extra_fields = 'profile',

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

















#User Serializer
    '''def validated_password(self, value):
        return make_password(value)


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
'''

