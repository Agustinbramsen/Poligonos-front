from django.db import models


class DatoHuerfanoCelular(models.Model):
    class Meta:
        db_table = 'datoHuerfano_celular'

    celular = models.CharField(max_length=20, primary_key=True)
    seccion_nombre = models.CharField(max_length=20)
    distrito_nombre = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.celular or ''


class DatoHuerfanoEmail(models.Model):
    class Meta:
        db_table = 'datoHuerfano_email'

    email = models.CharField(max_length=100, primary_key=True)
    seccion_nombre = models.CharField(max_length=100)
    distrito_nombre = models.CharField(max_length=100, null=True)
    tag = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.email


class DatoHuerfanoTelefono(models.Model):
    class Meta:
        db_table = 'datoHuerfano_telefono'

    telefono = models.CharField(max_length=20, primary_key=True)
    seccion_nombre = models.CharField(max_length=100)
    distrito_nombre = models.CharField(max_length=100, null=True)
    tag = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.telefono


class AndromedaTagsDescripcion(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'andromeda_tags_descripcion'

class Tags(models.Model):
    pass