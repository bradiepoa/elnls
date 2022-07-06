from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_students = models.BooleanField(default=False)


    class Meta:
    	swappable = 'AUTH_USER_MODEL'




class Bookcategory(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    SATUS_CHOICE = (
        ('pdf','PDF'),
        ('hard copy','Hard copy'),
        ('reserve','Reserve'),
        )


    Title = models.CharField(max_length=100)
    Category = models.ForeignKey(Bookcategory, on_delete=models.SET_NULL, blank=True, null=True)
    Author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=200, blank=True, null=True, unique=True)
    Book_Number = models.PositiveSmallIntegerField(blank=True, null=True)
    Year_Published = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=200)
    Book_Description = models.TextField(max_length=1000)
    Status = models.CharField(max_length=200, choices=SATUS_CHOICE, blank=True, null=True)
    Uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    Added = models.DateField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to='covers', blank=True)

    def __str__(self):
        return self.Title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.image.delete()
        super().delete(*args, **kwargs)  




class Borrow(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, editable=False,)
    return_date = models.DateTimeField(auto_now_add=True,editable=True)
    complete = models.BooleanField(default=False,null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class BorrowedBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrowed = models.ForeignKey(Borrow, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, editable=False)
    date_ordered = models.DateTimeField(auto_now_add=True, editable=False)
    return_date = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__ (str):
        return self.Book.title

class Chat(models.Model):

    SATUS_CHOICE = (

        ('all students','All students'),
        ('publisher','Publisher'),
        ('administor','Administor'),

        )
    name = models.CharField(max_length=200, blank=True,null=True)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    Message_To = models.CharField(max_length=200, choices=SATUS_CHOICE, default='all students', blank=True, null=True)


    def __str__(self):
        return str(self.message)
        
    class Meta:
        ordering =('-posted_at',)



class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.feedback
