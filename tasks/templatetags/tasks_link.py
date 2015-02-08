from django import template
from django.core.urlresolvers import reverse

register = template.Library()


def create_link(any_object):
    link = reverse('admin:%s_%s_change' % (any_object._meta.app_label,  any_object._meta.module_name),
                   args=[any_object.id])
    return link


class EditLinkNode(template.Node):
    def __init__(self, any_object):
        self.any_object = template.Variable(any_object)

    def render(self, context):
        return create_link(self.any_object.resolve(context))


@register.tag
def edit_link(parser, token):
    tag_name, any_object = token.split_contents()
    return EditLinkNode(any_object)