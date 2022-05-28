from django.db import models
from material_data.models import Author, Editorial
from location.models import Library, Rack

class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("spa", "Spanish"),
        ("en", "English")
    ]
    CATEGORY_CHOICES = [
        ("cts", "Cuento"),
        ("nov", "Novela"),
        ("cst", "Consulta"),
        ("ctf", "Cientifico"),
        ("poe", "Poesia"),
        ("bgr", "Biografico"),
        ("vjs", "Viajes"),
    ]
    authors = models.ManyToManyField(Author)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3)
    number_pages = models.IntegerField()
    size = models.IntegerField()
    description = models.TextField()
    additional_notes = models.TextField(blank=True, null=True)
    year_publication = models.CharField(max_length=4)
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class BookItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50)
    publication_date = models.DateField()
    is_rent = models.BooleanField(default=False)
    is_reserve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} | {self.rack}"
