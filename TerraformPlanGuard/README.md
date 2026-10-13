# TerraformPlanGuard

TerraformPlanGuard reviews Terraform plan JSON for destructive deletes, replacements, and changes to sensitive infrastructure.

```bash
terraform show -json tfplan > plan.json
python agent.py plan.json
python -m unittest discover -s tests
```

It never applies a plan. Human review and provider-specific policy checks remain essential.
