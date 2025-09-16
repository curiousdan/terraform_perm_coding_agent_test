"""Poodle configuration for prod environment in region1."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("poodle-compute-prod-1", region="us-central1", machine_type="n1-standard-4"),
    SomeClass1("poodle-compute-prod-2", region="us-central1", machine_type="n1-standard-4"),
    SomeClass1("poodle-storage-prod-1", region="us-central1", machine_type="n1-standard-2"),
])

sc2 = frozenset([
    SomeClass2("poodle-network-prod-1", zone="us-central1-a").with_config(vpc_name="poodle-prod-vpc"),
    SomeClass2("poodle-database-prod-1", zone="us-central1-b").with_config(db_tier="db-n1-standard-2"),
    SomeClass2("poodle-backup-prod-1", zone="us-central1-c").with_config(backup_schedule="daily"),
])