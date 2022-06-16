import re
from dhpythonirodsutils import validators, exceptions
from dhpythonirodsutils.enums import DropzoneState


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

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid dropzone type.
    """
    dropzone_path = None
    validators.validate_dropzone_token(token)
    validators.validate_dropzone_type(dropzone_type)
    if dropzone_type == "mounted":
        dropzone_path = "/nlmumc/ingest/zones/{}".format(token)
    elif dropzone_type == "direct":
        dropzone_path = "/nlmumc/ingest/direct/{}".format(token)
    return dropzone_path


def format_absolute_project_path(relative_path):
    """
    Format the projects absolute path based on a relative path.

    Parameters
    ----------
    relative_path : str
       Relative path to a collection or file

    Returns
    -------
    str
        Absolute project path

    Raises
    -------
    ValidationError
        Raises a ValidationError, if the path is not safe.
    """
    absolute_path = "/nlmumc/projects/{}".format(relative_path)
    validators.validate_full_path_safety(absolute_path)
    return absolute_path


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

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid dropzone type
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

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid dropzone type
    """
    dropzone_path = format_dropzone_path(token, dropzone_type)
    return "{}/instance.json".format(dropzone_path)


def format_schema_collection_path(project_id, collection_id):
    """
    Format the schema.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id e.g: P00000001
    collection_id : str
        The collection_id e.g: C00000001

    Returns
    -------
    str
        Absolute schema.json collection absolute path.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/schema.json".format(project_collection_path)


def format_instance_collection_path(project_id, collection_id):
    """
    Format the instance.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id e.g: P00000001
    collection_id : str
        The collection_id e.g: C00000001

    Returns
    -------
    str
        Absolute instance.json collection absolute path.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/instance.json".format(project_collection_path)


def format_schema_versioned_collection_path(project_id, collection_id, version):
    """
    Format the versioned schema.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id, e.g: P00000001
    collection_id : str
        The collection_id, e.g: C00000001
    version: str
        The version number, e.g: 2

    Returns
    -------
    str
        Absolute schema.json collection absolute path.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    validators.validate_metadata_version_number(version)
    metadata_versions_path = format_metadata_versions_path(project_id, collection_id)
    return "{}/schema.{}.json".format(metadata_versions_path, version)


def format_instance_versioned_collection_path(project_id, collection_id, version):
    """
    Format the versioned instance.json collection absolute path based on the token and the dropzone type.

    Parameters
    ----------
    project_id : str
        The project_id e.g: P00000001
    collection_id : str
        The collection_id e.g: C00000001
    version: str
        The version number, e.g: 2

    Returns
    -------
    str
        Absolute instance.json collection absolute path.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    validators.validate_metadata_version_number(version)
    metadata_versions_path = format_metadata_versions_path(project_id, collection_id)
    return "{}/instance.{}.json".format(metadata_versions_path, version)


def format_metadata_versions_path(project_id, collection_id):
    """
    Format the .metadata_versions collection absolute path based on the project_id and collection_id

    Parameters
    ----------
    project_id : str
        The project_id e.g: P00000001
    collection_id : str
        The collection_id e.g: C00000001

    Returns
    -------
    str
        Absolute .metadata_versions collection absolute path.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    project_collection_path = format_project_collection_path(project_id, collection_id)
    return "{}/.metadata_versions".format(project_collection_path)


def format_project_path(project_id):
    """
    Validate the project ID and format the project path

    Parameters
    ----------
    project_id: str
        The project id, e.g: P000000001

    Returns
    -------
    str
        The formatted path

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    if validators.validate_project_id(project_id):
        return "/nlmumc/projects/{}".format(project_id)


def format_project_collection_path(project_id, collection_id):
    """
    Validate and format the projectcollection path

    Parameters
    ----------
    project_id: str
        The project id, e.g: P000000001
    collection_id: str
        The collection id, e.g: C000000001

    Returns
    -------
    str
        The formatted path

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path
    """
    project_collection_path = "/nlmumc/projects/{}/{}".format(project_id, collection_id)
    if validators.validate_project_collection_path(project_collection_path):
        return project_collection_path


def get_project_id_from_project_path(project_path):
    """
    Return the project_id from the project path

    Parameters
    ----------
    project_path
        The full path of the project

    Returns
    -------
        The project id or None
    """
    match = re.search(r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/?$", project_path)
    if match is not None:
        return match.group("project")
    raise exceptions.ValidationError("Invalid project path {}".format(project_path))


def get_project_id_from_project_collection_path(project_collection_path):
    """
    Return the project_id from the projectcollection path

    Parameters
    ----------
    project_collection_path: str
        The full path of the project collection

    Returns
    -------
    str
        The project id or None
    """
    match = re.search(
        r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/(?P<collection>C[0-9]{9})?/?", project_collection_path
    )
    if match is not None:
        return match.group("project")
    raise exceptions.ValidationError("Invalid project collection path {}".format(project_collection_path))


def get_project_path_from_project_collection_path(project_collection_path):
    """
    Return the project path from the projectcollection path

    Parameters
    ----------
    project_collection_path: str
        The full path of the project collection

    Returns
    -------
    str
        The project path or None

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project path
    """
    match = re.search(
        r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/(?P<collection>C[0-9]{9})?/?", project_collection_path
    )
    if match is not None:
        return format_project_path(match.group("project"))
    raise exceptions.ValidationError("Invalid project collection path {}".format(project_collection_path))


def get_collection_id_from_project_collection_path(project_collection_path):
    """
    Return the collection_id from the projectcollection path

    Parameters
    ----------
    project_collection_path: str
        The full path of the project collection

    Returns
    -------
    str
        The collection id
    """
    match = re.search(
        r"^(/nlmumc/projects/)?(?P<project>P[0-9]{9})/?(?P<collection>C[0-9]{9})/?", project_collection_path
    )
    if match is not None:
        return match.group("collection")
    raise exceptions.ValidationError("Invalid project collection path {}".format(project_collection_path))


def format_boolean_to_string(boolean):
    """
    Formats a python boolean to a json compatible boolean

    Parameters
    ----------
    boolean: bool
        True or False

    Returns
    -------
    str
        "true" if True, "false" if False
    """
    if boolean:
        return "true"
    return "false"


def format_string_to_boolean(string):
    """
    Formats a json boolean string to a python boolean

    Parameters
    ----------
    string: str
        "true" or anything else

    Returns
    -------
    bool
        True if "true", False if anything else
    """
    if string == "true":
        return True
    return False

def get_is_dropzone_modifiable(state: DropzoneState):
    """
    Gets if the dropzone is modifiable (can ingest it, can edit it, can change its ACLs)

    Parameters
    ----------
    state: DropzoneState
        The state of the dropzone to check

    Returns
    -------
    True if it is part of a specific list of states

    """
    if state in (DropzoneState.OPEN, DropzoneState.WARNING_VALIDATION_INCORRECT):
        return True
    return False
