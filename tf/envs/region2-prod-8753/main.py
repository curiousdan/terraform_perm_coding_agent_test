"""Main Terraform stack configuration for region2-prod-8753."""

from tf.stack import TerraformStack, SomeDeployment
from .german_configs_prod import sc1 as german_sc1, sc2 as german_sc2


def create_infrastructure():
    """Create the Terraform infrastructure for region2-prod environment."""

    # Create main stack
    stack = TerraformStack(
        name="region2-prod-stack",
        project_id="prod-project-8753",
        region="europe-west3"
    )

    # Configure network with properties for both users (mixing it up)
    stack.add_network("german-prod-vpc", "10.4.0.0/16").someproperty(["user1", "user2"])

    # Add GCS assets
    stack.add_gcs_bucket("region2-prod-german-bucket", "europe-west3")
    stack.add_gcs_bucket("region2-prod-german-backup", "europe-west3")

    # Create german deployment
    german_deployment = SomeDeployment("german", "prod", "europe-west3")
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