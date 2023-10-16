from drf_yasg import openapi
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Habits

class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, attrs):
        relhab = attrs.get('relhab')
        nicehab = attrs.get('nicehab')
        reward = attrs.get('reward')
        time_to_act = attrs.get('time_to_act')
        periodic = attrs.get('periodic')

        if time_to_act and time_to_act > 120:
            raise serializers.ValidationError("Время на выполнение привычки указывается в секундах и оно не должно превышать 120")

        if periodic != None and periodic >= 8:
            raise  serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

        if relhab and not nicehab:
            raise serializers.ValidationError("Связанная привычка всегда должна быть приятной")

        if relhab is None and nicehab:
            raise serializers.ValidationError("Не указана связанная привычка")

        if relhab and reward:
            raise serializers.ValidationError("После выполнения связанной привычки нельзя вознаграждать себя")

        return attrs

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token

