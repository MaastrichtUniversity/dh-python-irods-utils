import pytest
from dhpythonirodsutils import validators
from dhpythonirodsutils import formatters
from dhpythonirodsutils.enums import DropzoneState
from dhpythonirodsutils.exceptions import ValidationError


@pytest.mark.parametrize(
    "token, dropzone_type, dropzone_type_folder_name",
    [
        ("crazy-frog", "mounted", "zones"),
        ("cool-bird", "direct", "direct"),
    ],
)
class TestDropzonePathValid:
    def test_format_dropzone_path_valid(self, token, dropzone_type, dropzone_type_folder_name):
        dropzone_path = formatters.format_dropzone_path(token, dropzone_type)
        assert dropzone_path == "/nlmumc/ingest/{}/{}".format(dropzone_type_folder_name, token)

    def test_format_schema_dropzone_path_valid(self, token, dropzone_type, dropzone_type_folder_name):
        dropzone_path = formatters.format_schema_dropzone_path(token, dropzone_type)
        assert dropzone_path == "/nlmumc/ingest/{}/{}/schema.json".format(dropzone_type_folder_name, token)

    def test_format_instance_dropzone_path_valid(self, token, dropzone_type, dropzone_type_folder_name):
        dropzone_path = formatters.format_instance_dropzone_path(token, dropzone_type)
        assert dropzone_path == "/nlmumc/ingest/{}/{}/instance.json".format(dropzone_type_folder_name, token)


@pytest.mark.parametrize(
    "token, dropzone_type",
    [
        ("wrong-one", "incorrect"),
        ("...-111", "direct"),
        ("nope", "direct"),
        ("-", "direct"),
    ],
)
class TestDropzonePathInvalid:
    def test_format_dropzone_path_invalid(self, token, dropzone_type):
        with pytest.raises(ValidationError):
            formatters.format_dropzone_path(token, dropzone_type)

    def test_format_schema_dropzone_path_invalid(self, token, dropzone_type):
        with pytest.raises(ValidationError):
            formatters.format_schema_dropzone_path(token, dropzone_type)

    def test_format_instance_dropzone_path_invalid(self, token, dropzone_type):
        with pytest.raises(ValidationError):
            formatters.format_instance_dropzone_path(token, dropzone_type)


@pytest.mark.parametrize(
    "project_id, collection_id, version",
    [
        ("P000000001", "C000000001", "1"),
        ("P123000001", "C000000321", "123456789"),
        ("P123456789", "C987654321", "42"),
    ],
)
class TestVersionedCollectionPathValid:
    def test_format_schema_versioned_collection_path_valid(self, project_id, collection_id, version):
        dropzone_path = formatters.format_schema_versioned_collection_path(project_id, collection_id, version)
        assert dropzone_path == "/nlmumc/projects/{}/{}/.metadata_versions/schema.{}.json".format(
            project_id, collection_id, version
        )

    def test_format_instance_versioned_collection_path_valid(self, project_id, collection_id, version):
        dropzone_path = formatters.format_instance_versioned_collection_path(project_id, collection_id, version)
        assert dropzone_path == "/nlmumc/projects/{}/{}/.metadata_versions/instance.{}.json".format(
            project_id, collection_id, version
        )


@pytest.mark.parametrize(
    "project_id, collection_id, version",
    [
        ("P123456789", "C987654321", "-6"),
        ("P123456789", "C987654321", "6.12"),
        ("P123456789", "C987654321", ".42"),
        (1, 11, 1),
    ],
)
class TestVersionedCollectionPathInvalid:
    def test_format_schema_versioned_collection_path_invalid(self, project_id, collection_id, version):
        with pytest.raises(ValidationError):
            formatters.format_schema_versioned_collection_path(project_id, collection_id, version)

    def test_format_instance_versioned_collection_path_invalid(self, project_id, collection_id, version):
        with pytest.raises(ValidationError):
            formatters.format_instance_versioned_collection_path(project_id, collection_id, version)


