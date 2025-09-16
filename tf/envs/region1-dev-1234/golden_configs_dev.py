"""Golden configuration for dev environment in region1."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("golden-api-dev-1", region="us-central1", machine_type="n1-standard-1"),
    SomeClass1("golden-worker-dev-1", region="us-central1", machine_type="e2-medium"),
])

sc2 = frozenset([
    SomeClass2("golden-lb-dev-1", zone="us-central1-a").with_config(load_balancer_type="HTTP"),
    SomeClass2("golden-cache-dev-1", zone="us-central1-c").with_config(memory_size="1GB"),
])