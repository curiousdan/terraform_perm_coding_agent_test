"""German configuration for prod environment in region2."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date

sc1 = frozenset([
    SomeClass1("user1", region="europe-west3", expiry=date(2025, 9, 16), machine_type="n1-standard-2"),
    SomeClass1("user2", region="europe-west3", expiry=date(2025, 9, 17), machine_type="n1-standard-2"),
    SomeClass1("user1", region="europe-west3", expiry=date(2025, 9, 16), machine_type="n1-standard-4"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="europe-west3-a", expiry=date(2025, 9, 16)).with_config(vpc_name="german-prod-vpc"),
    SomeClass2("user1", zone="europe-west3-b", expiry=date(2025, 9, 16)).with_config(db_tier="db-n1-standard-1"),
    SomeClass2("user1", zone="europe-west3-c", expiry=date(2025, 9, 16)).with_config(cache_policy="max-age=3600"),
])