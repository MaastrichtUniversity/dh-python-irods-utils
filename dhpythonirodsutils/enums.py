"""This module contains the enum classes for diverse entities"""
from enum import Enum


class DropzoneState(Enum):
    """Enumerate all the possible DropZone states AVUs in iRODS"""

    OPEN = "open"
    VALIDATING = "validating"
    IN_QUEUE_FOR_INGESTION = "in-queue-for-ingestion"
    WARNING_VALIDATION_INCORRECT = "warning-validation-incorrect"
    INGESTING = "ingesting"
    ERROR_INGESTION = "error-ingestion"
    ERROR_POST_INGESTION = "error-post-ingestion"
    INGESTED = "ingested"


# region Projects
class ProjectAVUs(Enum):
    """Enumerate all the possible Project AVUs in iRODS"""

    ARCHIVE_DESTINATION_RESOURCE = "archiveDestinationResource"
    AUTHORIZATION_PERIOD_END_DATE = "authorizationPeriodEndDate"
    COLLECTION_METADATA_SCHEMAS = "collectionMetadataSchemas"
    DATA_RETENTION_PERIOD_END_DATE = "dataRetentionPeriodEndDate"
    DATA_STEWARD = "dataSteward"
    DESCRIPTION = "description"
    ENABLE_ARCHIVE = "enableArchive"
    ENABLE_CONTRIBUTOR_EDIT_METADATA = "enableContributorEditMetadata"
    ENABLE_DROPZONE_SHARING = "enableDropzoneSharing"
    ENABLE_OPEN_ACCESS_EXPORT = "enableOpenAccessExport"
    ENABLE_UNARCHIVE = "enableUnarchive"
    INGEST_RESOURCE = "ingestResource"
    LATEST_PROJECT_COLLECTION_NUMBER = "latestProjectCollectionNumber"
    PRINCIPAL_INVESTIGATOR = "OBI:0000103"
    RESOURCE = "resource"
    RESPONSIBLE_COST_CENTER = "responsibleCostCenter"
    STORAGE_QUOTA_GB = "storageQuotaGb"
    TITLE = "title"


class ProjectCollectionActions(Enum):
    """Enumerate the all possible project collection actions in MDR"""

    ARCHIVE = ProjectAVUs.ENABLE_ARCHIVE.value
    BROWSE = "BROWSE"
    # EDIT_METADATA = ProjectAVUs.ENABLE_CONTRIBUTOR_EDIT_METADATA.value
    PUBLISH = ProjectAVUs.ENABLE_OPEN_ACCESS_EXPORT.value
    UNARCHIVE = ProjectAVUs.ENABLE_UNARCHIVE.value


# endregion
class AuditTailTopics(Enum):
    """Enumerate the all possible Audit trail topics in logs"""

    ARCHIVE = "ARCHIVE"
    CHANGE_COLLECTION_METADATA_SCHEMA = "CHANGE_COLLECTION_METADATA_SCHEMA"
    CHANGE_PROJECT_AVU = "CHANGE_PROJECT_AVU"
    CHANGE_PROJECT_PERMISSIONS = "CHANGE_PROJECT_PERMISSIONS"
    CHANGE_PROJECT_SCHEMA = "CHANGE_PROJECT_SCHEMA"
    COPY_WEBDAV_DATA = "COPY_WEBDAV_DATA"
    CREATE_DROPZONE = "CREATE_DROPZONE"
    CREATE_PROJECT = "CREATE_PROJECT"
    DELETE_DROPZONE = "DELETE_DROPZONE"
    DOWNLOAD_DATA = "DOWNLOAD_DATA"
    EDIT_COLLECTION_METADATA = "EDIT_COLLECTION_METADATA"
    EXPORT_DATAVERSE = "EXPORT_DATAVERSE"
    INGEST = "INGEST"
    LIST_CO = "LIST_CO"
    LOGIN = "LOGIN"
    POLICY = "POLICY"
    PREVIEW_SCHEMA = "PREVIEW_SCHEMA"
    REFERRED_HANDLE = "REFERRED_HANDLE"
    REQUEST_PROJECT = "REQUEST_PROJECT"
    UNARCHIVE = "UNARCHIVE"
    VIEW_METADATA = "VIEW_METADATA"
    DRAG_AND_DROP = "DRAG_AND_DROP"
    SEARCH = "SEARCH"
    INTEGRATED_HELP = "INTEGRATED_HELP"


# region Active process
class ProcessAttribute(Enum):
    """Enumerate all active process attribute names"""

    ARCHIVE = "archiveState"
    UNARCHIVE = "unArchiveState"
    EXPORTER = "exporterState"
    # INGEST = "state"


class ProcessType(Enum):
    """Enumerate the type of project collection process type"""

    ARCHIVE = "archive"
    DROP_ZONE = "drop_zone"
    EXPORT = "export"
    UNARCHIVE = "unarchive"


class ProcessState(Enum):
    """Enumerate the type of project collection process type"""

    COMPLETED = "completed"
    ERROR = "error"
    IN_PROGRESS = "in_progress"
    OPEN = "open"


# endregion
