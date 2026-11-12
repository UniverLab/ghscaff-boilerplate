# Sandbox

Everything the auditor needs to exercise the system locally: mocks of external services, fake users, probes and load scripts. Production is never a target.

- Secrets here are fake values, and the README says so for each one.
- Defaults that reach the internet (telemetry, update checks, announcements) are switched off before handing the sandbox over.
- The auditor records every change made to the sandbox in the report's method section.
