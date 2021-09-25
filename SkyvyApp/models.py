from django.db import models

# Create your models here.

class BotModel(models.Model):
    bot_name = models.CharField(max_length = 25, unique = True)
    bot_color = models.CharField(max_length = 25, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    time = models.DecimalField(max_digits=30, decimal_places=4)

    x = models.DecimalField(max_digits=30, decimal_places=4)
    y = models.DecimalField(max_digits=30, decimal_places=4)    
    angle = models.DecimalField(max_digits=30, decimal_places=4)

    delivering = models.BooleanField(default = False)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'
    
    def __str__(self):
        return self.bot_name

    




