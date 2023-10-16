from drf_yasg.utils import swagger_auto_schema

from .pagination import HabitsPagination
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Habits
from .serializers import HabitsSerializer, MyTokenObtainPairSerializer


def index(request):
    return render(request, "habits/index.html")


class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Habits.objects.filter(user=user)

    @swagger_auto_schema(
        operation_description="Create a new habit",
        request_body=HabitsSerializer,
        responses={201: HabitsSerializer()},
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'user': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Update an existing habit",
        request_body=HabitsSerializer,
        responses={200: HabitsSerializer()},
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'user': request.user.id})
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

class HabitsList(generics.ListCreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    data = {
        'id': user.id,
        'email': user.email,
    }
    return Response(data)


class CustomAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
