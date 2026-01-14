from django.template import Library
from django.db.models import Q



register = Library()

@register.filter
def filters(queryset, attrs, *args):
    split = attrs.split("-")
    kalit = split[0]
    qiymat = split[1]
    son = split[2]
    qidiruv = {
        kalit: qiymat
    }

    natija = queryset.filter(Q(**qidiruv))[:int(son)]
    return natija


