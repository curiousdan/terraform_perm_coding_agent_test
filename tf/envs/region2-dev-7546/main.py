"""Main Terraform stack configuration for region2-dev-7546."""

from tf.stack import TerraformStack, SomeDeployment
from .german_configs_dev import sc1 as german_sc1, sc2 as german_sc2


def create_infrastructure():
    """Create the Terraform infrastructure for region2-dev environment."""

    # Create main stack
    stack = TerraformStack(
        name="region2-dev-stack",
        project_id="dev-project-7546",
        region="europe-west3"
    )

    # Configure network with properties for user 2 only (mixing it up)
    stack.add_network("german-dev-vpc", "10.3.0.0/16").someproperty(["user2"])

    # Add GCS assets
    stack.add_gcs_bucket("region2-dev-german-bucket", "europe-west3")

    # Create german deployment
    german_deployment = SomeDeployment("german", "dev", "europe-west3")
    german_deployment.add_sc1(sc1=german_sc1).add_sc2(sc2=german_sc2)

    return {
        "stack": stack,
        "deployments": [german_deployment]
    }


if __name__ == "__main__":
    infrastructure = create_infrastructure()
    print(f"Created infrastructure: {infrastructure['stack'].name}")
    for deployment in infrastructure["deployments"]:
        print(f"Deployment: {deployment}")
        print(f"Status: {deployment.deploy()}")