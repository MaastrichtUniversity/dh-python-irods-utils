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