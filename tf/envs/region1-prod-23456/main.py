"""Main Terraform stack configuration for region1-prod-23456."""

from tf.stack import TerraformStack, SomeDeployment
from .poodle_configs_prod import sc1 as poodle_sc1, sc2 as poodle_sc2
from .golden_configs_prod import sc1 as golden_sc1, sc2 as golden_sc2


def create_infrastructure():
    """Create the Terraform infrastructure for region1-prod environment."""

    # Create main stack
    stack = TerraformStack(
        name="region1-prod-stack",
        project_id="prod-project-23456",
        region="us-central1"
    )

    # Configure network with properties for user 1 only (mixing it up)
    stack.add_network("prod-vpc", "10.2.0.0/16").someproperty(["user1"])

    # Add GCS assets
    stack.add_gcs_bucket("region1-prod-data-bucket", "us-central1")
    stack.add_gcs_bucket("region1-prod-backup-bucket", "us-central1")
    stack.add_gcs_bucket("region1-prod-logs-bucket", "us-central1")

    # Create deployments
    poodle_deployment = SomeDeployment("poodle", "prod", "us-central1")
    poodle_deployment.add_sc1(sc1=poodle_sc1).add_sc2(sc2=poodle_sc2)

    aussie_deployment = SomeDeployment("aussie", "prod", "us-central1")
    # Aussie uses golden configs for prod
    aussie_deployment.add_sc1(sc1=golden_sc1).add_sc2(sc2=golden_sc2)

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