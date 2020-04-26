from sqlalchemy import inspect
from werkzeug.security import generate_password_hash


def copy_attr(source, destination):
    """
    Copies all the attributes of source to target in-place.
    Copies only the first layer.

    Args:
        source: Source dictionary to copy
        destination: Destination dictionary to copy source values to
    """
    for k, v in source.items():
        if k == "password":
            hashed_password = generate_password_hash(
                source["password"], method="sha256"
            )
            setattr(destination, k, hashed_password)
        else:
            setattr(destination, k, v)


def has_changes(source, target):
    """
    Detect if source and target has changes only on the first layer.
    Warning: Compares as is.

    Args:
        source: Source dictionary. Keys from this dictionary are used to compare to target.
        target: Target dictionary.
    
    Returns:
        True if there are changes from source to target
        False otherwise
    """
    for k, v in source.items():
        if hasattr(target, k) and source[k] != getattr(target, k):
            return True
    return False


def get_schema(model_instance):
    """
    Gets the schema/attributes of the model

    Args:
        model_instance: SQLAlchemy model
    
    Returns:
        Array of keys from the model schema
    """
    inst = inspect(model_instance.__class__)
    attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
    return attr_names
