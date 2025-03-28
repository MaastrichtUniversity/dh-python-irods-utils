"""This module contains the enum classes for diverse entities"""
from enum import Enum


class DropzoneState(Enum):
    """Enumerate all the possible DropZone states AVUs in iRODS"""

    OPEN = "open"
    VALIDATING = "validating"
    IN_QUEUE_FOR_INGESTION = "in-queue-for-ingestion"
    WARNING_VALIDATION_INCORRECT = "warning-validation-incorrect"
    WARNING_UNSUPPORTED_CHARACTER = "warning-unsupported-character"
    INGESTING = "ingesting"
    ERROR_INGESTION = "error-ingestion"
    ERROR_POST_INGESTION = "error-post-ingestion"
    INGESTED = "ingested"


class ArchiveState(Enum):
    """Enumerate all the possible archival state AVUs in iRODS"""

    IN_QUEUE_FOR_ARCHIVAL = "in-queue-for-archival"
    NUMBER_OF_FILES_FOUND = "Number of files found: {}"
    ARCHIVE_IN_PROGESS = "archive-in-progress {}/{}"
    ERROR_ARCHIVE_FAILED = "error-archive-failed"
    ARCHIVE_DONE = "archive-done"


class UnarchiveState(Enum):
    """Enumerate all the possible unarchival state AVUs in iRODS"""

    IN_QUEUE_FOR_UNARCHIVAL = "in-queue-for-unarchival"
    NUMBER_OF_FILES_OFFLINE = "Number of files offline: {}"
    CACHING_FILES_COUNTDOWN = "Caching files countdown: {}"
    START_TRANSFER = "start-transfer"
    UNARCHIVE_IN_PROGESS = "unarchive-in-progress {}/{}"
    ERROR_UNARCHIVE_FAILED = "error-unarchive-failed"
    UNARCHIVE_DONE = "unarchive-done"


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
    UNARCHIVE = ProjectAVUs.ENABLE_UNARCHIVE.value
    DELETE = "DELETE"


class ProjectActions(Enum):
    """Enumerate the all possible project actions in MDR"""

    DELETE_PROJECT = "DELETE_PROJECT"


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
    DELETE_COLLECTION = "DELETE_COLLECTION"
    DELETE_DROPZONE = "DELETE_DROPZONE"
    DELETE_PROJECT = "DELETE_PROJECT"
    DOWNLOAD_DATA = "DOWNLOAD_DATA"
    EDIT_COLLECTION_METADATA = "EDIT_COLLECTION_METADATA"
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
    # INGEST = "state"


class ProcessType(Enum):
    """Enumerate the type of project collection process type"""

    ARCHIVE = "archive"
    DROP_ZONE = "drop_zone"
    UNARCHIVE = "unarchive"


class ProcessState(Enum):
    """Enumerate the type of project collection process type"""

    COMPLETED = "completed"
    ERROR = "error"
    IN_PROGRESS = "in_progress"
    OPEN = "open"


# endregion


# region Active process
class DataDeletionAttribute(Enum):
    """Enumerate all data project (collection) attribute names"""

    DESCRIPTION = "deletionReasonDescription"
    REASON = "deletionReason"
    STATE = "deletionState"


class DataDeletionState(Enum):
    """Enumerate all the possible project (collection) values for 'DataDeletionAttribute.STATE'"""

    DELETED = "deleted"
    PENDING = "pending-for-deletion"


# endregion
