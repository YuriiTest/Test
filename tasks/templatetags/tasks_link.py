from django import template
from django.core.urlresolvers import reverse

register = template.Library()

def create_link(any_ob):
    link = reverse('admin:%s_%s_change' %(any_ob._meta.app_label,  any_ob._meta.module_name),  args=[any_ob.id])
    return link


class EditLinkNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)
        
    def render(self, context):
        return create_link(self.object.resolve(context))

@register.tag
def edit_link(parser, token):
    tagname, object = token.split_contents()
    return EditLinkNode(object)