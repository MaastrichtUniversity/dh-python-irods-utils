import pytest

from dhpythonirodsutils import validators
from dhpythonirodsutils.enums import ProjectAVUs
from dhpythonirodsutils.exceptions import ValidationError


@pytest.mark.parametrize(
    "full_path",
    [
        "/nlmumc/projects/P000000001/C000000001",
        "/nlmumc/projects/P000000001/C000000001/bla/blabla/tx.txt",
        "/nlmumc/projects/P123456789/C987564321/blab/.././blob/tx.txt",
    ],
)
def test_validate_full_path_safety_valid(full_path):
    assert validators.validate_full_path_safety(full_path)


@pytest.mark.parametrize(
    "full_path",
    [
        "/nlmumc/projects/P000000002/C000000003/blab/../../../../blob/tx.txt",
        "/nlmumc/projects/P123456789/C987564321/blab/../../.././blob/tx.txt",
        "/nlmumc/projects/P000000001/C000000001/blab/../../blob/tx.txt",
    ],
)
def test_validate_full_path_safety_invalid(full_path):
    with pytest.raises(ValidationError):
        validators.validate_full_path_safety(full_path)


@pytest.mark.parametrize(
    "path",
    [
        "/nlmumc/projects/P000000001/C000000001/bla/blabla/tx.txt",
        "/nlmumc/projects/P000000001/C000000001/blab/../blob/tx.txt",
    ],
)
def test_validate_path_safety_valid(path):
    basedir = "/nlmumc/projects/P000000001/C000000001"
    assert validators.validate_path_safety(basedir, path)


@pytest.mark.parametrize(
    "path",
    [
        "/nlmumc/projects/P000000001/C000000001/blab/../../../../blob/tx.txt",
        "/nlmumc/projects/P000000001/C000000001/blab/../../../blob/tx.txt",
        "/nlmumc/projects/P000000001/C000000001/blab/../../blob/tx.txt",
        "/nlmumc/projects/P000000001/C000000002",
        "/nlmumc/projects/P000000001/C000000002/foobar",
    ],
)
def test_validate_path_safety_invalid(path):
    basedir = "/nlmumc/projects/P000000001/C000000001"
    with pytest.raises(ValidationError):
        validators.validate_path_safety(basedir, path)


@pytest.mark.parametrize(
    "project_id",
    [
        "P000000001",
        "P123000001",
        "P123456789",
    ],
)
def test_validate_project_id_valid(project_id):
    assert validators.validate_project_id(project_id)


@pytest.mark.parametrize(
    "project_id",
    [
        "wrong",
        "P0000000011",
        "C000000001",
        1,
    ],
)
def test_validate_project_id_invalid(project_id):
    with pytest.raises(ValidationError):
        validators.validate_project_id(project_id)


@pytest.mark.parametrize(
    "project_path",
    [
        "/nlmumc/projects/P000000001",
        "/nlmumc/projects/P000000002",
        "/nlmumc/projects/P987654321",
    ],
)
def test_validate_project_path_valid(project_path):
    assert validators.validate_project_path(project_path)


@pytest.mark.parametrize(
    "project_path",
    [
        "/nlmumc/projects/P0000000011111/C000000001",
        "/nlmumc/projects/P0000000011111/C000000001/",
        "/nlmumc/projects/P00000001/C00000000022",
        "/nlmumc2/projects/P000000001/C00000000022/",
        "/nlmumc/projectss/P000000001/C123456789",
        "P0000000011111",
        "C123456789",
    ],
)
def test_validate_project_path_invalid(project_path):
    with pytest.raises(ValidationError):
        validators.validate_project_id(project_path)


@pytest.mark.parametrize(
    "collection_id",
    [
        "C000000001",
        "C000000321",
        "C987654321",
    ],
)
def test_validate_collection_id_valid(collection_id):
    assert validators.validate_collection_id(collection_id)


@pytest.mark.parametrize(
    "collection_id",
    ["collection_id", "C00000001", "C0000000011"],
)
def test_validate_collection_id_invalid(collection_id):
    with pytest.raises(ValidationError):
        validators.validate_collection_id(collection_id)


@pytest.mark.parametrize(
    "project_collection_path",
    [
        "/nlmumc/projects/P000000001/C000000001",
        "/nlmumc/projects/P000000002/C000000002",
        "/nlmumc/projects/P987654321/C123456789",
    ],
)
def test_validate_project_collection_path_valid(project_collection_path):
    validators.validate_project_collection_path(project_collection_path)


