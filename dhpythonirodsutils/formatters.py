import re
import validators


def format_dropzone_path(token, dropzone_type):
    """
    Format the dropzone absolute path based on the token and the dropzone type.

    Parameters
    ----------
    token : str
        The dropzone token
    dropzone_type : str
        The type of dropzone, 'mounted' or 'direct'

    Returns
    -------
    str
        Absolute dropzone path
    """
    dropzone_path = None
    validators.validate_dropzone_type(dropzone_type)
    if dropzone_type == "mounted":
        dropzone_path = "/nlmumc/ingest/zones/{}".format(token)
    elif dropzone_type == "direct":
        dropzone_path = "/nlmumc/ingest/direct/{}".format(token)
    return dropzone_path


def format_schema_dropzone_path(token, dropzone_type):
    """
    Format the schema.json dropzone absolute path based on the token and the dropzone type.

    Parameters
    ----------
    token : str
        The dropzone token.
    dropzone_type : str
        The type of dropzone, 'mounted' or 'direct'.

    Returns
    -------
    str
        Absolute schema.json dropzone path.
    """
    dropzone_path = format_dropzone_path(token, dropzone_type)
    return "{}/schema.json".format(dropzone_path)


def format_instance_dropzone_path(token, dropzone_type):
    """
    Format the instance.json dropzone absolute path based on the token and the dropzone type.

    Parameters
    ----------
    token : str
        The dropzone token.
    dropzone_type : str
        The type of dropzone, 'mounted' or 'direct'.

    Returns
    -------
    str
        Absolute instance.json dropzone absolute path.
    """
    dropzone_path = format_dropzone_path(token, dropzone_type)
    return "{}/instance.json".format(dropzone_path)


def format_project_path(project_id):
    if validators.validate_project_id(project_id):
        return "/nlmumc/projects/{}".format(project_id)


def format_project_collection_path(project_id, collection_id):
    if validators.validate_project_collection_path(project_id, collection_id):
        return "/nlmumc/projects/{}/{}".format(project_id, collection_id)


def get_project_from_collection_path(path):
    """

    Parameters
    ----------
    path

    Returns
    -------

    """
    match = re.search(r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/C[0-9]{9}/?", path)
    if match is not None:
        return format_project_path(match.group("project"))
    else:
        return None
