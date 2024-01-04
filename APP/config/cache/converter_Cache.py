import json


def convert_to_cache(value):
    # Mengonversi nilai ke dalam bentuk yang sesuai untuk disimpan di cache
    return json.dumps(value)


def convert_from_cache(value):
    # Mengonversi nilai dari bentuk yang disimpan di cache ke bentuk semula
    return json.loads(value)
