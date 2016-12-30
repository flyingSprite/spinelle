
from dogpile.cache import make_region


region = make_region().configure(
    'dogpile.cache.pylibmc',
    expiration_time=3600,
    arguments={'url': ['127.0.0.1']}
)


@region.cache_on_arguments()
def load_user_info(user_id):
    return ''
