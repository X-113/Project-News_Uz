import datetime

from django.contrib import admin
from django.utils.html import format_html

from .models import Category, New, Comment, Contact, Subscription, NewsImage


# Register your models here.

admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Subscription)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'menu_status']
    list_display_links = ['name']

    @admin.display(description="Menyuda Chiqishi", empty_value="???")
    def menu_status(self,obj):
        if obj.is_menu:
            return format_html(
                "<span style='color: green;'>✅ chiqadi</span>"
            )
        else:
            return format_html(
                "<span style='color: red;'>❌ Chiqmaydi</span>"
            )


class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 3

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 5



@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['get_title','ctg','views','vaqt', 'get_image']
    list_filter = ['ctg','created','views']
    search_fields = ['short_desc','description','title','tags']
    list_per_page = 10
    ordering = ['created']

    inlines = [NewsImageInline,CommentInline]
    readonly_fields = ['id','views','vaqt']


    @admin.display(description="Sana", empty_value="Yo'q")
    def vaqt(self, obj):
        if obj.created:
            now = datetime.datetime.now()
            minut = int((now-obj.created).total_seconds() // 60)
            if minut < 2:
                return "Hozirgina"
            if 2 <= minut < 60:
                return f"{minut} minut oldin"

            if 60 <= minut < 24 * 60:
                return f"{int(minut//60)} soat oldin"
            return obj.created.strftime('%H:%M | %d.%m.%Y')
        return "Yo'q"


    @admin.display(description="Image", empty_value="Yo'q")
    def get_image(self, obj):
        return format_html(
            f"<img src='{obj.image.url}' width='150'>"
        )

    @admin.display(description="Mavzu", empty_value="Yo'q")
    def get_title(self, obj):
        return f"{obj.title[:40]}....."

