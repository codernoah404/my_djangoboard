# Generated by Django 4.1 on 2023-10-09 09:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0003_rename_board_comment_board"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="content",
            field=models.TextField(
                validators=[
                    django.core.validators.MinLengthValidator(
                        10, "최소 10글자 이상은 입력하셔야 합니다."
                    )
                ],
                verbose_name="내용",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="title",
            field=models.CharField(
                max_length=255,
                validators=[
                    django.core.validators.MinLengthValidator(
                        2, "최소 세 글자 이상은 입력해주셔야 합니다."
                    )
                ],
                verbose_name="제목",
            ),
        ),
    ]