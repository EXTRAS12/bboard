from django.contrib import admin
import datetime
import random
import string
from .models import AdvUser, SubRubric, SuperRubric, Bb, AdditionalImage, Comment
from .forms import SubRubricForm
from .utilities import send_activation_notification


def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, "Письма с требованиями отправлены")

send_activation_notifications.short_description = "Отправка писем с требованиями активация"


class NonactivatedFilter(admin.SimpleListFilter):
    title = "Прошли активацию?"
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3х дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_activate=True, is_activated=True)

        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_activate=False, is_activated=False,
                                   date_joined__date__lt=d)

        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_activate=False, is_activated=False,
                                   date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications, )


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)
    list_select_related = ['super_rubric']


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm
    list_select_related = ['super_rubric']


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'url', 'short_url',
              'contacts', 'image', 'is_active')
    inlines = (AdditionalImageInline,)
    list_select_related = ['author', 'rubric', 'rubric__super_rubric']

    def save_model(self, request, obj, form, change):
        
        if form.has_changed():
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            obj.short_url = random_chars
            obj.save()
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    list_select_related = ['bb', 'bb__author']


admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(Bb, BbAdmin)
admin.site.register(Comment, CommentAdmin)
