"""Golden configuration for dev environment in region1."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date, timedelta

sc1 = frozenset([
    SomeClass1("user1", region="us-central1", expiry=date.today() + timedelta(days=1), machine_type="n1-standard-1"),
    SomeClass1("user1", region="us-central1", expiry=date.today() + timedelta(days=1), machine_type="e2-medium"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="us-central1-a", expiry=date.today() + timedelta(days=1)).with_config(load_balancer_type="HTTP"),
    SomeClass2("user1", zone="us-central1-c", expiry=date.today() + timedelta(days=1)).with_config(memory_size="1GB"),
])