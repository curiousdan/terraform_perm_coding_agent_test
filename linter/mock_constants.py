"""Mock constants for Terraform linting."""

DEFAULT_REGION = "us-central1"
DEFAULT_ZONE = "us-central1-a"
PROJECT_ID = "mock-gcp-project-123456"

ALLOWED_MACHINE_TYPES = [
    "n1-standard-1",
    "n1-standard-2",
    "n1-standard-4",
    "e2-medium",
    "e2-standard-2",
]

TERRAFORM_VERSION = "1.5.0"
PROVIDER_VERSIONS = {
    "google": "4.84.0",
    "google-beta": "4.84.0",
}

LINT_RULES = {
    "require_tags": True,
    "enforce_naming_convention": True,
    "check_resource_limits": True,
    "validate_network_config": True,
}