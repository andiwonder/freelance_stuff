# Generated by Django 2.0.7 on 2018-07-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20180702_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eo_pricing_model_deductible',
            name='deductible_amount',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='eo_pricing_model_limit',
            name='occurence_limit',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='errors_omissions_policy_details',
            name='class_sub_code',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='hazard_rate_multiplier',
            name='hazard_level_rating',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_industry_code',
            name='class_code',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_11',
            name='class_sub_code',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_54',
            name='class_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_code_54',
            name='class_sub_code',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_hazard_rating',
            name='class_sub_code',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='naic_sub_industry_hazard_rating',
            name='hazard_level_rating',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterModelTable(
            name='naic_sub_industry_code_11',
            table='11_NAIC_SUB_INDUSTRY_CODE',
        ),
        migrations.AlterModelTable(
            name='naic_sub_industry_code_54',
            table='54_NAIC_SUB_INDUSTRY_CODE',
        ),
    ]
