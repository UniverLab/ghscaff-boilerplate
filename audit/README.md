# {{name}}

{{description}}. One UniverLab audit engagement, kept in its own private repository so that nobody who works on it can see any other client's audit.

## Layout

```
brief/AUDITOR-BRIEF.md   what is audited, what is forbidden, how to rate and what to hand in
sandbox/                 the local harness the auditor runs against (never production)
audit/audit.json         the univerlab.audit/1 contract: findings, evidence, sources, page sections
audit/assets/            every evidence file audit.json references, each with bytes and sha256
report/                  the written report and its PDF (TeXForge)
```

## Flow

1. **Brief.** Fill in `brief/AUDITOR-BRIEF.md`: pinned commits, scope, forbidden traffic, coverage areas.
2. **Audit.** The auditor works in `sandbox/` and delivers `audit/` and `report/report.md`. Every pull request runs the contract validator and a credential scan.
3. **Report.** Typeset `report/report.md` with TeXForge and add the PDF to `deliverables` in `audit.json`.
4. **Private page.** From a univerlab checkout: `node scripts/audit.ts push <this repo>/audit --slug {{name}}`. The client reads it at `https://univerlab.org/audits/{{name}}/` behind an Access PIN sent to `access.emails`.
5. **Zenodo draft.** `node scripts/audit.ts deposit <this repo>/audit --draft --prod`: a draft with a reserved DOI, visible only to the lab. Nothing is public and the draft can be discarded.
6. **Fixes.** Each finding moves from `open` to `fixed` (with the fixing commit), `accepted` or `wont-fix`. No critical or high finding may stay `open`.
7. **Publication**, only with the client's written consent (`deposit.consent: true`): `visibility: "public"`, `meta.status: "final"`, then `node scripts/audit.ts deposit <this repo>/audit --prod` publishes the draft and mints the DOI. A re-audit is a new version of the same record.

## Confidentiality

- This repository holds one client's data. Never copy findings, evidence or names into another audit repository.
- Evidence never contains a real credential, personal data of the client's users or production secrets. Redact before you commit; CI rejects common token formats but cannot catch everything.
- Access is granted per person to this repository only, and removed when the engagement ends. Then the repository is archived.
