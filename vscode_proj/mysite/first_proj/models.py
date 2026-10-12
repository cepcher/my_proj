from django.db import models

class FeedbackMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name = 'E-mail')
    message = models.CharField(verbose_name= 'Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправления')

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email})"