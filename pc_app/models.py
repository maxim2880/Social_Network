from django.db import models
from django.contrib.auth.models import AbstractUser


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")


class User(DatesModelMixin, AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['created_at']

    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    def __str__(self):
        return f"Пользователь: {self.username}"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)


class Comment(DatesModelMixin):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст', max_length=500)

    def __str__(self):
        return f"Comment: {self.text}"


class Post(DatesModelMixin):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['created_at']

    header = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.CharField(verbose_name='Текст', max_length=1000, blank=True)
    photo = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Изображение к посту")
    comments = models.ManyToManyField(Comment, blank=True, null=True, verbose_name="Комментарии")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Post: {self.header}"

    def display_comments(self):
        return ', '.join([comment.text for comment in self.comments.all()])

    display_comments.short_description = "Комментарии"
