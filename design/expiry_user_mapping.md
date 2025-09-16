Title: Add expiry date and user mapping to mock Terraform resources

Author: Assistant

Status: Proposed

Owners: You

Problem statement

Add an expiry date to SomeClass1 and SomeClass2 and update all <stack>_configs_<env>.py to:
- Include an expiry date object set to 1 or 2 days from today.
- Replace the first positional field (name/identifier) with either user1 or user2.
- Mapping should be deterministic. We do not need to keep original names.

Goals

- Store expiry as a Python date on instances.
- Deterministically assign user1/user2 and +1/+2 day expiry at config definition time.
- Keep current config semantics otherwise unchanged.

Non-goals

- Persisting or serializing to JSON (keeping date objects as-is is acceptable).
- Any change to deployment logic in tf/stack.py.

Proposed changes

- tf/modules/__init__.py
  - SomeClass1.__init__(..., expiry: date | None = None, **kwargs); set self.expiry.
  - SomeClass2.__init__(..., expiry: date | None = None, config: Optional[Dict] = None); set self.expiry.
  - to_dict() returns expiry as the date object if present; unchanged otherwise.
- All env config files add deterministic mapping and expiry values:
  - Files:
    - tf/envs/region1-dev-1234/golden_configs_dev.py
    - tf/envs/region1-dev-1234/poodle_configs_dev.py
    - tf/envs/region1-prod-23456/golden_configs_prod.py
    - tf/envs/region1-prod-23456/poodle_configs_prod.py
    - tf/envs/region2-dev-7546/german_configs_dev.py
    - tf/envs/region2-prod-8753/german_configs_prod.py
  - Add from datetime import date, timedelta.
  - Replace the first positional field with user1 or user2 per mapping rule below.
  - Pass expiry=... to constructors.

Deterministic mapping rule

- Use the original resource name/identifier’s trailing digit:
  - Odd → name/identifier becomes user1; expiry = date.today() + timedelta(days=1).
  - Even → name/identifier becomes user2; expiry = date.today() + timedelta(days=2).
  - No trailing digit → user1, +1 day.

Compatibility

- Existing calls without expiry still work; expiry is optional and keyword-only usage in configs.
- Sets of instances remain valid; multiple objects can share the same name/identifier.

Testing

- Quick import and execution of both main.py files to ensure no import/type errors.
- Spot-check to_dict() contains expiry date object.

Risks

- date objects are not JSON-serializable; acceptable per non-goals.
- Many instances will map to user1 (most end with 1); acceptable.

Rollout plan

- Phase 1: Update classes in tf/modules/__init__.py.
- Phase 2: Update all env configs with imports, new expiry, and user mapping.
- Phase 3: Sanity run the main.py scripts.


