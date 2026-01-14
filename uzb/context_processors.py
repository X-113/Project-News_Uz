import requests as re
from info.models import Category,New


def valyuta():
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
    response = re.get(url).json()
    return response


def main(request):
    ctgs = Category.objects.filter(is_menu=True)

    return {
        "ctgs": ctgs,
        # "valyuta": valyuta(),
        "fresh_news": New.objects.all().order_by('-id')[:8]
    }






