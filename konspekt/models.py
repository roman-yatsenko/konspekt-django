from django.db import models


class Topic(models.Model):
    """Тема (предмет), яку вивчає користувач"""

    text = models.CharField(max_length=200, verbose_name="Назва теми")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural ="Теми"
    
    def __str__(self):
        return self.text
    
class Note(models.Model):
    """Нотатки за темами"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Тема")
    text = models.TextField(verbose_name="Текст")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Нотатка"
        verbose_name_plural = "Нотатки"

    def __str__(self):
        return f"{self.text[:50]}..."
