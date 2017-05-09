def data_type(value):
    if isinstance(value, str):
        return len(value)
    elif value is None:
        return 'no value'
    elif isinstance(value, bool):
        return value
    elif isinstance(value, int):
        if value < 100:
            return 'less than 100'
        elif value is 100:
            return 'equal to 100'
        elif value > 100:
            return 'more than 100'
        else:
            return 'integer value not recognized'
    elif isinstance(value, list):
        if len(value) >= 3:
            return value[2]
        else:
            return None
    elif type(value) in [tuple, dict, set]:
        return type(value)
    else:
        return 'sorry, input is quite invalid'
