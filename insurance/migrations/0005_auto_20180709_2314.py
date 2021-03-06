# Generated by Django 2.0.7 on 2018-07-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_auto_20180703_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOP_EnEnhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'BOP_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='BOP_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'BOP_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='BOP_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('BOP_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'BOP_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='CV_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'CV_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='CV_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'CV_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='CV_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('CV_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'CV_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='CY_Base_Rate_1st_Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage_limit', models.IntegerField()),
                ('base_rate', models.IntegerField()),
            ],
            options={
                'db_table': 'CY_Base_Rate_1st_Party',
            },
        ),
        migrations.CreateModel(
            name='CY_Base_Rate_3rd_Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage_limit', models.IntegerField()),
                ('base_rate', models.IntegerField()),
            ],
            options={
                'db_table': 'CY_Base_Rate_3rd_Party',
            },
        ),
        migrations.CreateModel(
            name='CY_Deductible_Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deductible_amount', models.IntegerField()),
                ('deductible_factor', models.FloatField()),
            ],
            options={
                'db_table': 'CY_Deductible_Factor',
            },
        ),
        migrations.CreateModel(
            name='CY_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'CY_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='CY_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'CY_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='CY_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('CY_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'CY_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='CY_Hazard_Rate_Multiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard_level_rating', models.IntegerField(db_index=True)),
                ('rate_multiplier', models.FloatField()),
            ],
            options={
                'db_table': 'CY_Hazard_Rate_Multiplier',
            },
        ),
        migrations.CreateModel(
            name='CY_Increased_Limit_Factor_1st_Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_breach_expense_limit', models.IntegerField()),
                ('increased_limit_factor', models.FloatField()),
            ],
            options={
                'db_table': 'CY_Increased_Limit_Factor_1st_Party',
            },
        ),
        migrations.CreateModel(
            name='CY_Increased_Limit_Factor_3rd_Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_breach_expense_limit', models.IntegerField()),
                ('increased_limit_factor', models.FloatField()),
            ],
            options={
                'db_table': 'CY_Increased_Limit_Factor_3rd_Party',
            },
        ),
        migrations.CreateModel(
            name='CY_Naic_Industry_Hazard_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic_code', models.IntegerField()),
                ('hazard_level_rating', models.IntegerField()),
            ],
            options={
                'db_table': 'CY_Naic_Industry_Hazard_Rating',
            },
        ),
        migrations.CreateModel(
            name='DO_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'DO_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='DO_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'DO_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='DO_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('DO_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'DO_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='EO_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'EO_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='EO_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'EO_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='EO_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('EO_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'EO_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='GL_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'GL_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='GL_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'GL_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='GL_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('GL_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'GL_Naic_Policy_Exclusions',
            },
        ),
        migrations.CreateModel(
            name='WC_Enhancements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('enhance1', models.CharField(blank=True, max_length=200)),
                ('enhance2', models.CharField(blank=True, max_length=200)),
                ('enhance3', models.CharField(blank=True, max_length=200)),
                ('enhance4', models.CharField(blank=True, max_length=200)),
                ('enhance5', models.CharField(blank=True, max_length=200)),
                ('enhance6', models.CharField(blank=True, max_length=200)),
                ('enhance7', models.CharField(blank=True, max_length=200)),
                ('enhance8', models.CharField(blank=True, max_length=200)),
                ('enhance9', models.CharField(blank=True, max_length=200)),
                ('enhance10', models.CharField(blank=True, max_length=200)),
                ('enhance11', models.CharField(blank=True, max_length=200)),
                ('enhance12', models.CharField(blank=True, max_length=200)),
                ('enhance13', models.CharField(blank=True, max_length=200)),
                ('enhance14', models.CharField(blank=True, max_length=200)),
                ('enhance15', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'WC_Naic_Policy_Enhancements',
            },
        ),
        migrations.CreateModel(
            name='WC_Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('example', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'WC_Naic_Policy_Examples',
            },
        ),
        migrations.CreateModel(
            name='WC_Exclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naic', models.IntegerField()),
                ('exclusion1', models.CharField(blank=True, max_length=200)),
                ('exclusion2', models.CharField(blank=True, max_length=200)),
                ('exclusion3', models.CharField(blank=True, max_length=200)),
                ('exclusion4', models.CharField(blank=True, max_length=200)),
                ('exclusion5', models.CharField(blank=True, max_length=200)),
                ('exclusion6', models.CharField(blank=True, max_length=200)),
                ('exclusion7', models.CharField(blank=True, max_length=200)),
                ('exclusion8', models.CharField(blank=True, max_length=200)),
                ('exclusion9', models.CharField(blank=True, max_length=200)),
                ('exclusion10', models.CharField(blank=True, max_length=200)),
                ('exclusion11', models.CharField(blank=True, max_length=200)),
                ('exclusion12', models.CharField(blank=True, max_length=200)),
                ('exclusion13', models.CharField(blank=True, max_length=200)),
                ('exclusion14', models.CharField(blank=True, max_length=200)),
                ('exclusion15', models.CharField(blank=True, max_length=200)),
                ('CV_Dummy', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'WC_Naic_Policy_Exclusions',
            },
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_base_rate',
            name='annual_sales',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_base_rate',
            name='base_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_deductible',
            name='deductible_amount',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_deductible',
            name='multiplier',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_limit',
            name='increased_limit_factor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_limit',
            name='occurence_limit',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_marginal',
            name='annual_sales',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_marginal',
            name='marginal_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='errors_omissions_policy_details',
            name='class_sub_code',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='errors_omissions_policy_details',
            name='need_for_policy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='errors_omissions_policy_details',
            name='placeholder',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hazard_rate_multiplier',
            name='hazard_level_rating',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='hazard_rate_multiplier',
            name='rate_multiplier',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='naic_industry_code',
            name='class_code',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_industry_code',
            name='industry',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_11',
            name='class_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_11',
            name='class_sub_code',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_54',
            name='class_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_54',
            name='class_sub_code',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_hazard_rating',
            name='class_sub_code',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_hazard_rating',
            name='hazard_level_rating',
            field=models.IntegerField(),
        ),
    ]
