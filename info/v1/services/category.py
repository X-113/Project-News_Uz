from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK

from info.models import Category
from info.v1.serializers import CategorySerializer
from info.utils import BearerAuth

# APIView -> model shart bo'lmaganda ishlatilar ekan.

class CategoryView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerAuth]
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk).response(ctg_one=True)
        except:
            raise NotFound("Categoriya topilmadi!")

    def get(self,request,pk=None):
        print("user", request.user)
        if pk:
            natija = self.get_object(pk)
        else:
            ctgs = Category.objects.all()
            natija = []
            for i in ctgs:
                natija.append(i.response())

        return Response(natija, status=200)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Yangi Ctg qo'shildi"
        }, status=HTTP_200_OK)

    def put(self, request, pk):
        one_ctg = Category.objects.filter(id=pk).first()
        if not one_ctg:
            raise NotFound('Category topilmadi!')

        serializer = self.serializer_class(data=request.data, instance=one_ctg)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message":"Categoriya O'zgartirildi",
            "ctg": one_ctg.response(ctg_one=True)
        }, status=HTTP_200_OK)

    def patch(self, request, pk):
        one_ctg = Category.objects.filter(id=pk).first()
        if not one_ctg:
            raise NotFound('Category topilmadi!')

        serializer = self.serializer_class(data=request.data, instance=one_ctg, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Categoriya O'zgartirildi",
            "ctg": one_ctg.response(ctg_one=True)
        }, status=HTTP_200_OK)

    def delete(self,request, pk):
        # tanlab o'chirish uchun Q ishlatilinadi:Category.objects.filter(Q(id__in=request.data['ids'])).delete()
        try:
            Category.objects.filter(id=pk).first().delete()
        except: ...

        return Response(
            {
            "message": "Categoriya o'chirib yuborildi"
            }
        )




