# Generated by Django 2.2.6 on 2019-10-16 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fund_classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='grau_sigilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('qnt_ano', models.IntegerField()),
                ('cod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tipo_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='und_gestora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField()),
                ('sigla', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('cod_und_gestora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.und_gestora')),
                ('id_tipo_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.tipo_doc')),
            ],
        ),
        migrations.CreateModel(
            name='classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.TextField()),
                ('data_doc', models.DateField()),
                ('razao_calssf', models.TextField()),
                ('data_classf_doc', models.DateField()),
                ('autoridade_classf', models.CharField(max_length=150)),
                ('autoridade_ratificadora', models.CharField(max_length=150)),
                ('prazo_sigilo', models.IntegerField()),
                ('prazo_final', models.DateField()),
                ('fund_classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.fund_classificacao')),
                ('grau_sigilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.grau_sigilo')),
                ('nic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.NIC')),
                ('tipo_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.tipo_doc')),
                ('und_gestora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_informacao.und_gestora')),
            ],
        ),
    ]
