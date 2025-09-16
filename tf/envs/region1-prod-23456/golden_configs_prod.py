"""Golden configuration for prod environment in region1."""

from tf.modules import SomeClass1, SomeClass2
from datetime import date, timedelta

sc1 = frozenset([
    SomeClass1("user1", region="us-central1", expiry=date.today() + timedelta(days=1), machine_type="n1-standard-4"),
    SomeClass1("user2", region="us-central1", expiry=date.today() + timedelta(days=2), machine_type="n1-standard-4"),
    SomeClass1("user1", region="us-central1", expiry=date.today() + timedelta(days=1), machine_type="n1-standard-2"),
    SomeClass1("user2", region="us-central1", expiry=date.today() + timedelta(days=2), machine_type="n1-standard-2"),
])

sc2 = frozenset([
    SomeClass2("user1", zone="us-central1-a", expiry=date.today() + timedelta(days=1)).with_config(load_balancer_type="HTTPS"),
    SomeClass2("user1", zone="us-central1-b", expiry=date.today() + timedelta(days=1)).with_config(memory_size="8GB"),
    SomeClass2("user1", zone="us-central1-c", expiry=date.today() + timedelta(days=1)).with_config(alert_policy="critical"),
])