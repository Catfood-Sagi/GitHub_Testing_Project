import json

def strip_values(json_data):
    if isinstance(json_data, dict):
        return {key: strip_values(value) for key, value in json_data.items()}
    elif isinstance(json_data, list):
        return [strip_values(item) for item in json_data]
    else:
        return None  # Replace values with `None`

