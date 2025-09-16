"""Golden configuration for prod environment in region1."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("golden-api-prod-1", region="us-central1", machine_type="n1-standard-4"),
    SomeClass1("golden-api-prod-2", region="us-central1", machine_type="n1-standard-4"),
    SomeClass1("golden-worker-prod-1", region="us-central1", machine_type="n1-standard-2"),
    SomeClass1("golden-worker-prod-2", region="us-central1", machine_type="n1-standard-2"),
])

sc2 = frozenset([
    SomeClass2("golden-lb-prod-1", zone="us-central1-a").with_config(load_balancer_type="HTTPS"),
    SomeClass2("golden-cache-prod-1", zone="us-central1-b").with_config(memory_size="8GB"),
    SomeClass2("golden-monitor-prod-1", zone="us-central1-c").with_config(alert_policy="critical"),
])