@pytest.mark.parametrize(
    "project_collection_path",
    [
        "/nlmumc/projects/P0000000011111/C000000001",
        "/nlmumc/projects/P0000000011111/C000000001/zxc",
        "/nlmumc/projects/P00000001/C00000000022",
        "/nlmumc2/projects/P000000001/C00000000022/ewq",
        "/nlmumc/projectss/P000000001/C123456789",
        "C123456789",
    ],
)
def test_validate_project_collection_path_invalid(project_collection_path):
    with pytest.raises(ValidationError):
        validators.validate_project_collection_path(project_collection_path)


@pytest.mark.parametrize(
    "file_path",
    [
        "/nlmumc/projects/P000000001/C000000001/schema.json",
        "/nlmumc/projects/P123456789/C987654321/instance.json",
        "/nlmumc/projects/P000000001/C000000001/.metadata_versions/schema.json",
    ],
)
def test_validate_file_path_valid(file_path):
    assert validators.validate_file_path(file_path)


@pytest.mark.parametrize(
    "file_path",
    [
        "/nlmumc/projects/P000000001/C000000001schema.json",
        "/nlmumc/projects/P123456789/C9876543210/instance.json",
        "/nlmumc/projects/P0000000010/C000000001/.metadata_versions/schema.json",
    ],
)
def test_validate_file_path_invalid(file_path):
    with pytest.raises(ValidationError):
        validators.validate_file_path(file_path)


@pytest.mark.parametrize(
    "dropzone_type",
    [
        "mounted",
        "direct",
    ],
)
def test_validate_dropzone_type_valid(dropzone_type):
    assert validators.validate_dropzone_type(dropzone_type)


@pytest.mark.parametrize(
    "dropzone_type",
    [
        "wrong",
        "foobar",
        "",
        0,
        1,
        -1,
    ],
)
def test_validate_dropzone_type_invalid(dropzone_type):
    with pytest.raises(ValidationError):
        validators.validate_dropzone_type(dropzone_type)


@pytest.mark.parametrize(
    "path",
    [
        "/nlmumc/projects/P000000001/C000000001",
        "/nlmumc/projects/P000000002/C000000002",
        "/nlmumc/projects/P987654321/C123456789",
        "/nlmumc/projects/P000000001",
        "/nlmumc/projects/P000000002",
        "/nlmumc/projects/P987654321",
    ],
)
def test_validate_irods_collection_valid(path):
    assert validators.validate_irods_collection(path)


@pytest.mark.parametrize(
    "path",
    [
        "/nlmumc/projects/P0000000011111/C000000001",
        "/nlmumc/projects/P0000000011111/C000000001/",
        "/nlmumc/projects/P00000001/C00000000022",
        "/nlmumc2/projects/P000000001/C00000000022/",
        "/nlmumc/projectss/P000000001/C123456789",
        "P0000000011111",
        "C123456789",
    ],
)
def test_validate_irods_collection_invalid(path):
    with pytest.raises(ValidationError):
        validators.validate_irods_collection(path)


@pytest.mark.parametrize(
    "token",
    [
        "crazy-frog",
        "cool-bird",
    ],
)
def test_validate_dropzone_token_valid(token):
    assert validators.validate_dropzone_token(token)


@pytest.mark.parametrize(
    "token",
    [
        "wrong",
        "-bird",
        "hola-",
        "-",
    ],
)
def test_validate_dropzone_token_invalid(token):
    with pytest.raises(ValidationError):
        validators.validate_dropzone_token(token)


@pytest.mark.parametrize(
    "version",
    [
        "1",
        "42",
        "123456789",
        "987564321",
    ],
)
def test_validate_metadata_version_number_valid(version):
    assert validators.validate_metadata_version_number(version)


@pytest.mark.parametrize(
    "version",
    [
        "-1",
        "42.",
        "123456789.42",
        ".987564321",
    ],
)
def test_validate_metadata_version_number_invalid(version):
    with pytest.raises(ValidationError):
        validators.validate_metadata_version_number(version)


@pytest.mark.parametrize(
    "string_boolean",
    [
        "true",
        "false",
    ],
)
def test_validate_string_boolean_valid(string_boolean):
    assert validators.validate_string_boolean(string_boolean)


