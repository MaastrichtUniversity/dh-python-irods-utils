import os
import re
from itertools import takewhile

from dhpythonirodsutils import exceptions
from dhpythonirodsutils.enums import ProjectCollectionActions


def validate_full_path_safety(full_path):
    """
    Validate if the full path provided is safe or not

    Parameters
    ----------
    full_path: str
        The full path to the requested object, e.g: /nlmumc/projects/P000000001/foo/bar/instance.json

    Returns
    -------
    bool
        True, if the path is safe.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a safe path.
    """
    split_path = full_path.split("/")
    # basedir => "/nlmumc/projects/P[0-9]{9}/C[0-9]{9}"
    basedir = "/" + split_path[1] + "/" + split_path[2] + "/" + split_path[3] + "/" + split_path[4]
    return validate_path_safety(basedir, full_path)


# Python 2.7 compatible version of  os.path.commonpath
# According to http://rosettacode.org/wiki/Find_common_directory_path#Python
def commonpath(paths, sep="/"):
    bydirectorylevels = zip(*[p.split(sep) for p in paths])
    return sep.join(x[0] for x in takewhile(allnamesequal, bydirectorylevels))


def allnamesequal(name):
    return all(n == name[0] for n in name[1:])


# https://security.openstack.org/guidelines/dg_using-file-paths.html
# https://github.com/irods/python-irodsclient/blob/main/irods/path/__init__.py#L60
def validate_path_safety(basedir, path):
    """
    Validate if the path provided is safe or not

    Parameters
    ----------
    basedir: str
        The base path, e.g: /nlmumc/projects/P000000001
    path: str
        The path to the requested object, e.g: /nlmumc/projects/P000000001/instance.json

    Returns
    -------
    bool
        True, if the path is safe.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a safe path.
    """
    match_path = os.path.abspath(path)
    # if basedir == os.path.commonpath((basedir, match_path)): # NOT pyhton 2.7 compatible
    if basedir == commonpath([basedir, match_path]):
        return True
    raise exceptions.ValidationError("Path is not safe: {}".format(path))


def validate_project_id(project_id):
    """
    Validate the project id, raise an exception if not valid.

    Parameters
    ----------
    project_id: str
        The project id, e.g: P000000001

    Returns
    -------
    bool
        True, if the project id is valid

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project id.
    """
    if isinstance(project_id, str) and re.search("^P[0-9]{9}$", project_id) is not None:
        return True
    raise exceptions.ValidationError("Invalid project id {}".format(project_id))


def validate_project_path(project_path):
    """
    Validate the project path, raise an exception if not valid.

    Parameters
    ----------
    project_path: str
        The project path, e.g: /nlmumc/projects/P000000001

    Returns
    -------
    bool
        True, if the project path is valid.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project path.
    """
    if re.search("^/nlmumc/projects/P[0-9]{9}$", project_path) is not None:
        return True
    raise exceptions.ValidationError("Invalid project path {}".format(project_path))


def validate_collection_id(collection_id):
    """
    Validate the collection id, raise an exception if not valid.

    Parameters
    ----------
    collection_id: str
        The collection id, e.g: C000000001

    Returns
    -------
    bool
        True, if the collection id is valid.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid collection id.
    """
    if re.search("^C[0-9]{9}$", collection_id) is not None:
        return True
    raise exceptions.ValidationError("Invalid collection id {}".format(collection_id))


def validate_project_collection_path(project_collection_path):
    """
    Validate the project collection path, raise an exception if not valid.

    Parameters
    ----------
    project_collection_path: str
        The project collection path, e.g: /nlmumc/projects/P000000001/C000000001

    Returns
    -------
    bool
        True, if the project collection path is valid.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project collection path.
    """
    if re.search("^/nlmumc/projects/P[0-9]{9}/C[0-9]{9}$", project_collection_path) is not None:
        return True
    raise exceptions.ValidationError("Invalid project collection path {}".format(project_collection_path))


def validate_file_path(file_path):
    """
    Validate the file path, raise an exception if not valid.

    Parameters
    ----------
    file_path: str
        The file path, e.g: /nlmumc/projects/P000000001/C000000001/schema.json

    Returns
    -------
    bool
        True, if the file path is valid.

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid file path.
    """
    if re.search("^/nlmumc/projects/P[0-9]{9}/C[0-9]{9}/", file_path) is not None:
        return True
    raise exceptions.ValidationError("Invalid file path {}".format(file_path))


