# Generated by Django 2.2.6 on 2019-12-06 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Emprestimo', '0009_auto_20191204_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cliente.Cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Livros.Livro', verbose_name='Livro'),
        ),
    ]