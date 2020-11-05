from rest_framework import serializers
from api.models import User, Profile, Education, Experience, Feed, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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

class UserProfileSerializer(serializers.ModelSerializer):

    user_profile = ProfileSerializer()


    class Meta:
        model = User
        fields = "__all__"

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = "__all__"



class UserFriendSerializer(serializers.ModelSerializer):

    user_friendrequest = FriendRequestSerializer()
    

    class Meta:
        model = User
        fields = "__all__"
















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

