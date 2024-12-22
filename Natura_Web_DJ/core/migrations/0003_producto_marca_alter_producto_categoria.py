# Generated by Django 5.1.1 on 2024-12-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_card_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(choices=[('', 'Elegir'), ('ekos', 'Ekos'), ('tododia', 'Tododia'), ('mama_y_bebe', 'Mamá y Bebé'), ('creer_para_ver', 'Creer para Ver'), ('erva_doce', 'Erva Doce'), ('chronos', 'Chronos'), ('kaiak', 'Kaiak'), ('lumina', 'Lumina'), ('homem', 'Homem'), ('ilia', 'Ilía'), ('essencial', 'Essencial'), ('humor', 'Humor')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('', 'Elegir'), ('perfumería', 'Perfumería'), ('maquillaje', 'Maquillaje'), ('rostro', 'Rostro'), ('cuidados_diarios', 'Cuidados Diarios'), ('cabello', 'Cabello'), ('infantil', 'Infantil'), ('repuestos', 'Repuestos')], default='', max_length=50),
        ),
    ]
