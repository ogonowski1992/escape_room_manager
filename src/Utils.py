def add_error(field, error_msg):
    field.errors.clear()
    field.errors.append(error_msg)
