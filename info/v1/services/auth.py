from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from info.auth_models import User
from info.utils import password_validation, BearerAuth


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        if  "phone" not in data or "password" not in data:
            return Response(
                {
                    "error":"phone va password kirib kelsin!"
                }, status=HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(phone=data['phone']).first()
        if not user:
            return Response(
                {
                    "error": "Bunaqa user mavjud emas"
                }, status=HTTP_404_NOT_FOUND
            )
        if not user.is_active:
            return Response(
                {
                    "error":"Ushbu user active emas yoki ban qilingan bo'lishi mumkin!"
                }, status=HTTP_403_FORBIDDEN
            )

        if not user.check_password(data['password']):
            return Response(
                {
                    "error":"Login yoki parol xato!"
                }
            )

        token = Token.objects.get_or_create(user=user)[0]  # natija=tuple(obj,status)

        return Response(
            {
                "access_token": token.key
            }, status=HTTP_200_OK
        )

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get("password")
        age = request.data.get("age")
        gender = request.data.get("gender")

        if None in [phone,password,age,gender]:
            return Response({
                "error":"phone, password, age, gender required"
            }, status=HTTP_400_BAD_REQUEST)

        user = User.objects.filter(phone=phone).first()
        if user:
            return Response({
                "error": "Phone allaqachon mavjud"
            }, status=HTTP_403_FORBIDDEN)

        # parol tekshiramiz:
        password_validation(password)

        user = User.objects.create_user(**request.data)

        token = Token.objects.create(user=user)

        return Response({
            "message": "User registered successfully",
            "access_token": token.key
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuth]

    def post(self, request):
        Token.objects.get(user=request.user).delete()
        return Response({
            "message": "User logged out"
        })


