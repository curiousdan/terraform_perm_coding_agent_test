"""Mock TerraformStack and SomeDeployment classes."""

from typing import Dict, Any, List, Optional, Set
from .modules import SomeClass1, SomeClass2


class TerraformStack:
    """Mock Terraform stack for GCP resources."""

    def __init__(self, name: str, project_id: str, region: str):
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resources = []
        self.network_config = {}

    def add_network(self, name: str, cidr: str = "10.0.0.0/16") -> "TerraformStack":
        """Add a VPC network to the stack."""
        self.network_config = {
            "name": name,
            "cidr": cidr,
            "subnets": []
        }
        return self

    def someproperty(self, users: List[str]) -> "TerraformStack":
        """Configure network properties for users."""
        if "network_config" not in self.__dict__ or not self.network_config:
            self.network_config = {}

        self.network_config["allowed_users"] = users
        self.network_config["firewall_rules"] = [f"allow-{user}" for user in users]
        return self

    def add_gcs_bucket(self, name: str, location: str = None) -> "TerraformStack":
        """Add a GCS bucket to the stack."""
        bucket = {
            "type": "google_storage_bucket",
            "name": name,
            "location": location or self.region
        }
        self.resources.append(bucket)
        return self

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "project_id": self.project_id,
            "region": self.region,
            "network": self.network_config,
            "resources": self.resources
        }


class SomeDeployment:
    """Mock deployment class for managing SomeClass1 and SomeClass2 instances."""

    def __init__(self, name: str, environment: str, region: str):
        self.name = name
        self.environment = environment
        self.region = region
        self.sc1_instances: Set[SomeClass1] = set()
        self.sc2_instances: Set[SomeClass2] = set()

    def add_sc1(self, sc1: Set[SomeClass1]) -> "SomeDeployment":
        """Add SomeClass1 instances to the deployment."""
        self.sc1_instances.update(sc1)
        return self

    def add_sc2(self, sc2: Set[SomeClass2]) -> "SomeDeployment":
        """Add SomeClass2 instances to the deployment."""
        self.sc2_instances.update(sc2)
        return self

    def deploy(self) -> Dict[str, Any]:
        """Mock deploy method."""
        return {
            "name": self.name,
            "environment": self.environment,
            "region": self.region,
            "sc1_count": len(self.sc1_instances),
            "sc2_count": len(self.sc2_instances),
            "status": "deployed"
        }

    def __repr__(self):
        return f"SomeDeployment(name='{self.name}', env='{self.environment}', region='{self.region}')"