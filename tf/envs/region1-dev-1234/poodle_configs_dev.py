"""Poodle configuration for dev environment in region1."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date

sc1 = frozenset([
    SomeClass1("user1", region="us-central1", expiry=date(2025, 9, 16), machine_type="e2-medium"),
    SomeClass1("user1", region="us-central1", expiry=date(2025, 9, 16), machine_type="e2-small"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="us-central1-a", expiry=date(2025, 9, 16)).with_config(vpc_name="poodle-dev-vpc"),
    SomeClass2("user1", zone="us-central1-b", expiry=date(2025, 9, 16)).with_config(db_tier="db-f1-micro"),
])