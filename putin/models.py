from django.db import models


class EmojiStats(models.Model):
    guild_id = models.BigIntegerField(blank=True, null=True)
    emoji_id = models.BigIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoji_stats'
        unique_together = (('guild_id', 'emoji_id'),)

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
    name = models.TextField(blank=True, null=True)
    pfp = models.TextField(blank=True, null=True)

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

class Guilds(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'guilds'


class Settings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message_delete = models.BooleanField()
    message_edit = models.BooleanField()
    kick = models.BooleanField()
    ban = models.BooleanField()
    log_join = models.BooleanField()
    leave = models.BooleanField()
    welcome_enabled = models.BooleanField()
    welcome_channel = models.BigIntegerField(blank=True, null=True)
    log_commands = models.BooleanField()
    unban = models.BooleanField()
    buy_roles = models.BooleanField()
    advert = models.BooleanField()
    logging_channel = models.BigIntegerField(blank=True)

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

    def db_for_write(self, StarboardEntries, **hints):
        return 'bot'

    def db_for_read(self, StarboardEntries, **hints):
        return 'bot'


class Starrers(models.Model):
    author_id = models.BigIntegerField()
    entry = models.ForeignKey(StarboardEntries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'starrers'
        unique_together = (('author_id', 'entry'),)

    def db_for_write(self, Starrers, **hints):
        return 'bot'

    def db_for_read(self, Starrers, **hints):
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

    def db_for_write(self, TagLookup, **hints):
        return 'bot'

    def db_for_read(self, TagLookup, **hints):
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

    def db_for_write(self, Tags, **hints):
        return 'bot'

    def db_for_read(self, Tags, **hints):
        return 'bot'
