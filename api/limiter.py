# api/limiter.py
# Shared rate limiter instance.
# Lives in its own module to avoid circular imports — main.py and routes both need it.

from slowapi import Limiter
from slowapi.util import get_remote_address

# key_func=get_remote_address means limits are tracked per caller IP address.
limiter = Limiter(key_func=get_remote_address)
