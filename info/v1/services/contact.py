from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from info.models import Contact
from rest_framework.exceptions import NotFound

from info.v1.serializers import ContactSerializer


class ContactView(ListCreateAPIView, UpdateAPIView,DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


    def get(self,request, pk=None, *args, **kwargs):
        if pk:
            obj = self.queryset.filter(id=pk).first()
            if not obj:
                raise NotFound("Kontakt yo'q")
            else:
                return Response(obj.response())

        else:
            return super(ContactView, self).get(request, *args, **kwargs)









