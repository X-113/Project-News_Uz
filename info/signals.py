from time import strftime

from django.core.mail import send_mail
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import Comment, Category, New, Subscription, Contact
import requests
from django.conf import settings
import datetime

@receiver(post_save, sender=Comment)
def test_signal(sender,created,instance,**kwargs):
   if created:
       qabul_qiluvchilar = [
           'bdavlatxojayev@gmail.com',
           'azizbaxtiyorov674@gmail.com'
       ]

       message = f"""Saytga Yangi Izoh Qo'shildi
       Yangilik: {instance.new.title}
       User: {instance.user}
       Xabar: {instance.message}
       Sana: {datetime.datetime.now()}
        
       """

       send_mail(
           subject="Yangi Koment Qo'shildi",
           message=message,
           from_email=settings.EMAIL_HOST_USER,
           recipient_list=qabul_qiluvchilar
           )




@receiver(post_save, sender=Subscription)
def subs_signal(sender, created, instance, **kwargs):
    if created:
        message = f"news.uz saytimizda Yangi obunachi:\n <b>{instance.email}</b>"
        token = "8225709661:AAF6aZfcKDZXbLRCnxCvob6V3jhLX7Cku-U"
        user_ids = [2068375686, 6492515202, 61584199, 1963029843]

        for user_id in user_ids:
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={message}&parse_mode=HTML"
            requests.get(url)


@receiver(post_save, sender=New)
def news_signal(sender,created,instance: New,**kwargs):
    if created:
        message = f"""Saytimizda Yangi YAngilik qo'shildi. O'qish uchun Hozir kiring\n
        Sarlavha: {instance.title}
        Categoriya: {instance.ctg.name}
        Qisqacha: {instance.short_desc}
        Qo'shilgan_vaqt: {datetime.datetime.now().strftime('%H:%M | %D')}
        Taglar: {instance.tags}
         
        """
        qabul_qiluvchi = []
        for i in Subscription.objects.filter(is_trash=False):
            qabul_qiluvchi.append(i.email)
            sarlavha = "NEWS saytida Yangi Yangiliklar"
            send_mail(
                subject=sarlavha,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=qabul_qiluvchi

            )
            token = "8225709661:AAF6aZfcKDZXbLRCnxCvob6V3jhLX7Cku-U"
            message = "Hammaga xabar yuborildimi????"
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={2068375686}&text={message}&parse_mode=HTML"
            requests.get(url)

@receiver(post_save, sender=Contact)
def contact_signal(sender, created, instance, **kwargs):
    if created:
        message = f"Saytdan yangi xabar keldi\nYuboruvchi: {instance.user}\nTelefon raqami: {instance.phone}\n\n" \
                  f"Xabar: <i><b>{instance.message}</b></i>\n\nSana: {datetime.datetime.now().strftime('%H:%M | %D')}"
        token = "8225709661:AAF6aZfcKDZXbLRCnxCvob6V3jhLX7Cku-U"
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={2068375686}&text={message}&parse_mode=HTML"
        requests.get(url)




