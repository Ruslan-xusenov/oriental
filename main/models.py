from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/', blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)

    def get_flag(self):
        if self.flag:
            return self.flag.url
        elif self.flag_url:
            return self.flag_url
        return None

    def __str__(self):
        return self.name

class Institution(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="institutions")
    name = models.CharField(max_length=200)
    description = models.TextField()
    advantages = models.TextField(blank=True, help_text="Comma or newline separated advantages")
    image_url = models.URLField(blank=True, help_text="Image URL for institution")
    video_url = models.URLField(blank=True, help_text="MP4 link or YouTube embed link")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.country.name})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Matn")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Rasm")
    image_url = models.URLField(blank=True, null=True, verbose_name="Rasm URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title