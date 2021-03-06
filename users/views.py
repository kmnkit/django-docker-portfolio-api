import jwt
from func import get_secret
from django.contrib.auth import authenticate, logout
from rest_framework import views
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_object(self):
        id = self.kwargs["pk"]
        return self.get_queryset().get(id=id)

    @action(detail=False, methods=["post"])
    def custom_logout(self, request):
        logout(request)
        data = {"success": "성공적으로 로그아웃 되었습니다."}
        return Response(data=data, status=status.HTTP_200_OK)


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data

        email = data.get("email", None)
        password = data.get("password", None)

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                encoded_jwt = jwt.encode(
                    {"pk": user.pk}, get_secret("SECRET_KEY"), algorithm="HS256"
                )
                return Response(data={"token": encoded_jwt, "id": user.pk})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
