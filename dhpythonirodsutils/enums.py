"""This module contains the enum classes for diverse entities"""
from enum import Enum


class DropzoneAVUs(Enum):
    """Enumerate dropzone size and validation AVUs in iRODS."""

    # Total bytes measured by the periodic size calculation, stored as a string.
    DROPZONE_SIZE = "dropzoneSize"
    # UTC Unix seconds of the latest size calculation, stored as a string.
    DROPZONE_SIZE_UPDATED = "dropzoneSizeUpdated"
    # Total bytes found by the pre-ingest content scan, stored as a string.
    TOTAL_SIZE = "totalSize"
    # File count from the pre-ingest content scan, stored as a string.
    NUM_FILES = "numFiles"
    # "true" if the content scan found no unsupported paths, otherwise "false".
    IS_INGESTABLE = "isIngestable"


class DropzoneState(Enum):
    """Enumerate all the possible DropZone states AVUs in iRODS"""

    OPEN = "open"
    IN_QUEUE_FOR_VALIDATION = "in-queue-for-validation"
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


# region Resources
class ResourceStatus(Enum):
    """Enumerate statuses accepted when modifying an iRODS resource.

    Catalog queries can return an empty string for an up resource. Preserve
    that representation when returning raw catalog status to callers.
    """

    UP = "up"
    DOWN = "down"


class ReplicaStatus(Enum):
    """Enumerate DATA_REPL_STATUS values returned as strings by GenQuery.

    Incomplete or locked replicas (2, 3, 4) are reset to stale before cleanup
    by the existing ingest and tape recovery rules.
    """

    # Replica is out of date or incomplete.
    STALE = "0"
    # Replica is current and valid.
    GOOD = "1"
    # Replica is being created or updated and has not been finalized.
    INTERMEDIATE = "2"
    READ_LOCKED = "3"
    WRITE_LOCKED = "4"


# endregion


# region Ingest
class IngestAttribute(Enum):
    """Enumerate ingest AVU names and their value types.

    Coordination AVUs belong to the dropzone. Maintenance AVUs belong to the
    zone-wide ingest maintenance collection.
    """

    # Values: IngestTransferState; written by the coordinator.
    TRANSFER_STATE = "ingestTransferState"
    # Values: IngestStopRequestState; reset by the coordinator, set by rods.
    STOP_REQUESTED = "ingestStopRequested"
    # Values: IngestWorkerResult; removed before each transfer, written by the worker.
    WORKER_RESULT = "ingestWorkerResult"
    # Values: non-negative UTC Unix seconds, stored as strings; end must follow start.
    MAINTENANCE_START = "maintenanceStart"
    MAINTENANCE_END = "maintenanceEnd"


class IngestTransferState(Enum):
    """Enumerate values for 'IngestAttribute.TRANSFER_STATE'.

    These describe the current transfer, rather than the entire ingest workflow.
    Read DropzoneState separately to determine the ingest outcome.
    """

    # Worker exit or completion of failure handling has not yet been confirmed.
    # This can remain stale after a remote callback failure or service restart.
    ACTIVE = "active"
    # Worker exited, mounted access was restored, and stop failure handling
    # completed with the dropzone in error-ingestion.
    STOPPED = "stopped"
    # Transfer ended without a confirmed stop, including ordinary failures.
    FINISHED = "finished"


class IngestStopRequestState(Enum):
    """Enumerate values for 'IngestAttribute.STOP_REQUESTED'.

    A request does not confirm worker exit; a timeout leaves it requested.
    """

    # The coordinator resets the flag before starting each transfer.
    NOT_REQUESTED = "false"
    # rods requested cancellation; the worker checks this flag while copying.
    REQUESTED = "true"


class IngestWorkerResult(Enum):
    """Enumerate values for 'IngestAttribute.WORKER_RESULT'.

    The coordinator removes this AVU before each transfer. An absent AVU reads
    as an empty string and means worker exit has not yet been reported.
    """

    # The worker exited after cancellation handling; coordinator handling may remain.
    STOPPED = "stopped"
    # The worker exited normally or with an ordinary failure; success is not implied.
    EXITED = "exited"


# endregion


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
