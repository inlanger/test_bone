from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission, User

from test_app.models import Perm

class Command(BaseCommand):
    help = 'Create groups with permissions'

    def handle(self, *args, **options):
        for i in ['1', '2']:
            g, created = Group.objects.get_or_create(name='Group {}'.format(i))
            p, created = Permission.objects.get_or_create(
                name='view {}'.format(i), defaults={
                    "codename": 'view_perm {}'.format(i),
                    "content_type": ContentType.objects.get_for_model(Perm)
                }
            )
            g.permissions.add(p)

            u, created = User.objects.get_or_create(username='test{}'.format(i))
            u.groups.add(g)
            u.set_password('123123')
            u.save()