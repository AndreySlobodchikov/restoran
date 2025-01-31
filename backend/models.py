# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BackendAuthmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'backend_authmodel'


class BackendDish(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    menu = models.ForeignKey('BackendMenu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'backend_dish'


class BackendMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_updated = models.DateTimeField()
    restaurant = models.ForeignKey('BackendRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'backend_menu'


class BackendOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_order = models.DateTimeField()
    price_total = models.FloatField()
    username = models.ForeignKey(AuthUser, models.DO_NOTHING)
    restaurant = models.ForeignKey('BackendRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'backend_order'


class BackendOrderlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    dishes = models.JSONField()
    order = models.OneToOneField(BackendOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'backend_orderlist'


class BackendRestaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.CharField(max_length=100)
    time_start_day = models.TimeField()
    time_end_day = models.TimeField()
    work_days = models.CharField(max_length=27)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'backend_restaurant'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MenuAuthmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'menu_authmodel'


class MenuDish(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    menu = models.ForeignKey('MenuMenu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_dish'


class MenuMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_updated = models.DateTimeField()
    restaurant = models.ForeignKey('MenuRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_menu'


class MenuOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_order = models.DateTimeField()
    price_total = models.FloatField()
    username = models.ForeignKey(AuthUser, models.DO_NOTHING)
    restaurant = models.ForeignKey('MenuRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_order'


class MenuOrderlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    dishes = models.JSONField()
    order = models.OneToOneField(MenuOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_orderlist'


class MenuRestaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.CharField(max_length=100)
    time_start_day = models.TimeField()
    time_end_day = models.TimeField()
    work_days = models.CharField(max_length=27)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'menu_restaurant'
