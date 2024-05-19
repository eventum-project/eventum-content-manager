import os
from string import ascii_letters, digits


def validate_yaml_filename(filename: str) -> None:
    """Check if provided filename is in format <basename>.[yml|yaml]
    where basename consists only of ascii letters, digits and
    underscores. Raise `ValueError` on validation failure.
    """
    if not filename:
        raise ValueError(
            'File name cannot be empty'
        )

    filename, ext = os.path.splitext(filename)

    restricted_symbols = set(filename) - set(ascii_letters + digits + '_')
    if restricted_symbols:
        raise ValueError(
            'Only letters, digits and underscore are allowed in file basename'
        )

    if ext not in ['.yml', '.yaml']:
        raise ValueError('Only yml and yaml extensions are allowed')


def validate_jinja_filename(filename: str) -> None:
    """Check if provided filename is in format <basename>.jinja
    where basename consists only of ascii letters, digits and
    underscores. Raise `ValueError` on validation failure.
    """
    if not filename:
        raise ValueError(
            'File name cannot be empty'
        )

    filename, ext = os.path.splitext(filename)

    restricted_symbols = set(filename) - set(ascii_letters + digits + '_.')
    if restricted_symbols:
        raise ValueError(
            'Only letters, digits, underscore and dot '
            'are allowed in file basename'
        )

    if ext != '.jinja':
        raise ValueError('Only ".jinja" extension is allowed')
