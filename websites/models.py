from django.db import models
from django.contrib.auth.models import User

COUNTRY = (
        ('KZ', 'KAZAKHSTAN'),
        ('World', 'WORLD'),

    )


class CategoryLink(models.Model):
  category_name = models.CharField(max_length = 20)
  category_img = models.ImageField(upload_to='imagesDB',null = True,blank=True)
  parent = models.ForeignKey('self',on_delete = models.CASCADE,null = True,blank=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
      return self.category_name

  class Meta:
      verbose_name = 'Category of links'
      verbose_name_plural = 'Categories of links'



class LinkModel(models.Model):
  link_title = models.CharField(max_length = 400)
  link_logo = models.ImageField(upload_to='imagesDB')
  link_domain = models.CharField(max_length = 20)
  link_category = models.ForeignKey(CategoryLink,on_delete=models.CASCADE)
  country = models.CharField(max_length=300, choices = COUNTRY,null = True)
  visited_people_number_on_last_month = models.IntegerField(default=100)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=False)

  def __str__(self):
      return self.link_domain

  class Meta:
      verbose_name = 'Link'
      verbose_name_plural = 'Links'



class LinksInWishlist(models.Model):
  user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete= models.CASCADE)
  link = models.ForeignKey(LinkModel, on_delete= models.CASCADE,null = True)
  is_active = models.BooleanField(default=True, null=True)
  session_key =models.CharField(max_length=120,blank=True, null=True, default=None)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
      return '%s %s' % (self.id, self.link)

  class Meta:
    verbose_name='Link in wishlist'
    verbose_name_plural = 'Links in wishlist'



class VisitedHistoryModel(models.Model):
  link = models.ForeignKey(LinkModel, on_delete= models.CASCADE,null = True)
  session_key =models.CharField(max_length=120,blank=True, null=True, default=None)
  is_active = models.BooleanField(default=True, null=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
      return '%s %s' % (self.id, self.link)

  class Meta:
    verbose_name='Visited link'
    verbose_name_plural = 'Visited links'