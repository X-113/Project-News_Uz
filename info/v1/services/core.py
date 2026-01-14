from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class TestView(APIView):
    permission_classes = [AllowAny]


    def get(self, request):

        matematika = 11 + 11

        ctx = {
            "natija": "Salom API",
            "javob": matematika
        }

        return Response(ctx, status=HTTP_200_OK)

    def post(self, request):
        data = request.data
        ism = data.get('name', None)
        if not ism:
            return Response({
                "error": "Name kirib kelsin"
            }, status=400)

        return Response({
            "ma'lumot":"Zapros yuborilyabti...",
            "xabar":"frontdan ma'lumot keldi",
            "kelgan_data": data
        }, status=HTTP_200_OK)

    def put(self, request, pk):
        data = request.data

        return Response({
            "natija":"Bu put zaprosi",
            "id":pk,
            "frontdan_kelgan":data
        }, status=200)







