from sqlalchemy import inspect
from werkzeug.security import generate_password_hash


def copy_attr(source, destination, ignore=[]):
    """
    Copies all the attributes of source to target in-place.
    Copies only the first layer.

    Args:
        source: Source dictionary to copy
        destination: Destination dictionary to copy source values to
        ignore: Keys to ignore
    """
    for k, v in source.items():
        if k in ignore:
            continue
        elif k == "password":
            hashed_password = generate_password_hash(
                source["password"], method="sha256"
            )
            setattr(destination, k, hashed_password)
        else:
            setattr(destination, k, v)


def get_schema(model_instance):
    """
    Gets the schema/attributes of the model

    Args:
        model_instance: SQLAlchemy model
    
    Returns:
        attr_names: Array of keys from the model schema
    """
    inst = inspect(model_instance.__class__)
    attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
    return attr_names


def has_changes(source, target, ignore=[], print_diff=False):
    """
    Detect if source and target has changes only on the first layer.
    Warning: Compares as is.

    Args:
        source: Source dictionary. Keys from this dictionary are used to compare to target.
        target: Target dictionary.
        ignore: keys to ignore
        print_diff: Print mismatching keys
    
    Returns:
        True: if there are changes from source to target
        False: otherwise
    """
    for k in source_json.keys():
        if k in ignore:
            continue
        elif 'date' in k:
            try:
                if(hasattr(dest_model, k) and source_json[k] != getattr(dest_model, k).isoformat()):
                    if print_diff:
                        print(k, source_json[k], getattr(dest_model, k).isoformat())
                    return True
            except:
                pass
        elif hasattr(dest_model, k) and source_json[k] != getattr(dest_model, k):
            if print_diff:
                print(k, source_json[k], getattr(dest_model, k))
            return True
    return False