@pytest.mark.parametrize(
    "project_id, collection_id",
    [
        ("P000000001", "C000000001"),
        ("P123000001", "C000000321"),
        ("P123456789", "C987654321"),
    ],
)
class TestProjectCollectionIdValid:
    def test_format_metadata_versions_path_valid(self, project_id, collection_id):
        dropzone_path = formatters.format_metadata_versions_path(project_id, collection_id)
        assert dropzone_path == "/nlmumc/projects/{}/{}/.metadata_versions".format(project_id, collection_id)

    def test_format_project_collection_path(self, project_id, collection_id):
        dropzone_path = formatters.format_project_collection_path(project_id, collection_id)
        assert dropzone_path == "/nlmumc/projects/{}/{}".format(project_id, collection_id)

    def test_format_schema_collection_path_valid(self, project_id, collection_id):
        dropzone_path = formatters.format_schema_collection_path(project_id, collection_id)
        assert dropzone_path == "/nlmumc/projects/{}/{}/schema.json".format(project_id, collection_id)

    def test_format_instance_collection_path_valid(self, project_id, collection_id):
        dropzone_path = formatters.format_instance_collection_path(project_id, collection_id)
        assert dropzone_path == "/nlmumc/projects/{}/{}/instance.json".format(project_id, collection_id)


@pytest.mark.parametrize(
    "project_id, collection_id",
    [
        ("wrong", "collection_id"),
        ("P0000000011", "C000000001"),
        ("P000000001", "C0000000011"),
        (1, 11),
    ],
)
class TestProjectCollectionInvalid:
    def test_format_metadata_versions_path_invalid(self, project_id, collection_id):
        with pytest.raises(ValidationError):
            formatters.format_metadata_versions_path(project_id, collection_id)

    def test_format_project_collection_path(self, project_id, collection_id):
        with pytest.raises(ValidationError):
            formatters.format_project_collection_path(project_id, collection_id)

    def test_format_schema_collection_path_invalid(self, project_id, collection_id):
        with pytest.raises(ValidationError):
            formatters.format_schema_collection_path(project_id, collection_id)

    def test_format_instance_collection_path_invalid(self, project_id, collection_id):
        with pytest.raises(ValidationError):
            formatters.format_instance_collection_path(project_id, collection_id)


@pytest.mark.parametrize(
    "project_id",
    [
        "P000000001",
        "P123000001",
        "P123456789",
    ],
)
class TestProjectIdValid:
    def test_format_project_path(self, project_id):
        project_path = formatters.format_project_path(project_id)
        assert project_path == "/nlmumc/projects/{}".format(project_id)


@pytest.mark.parametrize(
    "project_id",
    [
        "wrong",
        "P0000000011",
        "C000000001",
        1,
    ],
)
class TestProjectIdInvalid:
    def test_format_project_path(self, project_id):
        with pytest.raises(ValidationError):
            formatters.format_project_path(project_id)


@pytest.mark.parametrize(
    "project_collection_path",
    [
        "/nlmumc/projects/P000000001/C000000001",
        "/nlmumc/projects/P000000002/C000000002/zxc",
        "/nlmumc/projects/P987654321/C123456789",
        "P000000001/C000000002/qwfqwf",
    ],
)
class TestProjectCollectionPathValid:
    def test_get_project_path_from_project_collection_path(self, project_collection_path):
        project_path = formatters.get_project_path_from_project_collection_path(project_collection_path)
        assert validators.validate_project_path(project_path)

    def test_get_project_id_from_project_collection_path(self, project_collection_path):
        project_id = formatters.get_project_id_from_project_collection_path(project_collection_path)
        assert validators.validate_project_id(project_id)

    def test_get_collection_id_from_project_collection_path(self, project_collection_path):
        collection_id = formatters.get_collection_id_from_project_collection_path(project_collection_path)
        assert validators.validate_collection_id(collection_id)


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
class TestProjectCollectionPathInvalid:
    def test_get_project_path_from_project_collection_path(self, project_collection_path):
        with pytest.raises(ValidationError):
            formatters.get_project_path_from_project_collection_path(project_collection_path)

    def test_get_project_id_from_project_collection_path(self, project_collection_path):
        with pytest.raises(ValidationError):
            formatters.get_project_id_from_project_collection_path(project_collection_path)

    def test_get_collection_id_from_project_collection_path(self, project_collection_path):
        with pytest.raises(ValidationError):
            formatters.get_collection_id_from_project_collection_path(project_collection_path)


