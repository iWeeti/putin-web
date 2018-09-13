# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


<<<<<<< HEAD
=======
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CommandConfig(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    whitelist = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'command_config'
        unique_together = (('channel_id', 'name', 'whitelist'),)


class Commands(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    used = models.DateTimeField(blank=True, null=True)
    prefix = models.TextField(blank=True, null=True)
    command = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commands'


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


class EmojiStats(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    emoji_id = models.BigIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoji_stats'
        unique_together = (('guild_id', 'emoji_id'),)


class English(models.Model):
    ident = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'english'


class Feeds(models.Model):
    id = models.AutoField()
    channel_id = models.BigIntegerField(blank=True, null=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feeds'


class Finnish(models.Model):
    id = models.AutoField()
    ident = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finnish'


class GuildModConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    raid_mode = models.SmallIntegerField(blank=True, null=True)
    broadcast_channel = models.BigIntegerField(blank=True, null=True)
    mention_count = models.SmallIntegerField(blank=True, null=True)
    safe_mention_channel_ids = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'guild_mod_config'


class IndexAnnouncement(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'index_announcement'


class IndexChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('IndexQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'index_choice'


class IndexQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'index_question'


class Plonks(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    entity_id = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plonks'


class Profiles(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bday = models.TextField(blank=True, null=True)
    picks = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    rings = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    diamonds = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    roses = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    alcohol = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    experience = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    cash = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True)
    married = models.BigIntegerField(blank=True, null=True)
    pet = models.TextField(blank=True, null=True)
    banner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Reminders(models.Model):
    expires = models.DateTimeField(unique=True, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    event = models.TextField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'reminders'


class Rtfm(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtfm'


class Settings(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    message_delete = models.BooleanField(blank=True, null=True)
    message_edit = models.BooleanField(blank=True, null=True)
    kick = models.BooleanField(blank=True, null=True)
    ban = models.BooleanField(blank=True, null=True)
    log_join = models.BooleanField(blank=True, null=True)
    leave = models.BooleanField(blank=True, null=True)
    welcome_enabled = models.BooleanField(blank=True, null=True)
    welcome_channel = models.BigIntegerField(blank=True, null=True)
    log_commands = models.BooleanField(blank=True, null=True)
    unban = models.BooleanField(blank=True, null=True)
    buy_roles = models.BooleanField(blank=True, null=True)
    advert = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Starboard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    threshold = models.IntegerField()
    locked = models.BooleanField(blank=True, null=True)
    max_age = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'starboard'


class StarboardEntries(models.Model):
    bot_message_id = models.BigIntegerField(blank=True, null=True)
    message_id = models.BigIntegerField(unique=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    guild = models.ForeignKey(Starboard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'starboard_entries'


class Starrers(models.Model):
    author_id = models.BigIntegerField()
    entry = models.ForeignKey(StarboardEntries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'starrers'
        unique_together = (('author_id', 'entry'),)


class Store(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    selling_id = models.AutoField()
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class TagLookup(models.Model):
    name = models.TextField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING, blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'tag_lookup'


class Tags(models.Model):
    name = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    uses = models.IntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'tags'


class Turkish(models.Model):
    id = models.AutoField()
    ident = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turkish'
>>>>>>> 353343a5d554b5ae7f99e694d85a616ab876fcf1
