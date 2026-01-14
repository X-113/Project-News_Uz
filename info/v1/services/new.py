from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from info.models import New
from info.v1.serializers import NewSerializer


class NewView(ListCreateAPIView,UpdateAPIView,DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewSerializer
    queryset = New.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.queryset.filter(id=pk).first()
            if not obj:
                raise NotFound('Yangilik topilmadi!')
            else:
                return Response(obj.response())

        else:
            return super(NewView, self).get(request, *args, **kwargs)

