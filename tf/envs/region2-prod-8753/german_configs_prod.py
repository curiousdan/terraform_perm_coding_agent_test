"""German configuration for prod environment in region2."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("german-web-prod-1", region="europe-west3", machine_type="n1-standard-2"),
    SomeClass1("german-web-prod-2", region="europe-west3", machine_type="n1-standard-2"),
    SomeClass1("german-app-prod-1", region="europe-west3", machine_type="n1-standard-4"),
])

sc2 = frozenset([
    SomeClass2("german-network-prod-1", zone="europe-west3-a").with_config(vpc_name="german-prod-vpc"),
    SomeClass2("german-db-prod-1", zone="europe-west3-b").with_config(db_tier="db-n1-standard-1"),
    SomeClass2("german-cdn-prod-1", zone="europe-west3-c").with_config(cache_policy="max-age=3600"),
])