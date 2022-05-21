from django.db import models

    
class Group(models.Model):
    title = models.CharField(
        max_length=150,
        help_text='input title here',
        verbose_name='title of group',
    )
    slug = models.SlugField(
        'slug of group',
        help_text='input a unique url-name of group',
        unique=True)
    description = models.TextField(
        'Brief description of the item group',
        max_length=150,
        help_text='input a description here'
    )

    def __str__(self):
        return self.title


class Item(models.Model):
    collection = models.CharField(
        verbose_name='collection_of_items',
        max_length=50,
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name='name_of_items',
        max_length=50,
    )
    description = models.TextField(
        max_length=250,
        verbose_name='descr of item')
        
    photo = models.ImageField(
        verbose_name='photo_item',
        upload_to='img',
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='price'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='item',
        verbose_name='group of items',
        
    )
    created = models.DateTimeField(
        verbose_name='a date of created',
        auto_now_add=True)


    class Meta:
        ordering = ['-created']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='item')
        ]
    def __str__(self):
        return self.name[:15]
