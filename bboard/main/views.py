from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.signing import BadSignature
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ChangeUserInfoForm, RegisterUserForm
from .models import AdvUser
from .utilities import signer


@login_required
def profile(request):
    return render(request, "main/profile.html")


def index(request):
    return render(request, "main/index.html")


def other_page(request, page):
    try:
        template = get_template("main/" + page + ".html")

    except TemplateDoesNotExist:
        raise Http404

    return HttpResponse(template.render(request=request))


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = "main/change_user_info.html"
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy("main:profile")
    success_message = "Данные пользователя изменены"

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBLogoutView(LogoutView):
    template_name = "main/logout.html"


class BBLoginView(LoginView):
    template_name = "main/login.html"


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = "main/password_change.html"
    success_url = reverse_lazy("main:profile")
    success_message = "Пароль пользователя изменён"


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = "main/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("main:register_done")


class RegisterDoneView(TemplateView):
    template_name = "main/register_done.html"
