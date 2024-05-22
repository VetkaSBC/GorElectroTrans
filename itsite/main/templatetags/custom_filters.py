from django import template

register = template.Library()

LEAVE_TYPE_COLORS = {
    'Annual Paid Leave': '#FFD700',
    'Leave Without Pay': '#FF4500',
    'Educational Leave': '#1E90FF',
    'Maternity Leave': '#FF69B4',
    'Business Trip': '#32CD32',
}

@register.filter
def color_code(leave_type):
    return LEAVE_TYPE_COLORS.get(leave_type, '#000000')
