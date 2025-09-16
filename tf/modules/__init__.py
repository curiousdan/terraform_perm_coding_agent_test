"""Terraform modules with mock classes."""

from typing import Dict, Any, Optional
from datetime import date


class SomeClass1:
    """Mock class representing a GCP resource configuration."""

    def __init__(self, name: str, region: str = "us-central1", expiry: Optional[date] = None, **kwargs):
        self.name = name
        self.region = region
        self.expiry = expiry
        self.properties = kwargs

    def __repr__(self):
        if getattr(self, "expiry", None) is not None:
            return f"SomeClass1(name='{self.name}', region='{self.region}', expiry={self.expiry})"
        return f"SomeClass1(name='{self.name}', region='{self.region}')"

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "name": self.name,
            "region": self.region,
            **self.properties
        }
        if self.expiry is not None:
            result["expiry"] = self.expiry
        return result


class SomeClass2:
    """Mock class representing another GCP resource configuration."""

    def __init__(self, identifier: str, zone: str = "us-central1-a", expiry: Optional[date] = None, config: Optional[Dict] = None):
        self.identifier = identifier
        self.zone = zone
        self.expiry = expiry
        self.config = config or {}

    def __repr__(self):
        if getattr(self, "expiry", None) is not None:
            return f"SomeClass2(identifier='{self.identifier}', zone='{self.zone}', expiry={self.expiry})"
        return f"SomeClass2(identifier='{self.identifier}', zone='{self.zone}')"

    def with_config(self, **kwargs) -> "SomeClass2":
        """Add configuration options."""
        self.config.update(kwargs)
        return self

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "identifier": self.identifier,
            "zone": self.zone,
            "config": self.config
        }
        if self.expiry is not None:
            result["expiry"] = self.expiry
        return result