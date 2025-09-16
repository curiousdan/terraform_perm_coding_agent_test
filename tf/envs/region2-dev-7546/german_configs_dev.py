"""German configuration for dev environment in region2."""

from tf.modules import SomeClass1, SomeClass2

sc1 = frozenset([
    SomeClass1("german-web-dev-1", region="europe-west3", machine_type="e2-medium"),
    SomeClass1("german-app-dev-1", region="europe-west3", machine_type="e2-small"),
])

sc2 = frozenset([
    SomeClass2("german-network-dev-1", zone="europe-west3-a").with_config(vpc_name="german-dev-vpc"),
    SomeClass2("german-db-dev-1", zone="europe-west3-b").with_config(db_tier="db-f1-micro"),
])