from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView


class View1(PermissionRequiredMixin, TemplateView):
    template_name = "view1.html"
    permission_required = 'test_app.view_perm 1'
