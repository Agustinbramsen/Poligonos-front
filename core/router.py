class Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'datos_huerfanos':
            return 'datos_huerfanos'
        elif model._meta.app_label == 'guias_telefonicas':
            return 'guias'
        elif model._meta.app_label == 'poligonos':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'datos_huerfanos':
            return db == 'datos_huerfanos'
        elif app_label == 'guias_telefonicas':
            return db == 'guias'
        elif app_label == 'poligonos':
            return db == 'default'
        return None