def validate_dropzone_type(dropzone_type):
    """
    Validate if the dropzone type is either 'mounted' or 'direct'.

    Parameters
    ----------
    dropzone_type: str
        The type of dropzone to create.

    Returns
    -------
    bool
        True if valid, False if not

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not a valid project path.
    """
    if dropzone_type in ["mounted", "direct"]:
        return True
    raise exceptions.ValidationError("Invalid dropzone type {}".format(dropzone_type))


def validate_irods_collection(path):
    """
    Validate an iRODS collection path.

    Parameters
    ----------
    path: str
        The absolute iRODS collection path

    Returns
    -------
    bool
        True if valid

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not valid.
    """
    try:
        validate_project_collection_path(path)
        return True
    except exceptions.ValidationError:
        pass

    try:
        validate_project_path(path)
        return True
    except exceptions.ValidationError:
        pass

    raise exceptions.ValidationError("Invalid irods collection path {}".format(path))


def validate_dropzone_token(token):
    """
    Check if the dropzone token follow the naming convention.

    Parameters
    ----------
    token: str
        The dropzone token value.

    Returns
    -------
    bool
        True if valid

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not valid.

    """
    if re.search(r"^\w+-\w+$", token) is not None:
        return True
    raise exceptions.ValidationError("Invalid dropzone token{}".format(token))


def validate_metadata_version_number(version):
    """
    Check if the string version variable represents a positive integer.

    Parameters
    ----------
    version: str|int
        The metadata version number to check

    Returns
    -------
    bool
        True if valid

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not valid.
    """
    if isinstance(version, int) or (isinstance(version, str) and version.isdigit()):
        return True
    raise exceptions.ValidationError("Invalid version number {}".format(version))


def validate_string_boolean(string_boolean):
    """
    Checks if the string provided can be converted to a legitimate boolean

    Parameters
    ----------
    string_boolean: str
        The string to check

    Returns
    -------
    bool
        True if valid

    Raises
    -------
    ValidationError
        Raises a ValidationError, if not valid.
    """
    if string_boolean not in ("true", "false"):
        raise exceptions.ValidationError("Invalid boolean as string '{}'".format(string_boolean))

    return True


def validate_budget_number(budget_number):
    """
    Check if budget number follow the standard format:
        * UM-{10} or UM-{11digits}[A-Z]
        * AZM-{6digits}
        * XXXXXXXXX if budget number is not specified

    Parameters
    ----------
    budget_number: str
        The budget number to validate

    Returns
    -------
    bool
        True if valid

    Raises
    ------
    ValidationError
        Raises a ValidationError if the budget number doesn't follow of the allowed format
    """
    if re.fullmatch(r"^UM-\d{10}$", budget_number) or re.fullmatch(r"^UM-\d{11}[A-Z]$", budget_number):
        return True
    if re.fullmatch(r"^AZM-\d{6}$", budget_number):
        return True
    if re.fullmatch(r"^XXXXXXXXX$", budget_number):
        return True

    raise exceptions.ValidationError("Invalid budget number as string '{}'".format(budget_number))


def validate_project_collection_action_name(action):
    """
    Check if the action name matches with one of the Enum ProjectCollectionActions names

    Parameters
    ----------
    action: str
        The action name to check

    Returns
    -------
    bool
        True, if valid

    Raises
    ------
    ValidationError
        Raises a ValidationError if the action is not part of the Enum ProjectCollectionActions
    """
    try:
        ProjectCollectionActions[action].value
    except KeyError:
        raise exceptions.ValidationError("Invalid ProjectCollectionActions '{}'".format(action))

    return True


def validate_project_collections_action_avu(attribute):
    """
    Check if the project AVU attribute matches with one of the Enum ProjectCollectionActions values.

    Parameters
    ----------
    attribute: str
        The project AVU attribute to check

    Returns
    -------
    bool
        True, if valid

    Raises
    ------
    ValidationError
        Raises a ValidationError if the action is not part of the Enum ProjectCollectionActions
    """
    if attribute in [actions.value for actions in ProjectCollectionActions]:
        return True
    raise exceptions.ValidationError("Invalid ProjectCollectionActions AVU '{}'".format(attribute))
