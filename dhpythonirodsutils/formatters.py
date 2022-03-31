import re
from dhpythonirodsutils import validators


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


def format_schema_collection_path(project_id, collection_id):
    """
    Format the schema.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id eg P00000001
    collection_id : str
        The collection_id eg C00000001

    Returns
    -------
    str
        Absolute schema.json collection absolute path.
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/schema.json".format(project_collection_path)

def format_instance_collection_path(project_id, collection_id):
    """
    Format the instance.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id eg P00000001
    collection_id : str
        The collection_id eg C00000001

    Returns
    -------
    str
        Absolute instance.json collection absolute path.
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/instance.json".format(project_collection_path)

def format_schema_versioned_collection_path(project_id, collection_id, version):
    """
    Format the versioned schema.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id, eg P00000001
    collection_id : str
        The collection_id, eg C00000001
    version: str
        The version number, eg 2

    Returns
    -------
    str
        Absolute schema.json collection absolute path.
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/.metadata_versions/schema.{}.json".format(project_collection_path, version)


def format_instance_versioned_collection_path(project_id, collection_id, version):
    """
    Format the versioned instance.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id eg P00000001
    collection_id : str
        The collection_id eg C00000001
    version: str
        The version number, eg 2

    Returns
    -------
    str
        Absolute instance.json collection absolute path.
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/.metadata_versions/schema.{}.json".format(project_collection_path, version)

def format_project_path(project_id):
    """
    Validate the project ID and format the project path

    Parameters
    ----------
    project_id
        The project id, eg P000000001

    Returns
    -------
        The formatted path

    """
    if validators.validate_project_id(project_id):
        return "/nlmumc/projects/{}".format(project_id)


def format_project_collection_path(project_id, collection_id):
    """
    Validate and format the projectcollection path

    Parameters
    ----------
    project_id
        The project id, eg P000000001
    collection_id
        The collection id, eg C000000001

    Returns
    -------
        The formatted path

    """
    project_collection_path = "/nlmumc/projects/{}/{}".format(project_id, collection_id)
    if validators.validate_project_collection_path(project_collection_path):
        return project_collection_path


def get_project_from_collection_path(path):
    """
    Return the project path from the projectcollection path

    Parameters
    ----------
    path
        The full path of the project collection

    Returns
    -------
        The project path

    """
    match = re.search(r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/C[0-9]{9}/?", path)
    if match is not None:
        return format_project_path(match.group("project"))
    else:
        return None

def get_project_id_from_project_path(path):
    """
    Return the project_id from the project path

    Parameters
    ----------
    path
        The full path of the project

    Returns
    -------
        The project id

    """
    match = re.search(r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/?", path)
    if match is not None:
        return match.group("project")
    else:
        return None

def get_project_id_from_collection_path(path):
    """
    Return the project_id from the projectcollection path

    Parameters
    ----------
    path
        The full path of the project collection

    Returns
    -------
        The project id

    """
    match = re.search(r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/C[0-9]{9}/?", path)
    if match is not None:
        return match.group("project")
    else:
        return None

def get_collection_id_from_collection_path(path):
    """
    Return the collection_id from the projectcollection path

    Parameters
    ----------
    path
        The full path of the project collection

    Returns
    -------
        The collection id

    """
    match = re.search(r"^(/nlmumc/projects/)?(P[0-9]{9})/?(?P<collection>C[0-9]{9})/?", path)
    if match is not None:
        return match.group("collection")
    else:
        return None