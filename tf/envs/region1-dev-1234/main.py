"""Main Terraform stack configuration for region1-dev-1234."""

from tf.stack import TerraformStack, SomeDeployment
from .poodle_configs_dev import sc1 as poodle_sc1, sc2 as poodle_sc2


def create_infrastructure():
    """Create the Terraform infrastructure for region1-dev environment."""

    # Create main stack
    stack = TerraformStack(
        name="region1-dev-stack",
        project_id="dev-project-1234",
        region="us-central1"
    )

    # Configure network with properties for users 1 & 2
    stack.add_network("dev-vpc", "10.1.0.0/16").someproperty(["user1", "user2"])

    # Add GCS assets
    stack.add_gcs_bucket("region1-dev-data-bucket", "us-central1")
    stack.add_gcs_bucket("region1-dev-backup-bucket", "us-central1")

    # Create deployments
    poodle_deployment = SomeDeployment("poodle", "dev", "us-central1")
    poodle_deployment.add_sc1(sc1=poodle_sc1).add_sc2(sc2=poodle_sc2)

    aussie_deployment = SomeDeployment("aussie", "dev", "us-central1")
    # Aussie uses same configs for dev
    aussie_deployment.add_sc1(sc1=poodle_sc1).add_sc2(sc2=poodle_sc2)

    return {
        "stack": stack,
        "deployments": [poodle_deployment, aussie_deployment]
    }


if __name__ == "__main__":
    infrastructure = create_infrastructure()
    print(f"Created infrastructure: {infrastructure['stack'].name}")
    for deployment in infrastructure["deployments"]:
        print(f"Deployment: {deployment}")
        print(f"Status: {deployment.deploy()}")