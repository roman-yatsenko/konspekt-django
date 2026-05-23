from django.db import models


class Topic(models.Model):
    """Тема (предмет), яку вивчає користувач"""

    text = models.CharField(max_length=200, verbose_name="Назва теми")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def __str__(self):
        return self.text
    