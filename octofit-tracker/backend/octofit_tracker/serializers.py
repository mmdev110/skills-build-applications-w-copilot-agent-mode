from bson import ObjectId
from rest_framework import serializers

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class ObjectIdSerializerField(serializers.Field):
    def to_representation(self, value):
        return str(value) if value else None

    def to_internal_value(self, data):
        try:
            return ObjectId(str(data))
        except Exception as exc:
            raise serializers.ValidationError("Invalid ObjectId") from exc


class TeamSerializer(serializers.ModelSerializer):
    mongo_id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = Team
        fields = ['mongo_id', 'name']
        read_only_fields = ['mongo_id']


class UserSerializer(serializers.ModelSerializer):
    mongo_id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = User
        fields = ['mongo_id', 'name', 'email', 'team']
        read_only_fields = ['mongo_id']


class ActivitySerializer(serializers.ModelSerializer):
    mongo_id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = Activity
        fields = ['mongo_id', 'user', 'type', 'duration', 'date']
        read_only_fields = ['mongo_id']


class WorkoutSerializer(serializers.ModelSerializer):
    mongo_id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = Workout
        fields = ['mongo_id', 'name', 'description', 'suggested_for']
        read_only_fields = ['mongo_id']


class LeaderboardSerializer(serializers.ModelSerializer):
    mongo_id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['mongo_id', 'user', 'score']
        read_only_fields = ['mongo_id']
