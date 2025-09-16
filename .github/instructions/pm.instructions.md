---
applyTo: "**/tf/**/*.py"
---

Copilot Coding Agent: Permissions Update Rules

Purpose

Standardize how to handle user requests to add permissions/resources across Terraform mock configs. Keep it deterministic, validate inputs strictly, and structure logic so new permission types are easy to add.

Required Inputs

- date: ISO date (YYYY-MM-DD) or relative duration like "3 days"
- name: principal/identifier to be added (e.g., a username)
- perm: permission/resource type. Supported: sc1, sc2, bb (alias for sc1), network

If any are missing, respond with: "Cannot proceed: missing required input(s): <list>" and stop.

Environment Resolution

- region: accept aliases
  - reg1 or region1 → region1
  - reg2 or region2 → region2
- env: dev or prod. If not provided, assume dev.

Date Handling

- If ISO date provided, use it as a literal date object: date(YYYY, M, D)
- If relative (e.g., "3 days"), compute deterministically via CLI before edits and insert the literal date:
  - Command: python -c 'from datetime import date, timedelta; print(date.today() + timedelta(days=3))'
  - Parse output YYYY-MM-DD → use date(YYYY, M, D)

Target Discovery

- Find the environment directory by prefix:
  - tf/envs/<region>-<env>-*/
  - If multiple match, select the one that matches the requested region and env (there is typically exactly one).
- Within that directory:
  - Stack config files: any file matching *_configs_<env>.py (e.g., golden_configs_dev.py, poodle_configs_prod.py)
  - Main stack file: main.py

Permissions Registry (extensible)

Define behavior per permission. To add a new permission type, create a new entry mirroring the structure below.

permissions:
  sc1:
    description: Add a SomeClass1 entry to each stack config file in the target env directory.
    target: env_config.sc1
    constructor: SomeClass1
    add:
      - In each *_configs_<env>.py:
        - Ensure 'from datetime import date' is present (remove timedelta if unused).
        - Determine region string by reading existing sc1 entries in that file (e.g., "us-central1" for region1, "europe-west3" for region2). Reuse the same region value.
        - Append a new element inside the sc1 frozenset([...]) with matching indentation and style:
          SomeClass1("<name>", region="<inferred-region>", expiry=date(YYYY, M, D))
        - Do not remove or alter existing entries. If an identical name already exists, update its expiry instead of duplicating.

  bb:
    aliasFor: sc1

  sc2:
    description: Add a SomeClass2 entry to each stack config file in the target env directory.
    target: env_config.sc2
    constructor: SomeClass2
    add:
      - In each *_configs_<env>.py:
        - Ensure 'from datetime import date' is present (remove timedelta if unused).
        - Determine zone string by reading existing sc2 entries in that file. Reuse the first entry's zone. If none exist, default zones: region1 → "us-central1-a", region2 → "europe-west3-a".
        - Append a new element inside the sc2 frozenset([...]) with matching indentation and style, applying required default config:
          SomeClass2("<name>", zone="<inferred-zone>", expiry=date(YYYY, M, D)).with_config(db_tier="db-n1-standard-1")
        - If an identical identifier already exists, update its expiry and ensure config includes db_tier="db-n1-standard-1".

  network:
    description: Add the user to the allowed users in the main stack's network someproperty.
    target: main.someproperty
    add:
      - Open tf/envs/<region>-<env>-*/main.py
      - Locate the chained call: stack.add_network(...).someproperty([...])
      - Ensure the "<name>" appears once in the list (add if missing). Preserve order and existing users.

General Editing Rules

- Preserve file formatting:
  - Keep indentation style and width identical to surrounding code.
  - Maintain trailing commas and list/frozenset layout as in the file.
- Do not refactor unrelated code.
- When adding imports, group with existing imports and avoid duplicates.
- Use literal dates via date(YYYY, M, D); do not compute at runtime.

Stack Selection

- If the request does not specify a particular stack (e.g., golden/poodle/german), apply the change to all stack config files in the environment directory.
- If a stack is specified, only modify that stack's *_configs_<env>.py file.

Validation & Errors

- Before editing, validate required inputs (date|relative, name, perm). If any are missing, reply exactly:
  "Cannot proceed: missing required input(s): <comma-separated-list>"
- Validate perm against the registry (including aliases). If unknown, reply:
  "Cannot proceed: unknown permission '<perm>'. Supported: sc1, sc2, bb, network"
- Validate region alias and env; if invalid, reply with the accepted values.

Examples (concise)

- Input: { region: reg1, env: prod, perm: sc2, name: alice, date: 2025-10-01 }
  - Edit all *_configs_prod.py in tf/envs/region1-prod-*/ to append:
    SomeClass2("alice", zone="<inferred>", expiry=date(2025, 10, 1)).with_config(db_tier="db-n1-standard-1")

- Input: { region: reg2, perm: network, name: bob, date: 3 days }
  - Compute date via CLI (do not insert the command output anywhere): use the literal date in any added expiry fields if applicable.
  - Edit tf/envs/region2-dev-*/main.py (env defaults to dev) and ensure someproperty([...]) contains "bob".

Extensibility

- To add a new permission type, add a new entry under permissions with:
  - description, target, constructor (if applicable), and add steps
  - required defaults or config specifics
  - file selection rules if different from the standard patterns
