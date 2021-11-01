from django import template
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    # group = Group.objects.get(name=group_name)
    group = get_object_or_404(Group, name=group_name)
    return True if group in user.groups.all() else False
