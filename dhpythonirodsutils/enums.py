from enum import Enum


class DropzoneState(Enum):
    OPEN = "open"
    VALIDATING = "validating"
    IN_QUEUE_FOR_INGESTION = "in-queue-for-ingestion"
    WARNING_VALIDATION_INCORRECT = "warning-validation-incorrect"
    INGESTING = "ingesting"
    ERROR_INGESTION = "error-ingestion"
    ERROR_POST_INGESTION = "error-post-ingestion"
    INGESTED = "ingested"


class ProjectAVUs(Enum):
    ARCHIVE_DESTINATION_RESOURCE = "archiveDestinationResource"
    AUTHORIZATION_PERIOD_END_DATE = "authorizationPeriodEndDate"
    COLLECTION_METADATA_SCHEMAS = "collectionMetadataSchemas"
    DATA_RETENTION_PERIOD_END_DATE = "dataRetentionPeriodEndDate"
    DATA_STEWARD = "dataSteward"
    ENABLE_ARCHIVE = "enableArchive"
    ENABLE_CONTRIBUTOR_EDIT_METADATA = "enableContributorEditMetadata"
    ENABLE_DROPZONE_SHARING = "enableDropzoneSharing"
    ENABLE_OPEN_ACCESS_EXPORT = "enableOpenAccessExport"
    ENABLE_UNARCHIVE = "enableUnarchive"
    INGEST_RESOURCE = "ingestResource"
    PRINCIPAL_INVESTIGATOR = "OBI:0000103"
    RESOURCE = "resource"
    RESPONSIBLE_COST_CENTER = "responsibleCostCenter"
    STORAGE_QUOTA_GB = "storageQuotaGb"
    TITLE = "title"


class ProjectCollectionActions(Enum):
    ARCHIVE = ProjectAVUs.ENABLE_ARCHIVE.value
    BROWSE = "BROWSE"
    # EDIT_METADATA = ProjectAVUs.ENABLE_CONTRIBUTOR_EDIT_METADATA.value
    PUBLISH = ProjectAVUs.ENABLE_OPEN_ACCESS_EXPORT.value
    UNARCHIVE = ProjectAVUs.ENABLE_UNARCHIVE.value
