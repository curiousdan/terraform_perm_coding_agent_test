"""Poodle configuration for dev environment in region1."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("poodle-compute-dev-1", region="us-central1", machine_type="e2-medium"),
    SomeClass1("poodle-storage-dev-1", region="us-central1", machine_type="e2-small"),
])

sc2 = frozenset([
    SomeClass2("poodle-network-dev-1", zone="us-central1-a").with_config(vpc_name="poodle-dev-vpc"),
    SomeClass2("poodle-database-dev-1", zone="us-central1-b").with_config(db_tier="db-f1-micro"),
])