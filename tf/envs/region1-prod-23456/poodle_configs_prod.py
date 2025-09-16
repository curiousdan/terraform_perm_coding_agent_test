"""Poodle configuration for prod environment in region1."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date

sc1 = frozenset([
    SomeClass1("user1", region="us-central1", expiry=date(2025, 9, 16), machine_type="n1-standard-4"),
    SomeClass1("user2", region="us-central1", expiry=date(2025, 9, 17), machine_type="n1-standard-4"),
    SomeClass1("user1", region="us-central1", expiry=date(2025, 9, 16), machine_type="n1-standard-2"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="us-central1-a", expiry=date(2025, 9, 16)).with_config(vpc_name="poodle-prod-vpc"),
    SomeClass2("user1", zone="us-central1-b", expiry=date(2025, 9, 16)).with_config(db_tier="db-n1-standard-2"),
    SomeClass2("user1", zone="us-central1-c", expiry=date(2025, 9, 16)).with_config(backup_schedule="daily"),
])