from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from info.models import Subscription
from info.v1.serializers import SubscriptionSerializer


class SubscriptionView(ListCreateAPIView,UpdateAPIView,DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.queryset.filter(id=pk).first()
            if not obj:
                raise NotFound("Obunachi Yo'q")
            else:
                return Response(obj.response())

        return super(SubscriptionView, self).get(request, *args, **kwargs)

