"""Mock Terraform linter implementation."""

from typing import List, Dict, Any
from .mock_constants import LINT_RULES, ALLOWED_MACHINE_TYPES


class MockTerraformLinter:
    """A mock Terraform linter for GCP resources."""

    def __init__(self, rules: Dict[str, bool] = None):
        self.rules = rules or LINT_RULES
        self.warnings = []
        self.errors = []

    def lint_resource(self, resource: Dict[str, Any]) -> Dict[str, List[str]]:
        """Lint a single Terraform resource."""
        warnings = []
        errors = []

        # Check naming convention
        if self.rules.get("enforce_naming_convention"):
            if not resource.get("name", "").startswith(("dev-", "prod-", "staging-")):
                warnings.append("Resource name should start with environment prefix")

        # Check machine type
        if resource.get("type") == "google_compute_instance":
            machine_type = resource.get("machine_type")
            if machine_type not in ALLOWED_MACHINE_TYPES:
                errors.append(f"Machine type {machine_type} not allowed")

        # Check tags
        if self.rules.get("require_tags"):
            if not resource.get("tags"):
                warnings.append("Resource missing required tags")

        return {"warnings": warnings, "errors": errors}

    def lint_file(self, file_path: str) -> Dict[str, Any]:
        """Mock lint a Terraform file."""
        return {
            "file": file_path,
            "warnings": ["Mock warning: Consider using latest provider version"],
            "errors": [],
            "score": 85
        }