from django.db import migrations

def create_leave_types(apps, schema_editor):
    LeaveType = apps.get_model('main', 'LeaveType')
    leave_types = [
        "Ежегодный оплачиваемый",
        "Без сохранения заработной платы",
        "Учебный",
        "По родам, кормлению и уходу за ребенком",
        "Командировка",
    ]
    for leave_type in leave_types:
        LeaveType.objects.create(name=leave_type)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_application_leave_type'),  # Замените на актуальную зависимость, если она отличается
    ]

    operations = [
        migrations.RunPython(create_leave_types),
    ]
