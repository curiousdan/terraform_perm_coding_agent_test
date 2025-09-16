"""Terraform modules with mock classes."""

from typing import Dict, Any, Optional


class SomeClass1:
    """Mock class representing a GCP resource configuration."""

    def __init__(self, name: str, region: str = "us-central1", **kwargs):
        self.name = name
        self.region = region
        self.properties = kwargs

    def __repr__(self):
        return f"SomeClass1(name='{self.name}', region='{self.region}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "region": self.region,
            **self.properties
        }


class SomeClass2:
    """Mock class representing another GCP resource configuration."""

    def __init__(self, identifier: str, zone: str = "us-central1-a", config: Optional[Dict] = None):
        self.identifier = identifier
        self.zone = zone
        self.config = config or {}

    def __repr__(self):
        return f"SomeClass2(identifier='{self.identifier}', zone='{self.zone}')"

    def with_config(self, **kwargs) -> "SomeClass2":
        """Add configuration options."""
        self.config.update(kwargs)
        return self

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identifier": self.identifier,
            "zone": self.zone,
            "config": self.config
        }