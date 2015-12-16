""" Model classes for list application
"""
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):

    """List
    """

    def get_absolute_url(self):
        """Get direct url mapping for a list
        """
        return reverse('view_list', args=[self.id])


class Item(models.Model):

    """Single item on a list
    """
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:

        """Restrictions and settings for Items
        """
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
