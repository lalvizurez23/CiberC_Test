from django.db import models
from pyxlsb import open_workbook

# Create your models here.

class upload_file(models.Model):
    """
    Model that represent a file that will be uploaded with the inventory information.
    """
    file_name = models.CharField(max_length=250)
    date = models.DateField(max_length=100)
    file_field = models.CharField(max_length=250)

    def __str__(self):
        return self.file_name

    def save(self):
        current_location = "{}.xlsx".format(self.file_name)
        with open_workbook(current_location) as wb:
            with wb.get_sheet('inventory') as sheet:
                for row in sheet.rows():
                    print('fila')
                    print(row)
        super().save()



class inventory(models.Model):
    """
    Model that represent an inventory.
    """
    serial_number = models.CharField(max_length=100)
    number_of_elements = models.IntegerField(max_length=100)
    price = models.IntegerField(max_length=100)
    Upload_file = models.ForeignKey('Upload_file', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.serial_number, self.number_of_elements, self.price, self.Upload_file, 
