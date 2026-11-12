# Audit brief: {{description}}

You are an independent auditor. You did not build this software and you owe it nothing. Find out what is wrong with it, prove each problem with evidence, and say plainly how serious it is. Do not soften findings, do not praise, and do not take a claim in the docs as true until you have checked it. If you checked an area and found nothing, say what you did: that is a result too.

## 1. What is audited (pinned)

| Repo or system | Commit or version | What it is |
|---|---|---|
| `<url>` | `<commit>` | <one line> |

Every code reference in the audit links to these commits.

## 2. Scope

In scope:
- <area>

Out of scope, and **forbidden**:
- Any traffic to production: <domains, accounts, third-party services>. Everything runs in `sandbox/`.
- Opening issues or pull requests outside this repository, contacting anyone, publishing anything.
- <third-party software beyond how the system uses it>

## 3. What to cover

Each area ends up in the coverage table with a verdict: the finding ids it produced, or "checked, nothing found" plus what you did. Go deeper where the risk is highest.

1. **<area>:** <what to look at>

## 4. The sandbox

`sandbox/` is the local harness: <what it contains>. Read `sandbox/README.md`.

- It is a tool, not a verdict. Read a probe before you trust its output.
- Its probes encode what the developers already thought to check. Your best findings will probably come from what it does not probe.
- Its secrets are fake. Never put a real credential anywhere.
- If it is broken, fix it and record the change in the method section.

## 5. Rating

- **severity:** `critical` = remote compromise of a host or account, or data exposure across users, with no unusual preconditions. `high` = the same with a precondition (a victim's click, a malicious input, a local attacker), or a complete bypass of a security control. `medium` = a weakened control, a realistic denial of service, or a leak of low-sensitivity data. `low` = defence in depth, or hard to exploit. `info` = an observation, or a usage or docs problem with no security impact. Usage problems that block a new user are `medium`.
- **likelihood** (1–5): 1 = needs insider access or a chain of unlikely events; 3 = a motivated attacker or an ordinary mistake can trigger it; 5 = it happens in normal use or with one trivial request.
- **impact** (1–5): 1 = cosmetic; 3 = one user's data or one host degraded; 5 = code execution, account takeover, or every user affected.
- **effort** to fix: `small` (hours), `medium` (days), `large` (a design change).
- **status:** every finding starts as `open`. Leave `cost` out.

## 6. Evidence

Every finding needs at least one evidence asset and, where code is involved, a source pointing at the exact lines at the pinned commit.

- **Transcript** (`kind: "code"` or `"data"`, `.txt`): the exact commands, environment and preconditions first, then the full output.
- **Screenshot** (`kind: "image"`, `.png`): only when the browser state is the evidence, with real `alt` text.
- **Chart data** (`kind: "data"`, `.json`): for load or performance results.
- **No videos.** Each asset under 5 MB, catalogued with `bytes` and `sha256`.
- Write exploit details in full: the audit stays private until the critical and high findings are fixed.

## 7. Deliverables

1. **`audit/audit.json`**, the `univerlab.audit/1` contract: `meta.status` `"draft"`, `visibility` `"private"`, `deliverables` `{}`.
2. **`audit/assets/`**: every evidence file referenced in `assets`.
3. **`report/report.md`**: executive summary; scope and method (environment, versions, tools, sandbox changes); the coverage table; every finding in full (description, reproduction, root cause with code references, impact, recommendation); what is done well, only when backed by a test you ran; limitations; appendix.

Suggested page sections: a summary (`stats`, `riskMatrix`, `findingsTable`, a short `prose` verdict), scope and method with a Mermaid `diagram` marking trust boundaries, one section per area with findings, coverage (`table`), a fix roadmap (`timeline`) and an appendix (`sources`, `assetCard`s). Cross-reference with `{{finding:F-01}}`, `{{source:id}}`, `{{term:word}}` and `{{asset:id}}`, and define jargon in `glossary`.

## 8. Before you hand it in

- The pull request's CI passes (contract validator and credential scan).
- Every finding has evidence that reproduces it, and every source link points at the pinned commit.
- The coverage table has every area from section 3, and the summary counts match the findings.
- Your final message lists the findings by severity, one line each, and anything you could not test, with the reason.
