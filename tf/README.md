# Mock Terraform GCP Repository

This is a mock Terraform repository for creating assets on Google Cloud Platform (GCP).

## Structure

- `linter/` - Contains linting utilities and mock constants
- `tf/` - Main Terraform configuration
  - `modules/` - Reusable Terraform modules
  - `envs/` - Environment-specific configurations

## Environments

- `region1-dev-1234` - Development environment in region 1
- `region1-prod-23456` - Production environment in region 1
- `region2-dev-7546` - Development environment in region 2
- `region2-prod-8753` - Production environment in region 2

## Usage

Each environment contains configuration files and a main.py that defines the infrastructure stack.