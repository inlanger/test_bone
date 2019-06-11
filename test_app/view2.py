from .view1 import View1


class View2(View1):
    template_name = "view2.html"
    permission_required = 'test_app.view_perm 2'
