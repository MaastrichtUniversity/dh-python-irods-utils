import os
import re
from dhpythonirodsutils import exceptions


def validate_full_path_safety(full_path):
    """
    Validate if the full path provided is safe or not

    Parameters
    ----------
    full_path
        The full path to the requested object, eg /nlmumc/projects/P000000001/foo/bar/instance.json

    """
    split_path = full_path.split("/")
    # basedir => "/nlmumc/projects/P[0-9]{9}/C[0-9]{9}"
    basedir = "/" + split_path[1] + "/" + split_path[2] + "/" + split_path[3] + "/" + split_path[4]
    return validate_path_safety(basedir, full_path)


# https://security.openstack.org/guidelines/dg_using-file-paths.html
# https://github.com/irods/python-irodsclient/blob/main/irods/path/__init__.py#L60
def validate_path_safety(basedir, path):
    """
    Validate if the path provided is safe or not

    Parameters
    ----------
    basedir
        The base path, eg /nlmumc/projects/P000000001
    path
        The path to the requested object, eg /nlmumc/projects/P000000001/instance.json

    """
    match_path = os.path.abspath(path)
    if basedir == os.path.commonpath((basedir, match_path)):
        return True
    else:
        raise exceptions.ValidationError("Path is not safe: {}".format(path))


def validate_project_id(project_id):
    """
    Validate the project id, raise an exception if not valid.

    Parameters
    ----------
    project_id
        The project id, eg P000000001

    """
    if re.search("^P[0-9]{9}$", project_id) is not None:
        return True
    else:
        raise exceptions.ValidationError("Invalid project id {}".format(project_id))


def validate_project_path(project_path):
    """
    Validate the project path, raise an exception if not valid.

    Parameters
    ----------
    project_path
        The project path, eg /nlmumc/projects/P000000001

    """
    if re.search("^/nlmumc/projects/P[0-9]{9}$", project_path) is not None:
        return True
    else:
        raise exceptions.ValidationError("Invalid project path {}".format(project_path))


def validate_collection_id(collection_id):
    """
    Validate the collection id, raise an exception if not valid.

    Parameters
    ----------
    collection_id
        The project id, eg C000000001

    """
    if re.search("^C[0-9]{9}$", collection_id) is not None:
        return True
    else:
        raise exceptions.ValidationError("Invalid collection id {}".format(collection_id))


def validate_project_collection_path(project_collection_path):
    """
    Validate the project collection path, raise an exception if not valid.

    Parameters
    ----------
    project_collection_path
        The project path, eg /nlmumc/projects/P000000001/C000000001

    """
    if re.search("^/nlmumc/projects/P[0-9]{9}/C[0-9]{9}$", project_collection_path) is not None:
        return True
    else:
        raise exceptions.ValidationError("Invalid project collection path {}".format(project_collection_path))


def validate_file_path(file_path):
    """
    Validate the file path, raise an exception if not valid.

    Parameters
    ----------
    file_path
        The file path, eg /nlmumc/projects/P000000001/schema.json

    """
    if re.search("^/nlmumc/projects/P[0-9]{9}/C[0-9]{9}/", file_path) is not None:
        return True
    else:
        raise exceptions.ValidationError("Invalid file path {}".format(file_path))


def validate_dropzone_type(dropzone_type):
    """
    Validate if the dropzone type is either 'mounted' or 'direct'

    Parameters
    ----------
    dropzone_type: str
        The type of dropzone to create

    Returns
    -------
    True if valid, False if not

    """
    if dropzone_type in ["mounted", "direct"]:
        return True
    else:
        raise exceptions.ValidationError("Invalid dropzone type {}".format(dropzone_type))
