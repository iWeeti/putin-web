# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmojiStats(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    emoji_id = models.BigIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoji_stats'
        unique_together = (('guild_id', 'emoji_id'),)

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


# class Feeds(models.Model):
#     id = models.AutoField()
#     channel_id = models.BigIntegerField(blank=True, null=True)
#     role_id = models.BigIntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'feeds'


class GuildModConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    raid_mode = models.SmallIntegerField(blank=True, null=True)
    broadcast_channel = models.BigIntegerField(blank=True, null=True)
    mention_count = models.SmallIntegerField(blank=True, null=True)
    safe_mention_channel_ids = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'guild_mod_config'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class IndexAnnouncement(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'index_announcement'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class IndexChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('IndexQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'index_choice'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class IndexQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'index_question'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Plonks(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    entity_id = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plonks'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Profiles(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Reminders(models.Model):
    expires = models.DateTimeField(unique=True, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    event = models.TextField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'reminders'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Rtfm(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtfm'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Settings(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Starboard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    threshold = models.IntegerField()
    locked = models.BooleanField(blank=True, null=True)
    max_age = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'starboard'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class StarboardEntries(models.Model):
    bot_message_id = models.BigIntegerField(blank=True, null=True)
    message_id = models.BigIntegerField(unique=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    guild = models.ForeignKey(Starboard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'starboard_entries'

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


class Starrers(models.Model):
    author_id = models.BigIntegerField()
    entry = models.ForeignKey(StarboardEntries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'starrers'
        unique_together = (('author_id', 'entry'),)

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


# class Store(models.Model):
#     id = models.BigIntegerField(blank=True, null=True)
#     price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     seller_id = models.BigIntegerField(blank=True, null=True)
#     selling_id = models.AutoField()
#     quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     item_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'store'


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

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'


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

    def db_for_write(self, model, **hints):
        return 'bot'

    def db_for_read(self, model, **hints):
        return 'bot'