@pytest.mark.parametrize(
    "project_path",
    [
        "/nlmumc/projects/P000000001/",
        "/nlmumc/projects/P000000002",
        "P000000001/",
        "P000000001",
        "/nlmumc/projects/P987654321",
    ],
)
def test_get_project_id_from_project_path_valid(project_path):
    project_id = formatters.get_project_id_from_project_path(project_path)
    assert validators.validate_project_id(project_id)


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
def test_get_project_id_from_project_path_invalid(project_path):
    with pytest.raises(ValidationError):
        formatters.get_project_id_from_project_path(project_path)


@pytest.mark.parametrize(
    "relative_path",
    [
        "P000000001/C000000001/foo/bar/instance.json",
        "P000000001/foo/bar/instance.json-one",
    ],
)
def test_format_absolute_project_path_valid(relative_path):
    dropzone_path = formatters.format_absolute_project_path(relative_path)
    assert dropzone_path.startswith("/nlmumc/projects/P000000001")


@pytest.mark.parametrize(
    "relative_path",
    [
        "P000000001/foo/../../../../bar/instance.json",
        "P000000001/foo/../bar/instance.json-one",
    ],
)
def test_format_absolute_project_path_invalid(relative_path):
    with pytest.raises(ValidationError):
        formatters.format_absolute_project_path(relative_path)


@pytest.mark.parametrize(
    "boolean",
    [True, False, None, {}, [], 1, -1, 1.42, -1.42],
)
def test_format_boolean_to_string(boolean):
    assert formatters.format_boolean_to_string(boolean) in ["true", "false"]


@pytest.mark.parametrize(
    "string",
    ["true", "false", "random", None, {}, [], 1, -1, 1.42, -1.42],
)
def test_format_string_to_boolean(string):
    assert formatters.format_string_to_boolean(string) in [True, False]


@pytest.mark.parametrize(
    "state,expected_result",
    [
        (DropzoneState.OPEN, True),
        (DropzoneState.WARNING_VALIDATION_INCORRECT, True),
        (DropzoneState.WARNING_UNSUPPORTED_CHARACTER, True),
        (DropzoneState.ERROR_INGESTION, False),
        (DropzoneState.ERROR_POST_INGESTION, False),
        (DropzoneState.INGESTED, False),
        (DropzoneState.INGESTING, False),
    ],
)
def test_get_is_dropzone_state_ingestable(state, expected_result):
    assert formatters.get_is_dropzone_state_ingestable(state) is expected_result


@pytest.mark.parametrize(
    "state,expected_result",
    [
        (DropzoneState.OPEN, False),
        (DropzoneState.WARNING_VALIDATION_INCORRECT, False),
        (DropzoneState.WARNING_UNSUPPORTED_CHARACTER, False),
        (DropzoneState.ERROR_INGESTION, False),
        (DropzoneState.ERROR_POST_INGESTION, False),
        (DropzoneState.INGESTED, False),
        (DropzoneState.INGESTING, True),
        (DropzoneState.IN_QUEUE_FOR_INGESTION, True),
        (DropzoneState.VALIDATING, True),
    ],
)
def test_get_is_dropzone_state_in_active_ingestion(state, expected_result):
    assert formatters.get_is_dropzone_state_in_active_ingestion(state) is expected_result
