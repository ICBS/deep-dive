def validate_int(name, value, min_val=None, max_val=None):
  if not isinstance(value, int):
    raise TypeError(f'{name} must be an integer.')
  if min_val is not None and value < min_val:
    raise ValueError(f'{name} must be no smaller than {min_val}.')
  if max_val is not None and value > max_val:
    raise ValueError(f'{name} must be no larger than {max_val}.')
