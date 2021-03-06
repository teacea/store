from django.db import models

VALUES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
    )
    
class Collection(models.Model):
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
    image = models.ImageField(
        verbose_name='photo_item',
        upload_to='img',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.slug

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
    collection = models.ForeignKey(
        Collection,
        null=True,
        related_name='item',
        on_delete=models.CASCADE,
        verbose_name='collections of items',
        
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='item',
        verbose_name='group of items',
        
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
    old_price = models.PositiveIntegerField(
        verbose_name='old_price',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='a date of created',
        auto_now_add=True)
    values = models.CharField(
        verbose_name='name_of_items',
        max_length=50,
        choices=VALUES
    )

    class Meta:
        ordering = ['-created']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='item')
        ]
    def __str__(self):
        return self.name[:15]


