def non_empty(value: str, field_name: str) -> None:
    if not value or not value.strip():
        raise ValueError(f'{field_name} cannot be empty.')


def bounded_int(value: int, field_name: str, minimum: int, maximum: int) -> None:
    if value < minimum or value > maximum:
        raise ValueError(f'{field_name} must be between {minimum} and {maximum}.')
