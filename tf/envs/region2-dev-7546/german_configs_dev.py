"""German configuration for dev environment in region2."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date, timedelta

sc1 = frozenset([
    SomeClass1("user1", region="europe-west3", expiry=date.today() + timedelta(days=1), machine_type="e2-medium"),
    SomeClass1("user1", region="europe-west3", expiry=date.today() + timedelta(days=1), machine_type="e2-small"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="europe-west3-a", expiry=date.today() + timedelta(days=1)).with_config(vpc_name="german-dev-vpc"),
    SomeClass2("user1", zone="europe-west3-b", expiry=date.today() + timedelta(days=1)).with_config(db_tier="db-f1-micro"),
])