
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError


class BearerAuth(TokenAuthentication):
    keyword = "Bearer"




def password_validation(password):
    if 6 <= len(password) <= 15:
        element = {
            'katta': 0,
            'kichik': 0,
            'son': 0,
            'sym': 0
        }
        for i in password:
            if i.isupper():
                element['katta'] += 1
            elif i.islower():
                element['kichik'] += 1
            elif i.isdigit():
                element['son'] += 1
            elif not i.isalnum():
                element['sym'] += 1

        if element['katta'] == 0:
            raise ValidationError("Eng kamida katta harf bo'lsin!")
        elif element['kichik'] == 0:
            raise ValidationError("Ey kamida kichik harf bo'lsin!")
        elif element['son'] == 0:
            raise ValidationError("Ey kamida 1ta son bo'lsin!")
        elif element['sym'] == 0:
            raise ValidationError("Ey kamida 1ta symbol bo'lsin!")
        else:
            return True
    else:
        raise ValidationError("Uzunlik 6dan 15gacha bo'lsin!")


