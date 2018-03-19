from collections import OrderedDict
from cryptography.fernet import Fernet
import time
import uuid

from cdislogging import get_logger

logger = get_logger(__name__)

try:
    from fence.local_settings import *
except ImportError:
    logger.warn('no module fence.local_settings')

# WARNING: the test database is cleared every run
DB = 'postgresql://postgres:postgres@localhost:5432/fence_test_tmp'

DEBUG = False
OAUTH2_PROVIDER_ERROR_URI = "/oauth2/errors"

BASE_URL = 'https://bionimbus-pdc.opensciencedatacloud.org/user'
APPLICATION_ROOT = '/user'

MOCK_AUTH = {
    'pur': 'access',
    'aud': ['openid', 'fence', 'user', 'data'],
    'sub': '0',
    'iss': BASE_URL,
    'iat': time.time(),
    'exp': time.time() + 1000000,
    'jti': str(uuid.uuid4()),
    'context': {
        'user': {
            'name': 'MOCK_USER',
            'is_admin': True,
            'projects': {
            },
        },
    },
}

SHIBBOLETH_HEADER = 'persistent_id'
SSO_URL = 'https://itrusteauth.nih.gov/affwebservices/public/saml2sso?SPID=https://bionimbus-pdc.opensciencedatacloud.org/shibboleth&RelayState='
SINGLE_LOGOUT = 'https://itrusteauth.nih.gov/siteminderagent/smlogout.asp?mode=nih&AppReturnUrl=https://bionimbus-pdc.opensciencedatacloud.org/storage/login'
ITRUST_GLOBAL_LOGOUT = 'https://auth.nih.gov/siteminderagent/smlogout.asp?mode=nih&AppReturnUrl='

LOGOUT = "https://bionimbus-pdc.opensciencedatacloud.org/auth/logout/?next=/Shibboleth.sso/Logout%3Freturn%3Dhttps%3A%2F%2Fbionimbus-pdc.opensciencedatacloud.org/api"
BIONIMBUS_ACCOUNT_ID = 123456789012

#: ``ACCESS_TOKEN_EXPIRES_IN: int``
#: The number of seconds after an access token is issued until it expires.
ACCESS_TOKEN_EXPIRES_IN = 1200

#: ``ACCESS_TOKEN_COOKIE_NAME: str``
#: The name of the browser cookie in which the access token will be stored.
ACCESS_TOKEN_COOKIE_NAME = 'access_token'

#: ``REFRESH_TOKEN_EXPIRES_IN: int``
#: The number of seconds after a refresh token is issued until it expires.
REFRESH_TOKEN_EXPIRES_IN = 1728000

#: ``SESSION_TIMEOUT: int``
#: The number of seconds after which a browser session is considered stale.
SESSION_TIMEOUT = 1800

#: ``SESSION_LIFETIME: int``
#: The maximum session lifetime in seconds.
SESSION_LIFETIME = 28800

#: ``SESSION_COOKIE_NAME: str``
#: The name of the browser cookie in which the session token will be stored.
#: Note that the session token also stores information for the
#: ``flask.session`` in the ``context`` field of the token.
SESSION_COOKIE_NAME = 'fence'

HMAC_ENCRYPTION_KEY = Fernet.generate_key()
ENABLE_CSRF_PROTECTION = False

JWT_KEYPAIR_FILES = OrderedDict([
    (
        'key-test',
        ('resources/keys/test_public_key.pem', 'resources/keys/test_private_key.pem'),
    ),
    (
        'key-test-2',
        ('resources/keys/test_public_key_2.pem', 'resources/keys/test_private_key_2.pem'),
    ),
])

STORAGE_CREDENTIALS = {
    'test-cleversafe': {
        'backend': 'cleversafe'
    }
}

AWS_CREDENTIALS = {
    "CRED1": {
        'aws_access_key_id': '',
        'aws_secret_access_key': ''
    },
    "CRED2": {
        'aws_access_key_id': '',
        'aws_secret_access_key': ''
    }
}

S3_BUCKETS = {
    "bucket1": "CRED1",
    "bucket2": "CRED2",
    "bucket3": "CRED1",
}

ENABLED_IDENTITY_PROVIDERS = {
    # ID for which of the providers to default to.
    'default': 'google',
    # Information for identity providers.
    'providers': {
        'fence': {
            'name': 'Fence Multi-Tenant OAuth',
        },
        'google': {
            'name': 'Google OAuth',
        },
        'shibboleth': {
            'name': 'NIH Login',
        },
    },
}

SHIBBOLETH_HEADER = 'persistent_id'
