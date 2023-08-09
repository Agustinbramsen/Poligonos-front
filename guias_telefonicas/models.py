from django.db import models

class GuiaTelefonicaBuenosaires(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_BuenosAires'


class GuiaTelefonicaCaba(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_CABA'


class GuiaTelefonicaCatamarca(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Catamarca'


class GuiaTelefonicaChaco(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Chaco'


class GuiaTelefonicaChubut(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Chubut'


class GuiaTelefonicaCordoba(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Cordoba'


class GuiaTelefonicaCorrientes(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Corrientes'


class GuiaTelefonicaEntrerios(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_EntreRios'


class GuiaTelefonicaFormosa(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Formosa'


class GuiaTelefonicaJujuy(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Jujuy'


class GuiaTelefonicaLapampa(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_LaPampa'


class GuiaTelefonicaLarioja(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_LaRioja'


class GuiaTelefonicaMendoza(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Mendoza'


class GuiaTelefonicaMisiones(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Misiones'


class GuiaTelefonicaNeuquen(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Neuquen'


class GuiaTelefonicaRionegro(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_RioNegro'


class GuiaTelefonicaSalta(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Salta'


class GuiaTelefonicaSanjuan(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_SanJuan'


class GuiaTelefonicaSanluis(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_SanLuis'


class GuiaTelefonicaSantacruz(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_SantaCruz'


class GuiaTelefonicaSantafe(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_SantaFe'


class GuiaTelefonicaSantiagodelestero(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_SantiagoDelEstero'


class GuiaTelefonicaTierradelfuego(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_TierraDelFuego'


class GuiaTelefonicaTucuman(models.Model):
    tipoguia = models.CharField(db_column='TipoGuia', max_length=1, blank=True, null=True)  
    titular = models.CharField(db_column='Titular', max_length=100, blank=True, null=True)  
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True, null=True)  
    rubro = models.CharField(db_column='Rubro', max_length=100, blank=True, null=True)  
    tipo_documento = models.CharField(db_column='Tipo_documento', max_length=100, blank=True, null=True)  
    nro_documento = models.CharField(db_column='Nro_documento', max_length=100, blank=True, null=False, primary_key=True)  
    fecha_nac = models.CharField(db_column='Fecha_nac', max_length=100, blank=True, null=True)  
    partido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_Guia_Telefonica_Tucuman'