@pytest.mark.parametrize(
    "string_boolean",
    [
        "False",
        "True",
        "foobar",
        "$#@#!#",
        "gg",
        "1234",
    ],
)
def test_validate_string_boolean_invalid(string_boolean):
    with pytest.raises(ValidationError):
        validators.validate_string_boolean(string_boolean)


@pytest.mark.parametrize(
    "budget_number",
    [
        "UM-12345678901B",
        "UM-01234567890R",
        "UM-12345678901N",
        "UM-01234567890E",
        "UM-01234567890A",
        "UM-01234567890Z",
        "UM-0123456789",
        "XXXXXXXXX",
        "AZM-012345",
    ],
)
def test_validate_budget_number_valid(budget_number):
    assert validators.validate_budget_number(budget_number)


@pytest.mark.parametrize(
    "budget_number",
    [
        "UM-12345678901b",
        "UM-0123456789r",
        "UM-12345678901.N",
        "MU-01234567890E",
        "UM-01234567890",
        "hola",
        "MUMC-012345",
        1234567890,
    ],
)
def test_validate_budget_number_invalid(budget_number):
    with pytest.raises(ValidationError):
        validators.validate_budget_number(str(budget_number))


@pytest.mark.parametrize(
    "action",
    [
        "ARCHIVE",
        "UNARCHIVE",
        "BROWSE",
    ],
)
def test_validate_project_collection_action_name_valid(action):
    assert validators.validate_project_collection_action_name(action)


@pytest.mark.parametrize(
    "action",
    [
        "WRONG",
        42,
        0.0,
    ],
)
def test_validate_project_collection_action_name_invalid(action):
    with pytest.raises(ValidationError):
        validators.validate_project_collection_action_name(action)


@pytest.mark.parametrize(
    "attribute",
    [
        ProjectAVUs.ENABLE_ARCHIVE.value,
        ProjectAVUs.ENABLE_UNARCHIVE.value,
        "BROWSE",
        ProjectAVUs.ENABLE_OPEN_ACCESS_EXPORT.value,
    ],
)
def test_validate_project_collections_action_avu_valid(attribute):
    assert validators.validate_project_collections_action_avu(attribute)


@pytest.mark.parametrize(
    "attribute",
    [
        "WRONG",
        42,
        0.0,
    ],
)
def test_validate_project_collections_action_avu_valid(attribute):
    with pytest.raises(ValidationError):
        validators.validate_project_collections_action_avu(attribute)


@pytest.mark.parametrize(
    "budget_number",
    [
        "UM-12345678901B",
        "UM-01234567890R",
        "UM-12345678901N",
        "UM-01234567890E",
        "UM-01234567890A",
        "UM-01234567890Z",
        "UM-0123456789",
        "XXXXXXXXX",
        "AZM-012345",
    ],
)
def test_validate_budget_number_valid(budget_number):
    assert validators.validate_budget_number(budget_number)


@pytest.mark.parametrize(
    "budget_number",
    [
        "UM-12345678901b",
        "UM-0123456789r",
        "UM-12345678901.N",
        "MU-01234567890E",
        "UM-01234567890",
        "hola",
        "MUMC-012345",
        1234567890,
    ],
)
def test_validate_budget_number_invalid(budget_number):
    with pytest.raises(ValidationError):
        validators.validate_budget_number(str(budget_number))


@pytest.mark.parametrize(
    "action",
    [
        "ARCHIVE",
        "UNARCHIVE",
        "BROWSE",
    ],
)
def test_validate_project_collection_action_name_valid(action):
    assert validators.validate_project_collection_action_name(action)


@pytest.mark.parametrize(
    "action",
    [
        "WRONG",
        42,
        0.0,
    ],
)
def test_validate_project_collection_action_name_invalid(action):
    with pytest.raises(ValidationError):
        validators.validate_project_collection_action_name(action)


@pytest.mark.parametrize(
    "attribute",
    [
        ProjectAVUs.ENABLE_ARCHIVE.value,
        ProjectAVUs.ENABLE_UNARCHIVE.value,
        "BROWSE",
        ProjectAVUs.ENABLE_OPEN_ACCESS_EXPORT.value,
    ],
)
def test_validate_project_collections_action_avu_valid(attribute):
    assert validators.validate_project_collections_action_avu(attribute)


@pytest.mark.parametrize(
    "attribute",
    [
        "WRONG",
        42,
        0.0,
    ],
)
def test_validate_project_collections_action_avu_valid(attribute):
    with pytest.raises(ValidationError):
        validators.validate_project_collections_action_avu(attribute)
