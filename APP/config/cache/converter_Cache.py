# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

import json
from APP.config.log import LogProses


def convert_to_cache(value) -> str:
    # Mengonversi nilai ke dalam bentuk yang sesuai untuk disimpan di cache
    try:
        return json.dumps(value)
    except Exception as e:
        LogProses(f"error dumping json: {e}")
        return ""


def convert_from_cache(value) -> dict:
    # Mengonversi nilai dari bentuk yang disimpan di cache ke bentuk semula
    try:
        return json.loads(value)
    except Exception as e:
        LogProses(f"error loads json: {e}")
        return {"value": "", "ttl": 1}


# }}}
