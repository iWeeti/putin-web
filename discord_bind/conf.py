from __future__ import unicode_literals

from django.conf import settings
from appconf import AppConf


class DiscordBindConf(AppConf):
    """ Application settings """
    # API service endpoints
    BASE_URI = 'https://discordapp.com/api'
    AUTHZ_PATH = '/oauth2/authorize'
    TOKEN_PATH = '/oauth2/token'

    # OAuth2 application credentials
    CLIENT_ID = 460846291300122635
    CLIENT_SECRET = 'CHrf6ZD3BhcPXlf5kiXPekF_eCBUbCJn'

    # OAuth2 scope
    EMAIL_SCOPE = False
    GUILDS_SCOPE = True
    INVITE_SCOPE = False
    CONNECTIONS_SCOPE = False

    # URI settings
    REDIRECT_URI = None
    INVITE_URI = 'https://discordapp.com/channels/@me'
    RETURN_URI = '/'
    ERROR_URI = '/'

    class Meta:
        proxy = True
        prefix = 'discord'
        required = ['CLIENT_ID', 'CLIENT_SECRET']
