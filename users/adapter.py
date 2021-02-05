from allauth.account.adapter import DefaultAccountAdapter
from roboPortal.models import portalUser


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.name = data.get('name')
        user.phone_no = data.get('phone_no')
        user.save()
        a = portalUser(user = user)
        a.save()
        return user
