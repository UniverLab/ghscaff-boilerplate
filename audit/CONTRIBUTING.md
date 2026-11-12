# Working on this audit (auditors)

You were given access to this repository, and only this one, for one engagement. The client has access to it too: **everything you commit, every branch and every pull request, open or closed, is visible to the client.**

## Rules

- **Only what the client may see.** No internal lab notes, no other clients' names or data, no drafts you would not show. Lab-internal notes go to the lab's own knowledge base, never here.
- **Confidential.** Nothing here leaves this repository: no copies to other repositories, chats, AI tools outside the agreed environment, or personal storage.
- **No production.** Test only in `sandbox/`. Any traffic to the client's production systems, accounts or users is forbidden unless the brief allows it in writing.
- **No real secrets.** Credentials, tokens, keys and personal data of the client's users are redacted before they are committed. If one slips in, tell the lab at once: rewriting history is not enough, the secret has to be rotated.
- **Pull requests only**, squash-merged. CI must pass: the `univerlab.audit/1` validator and the credential scan.
- **Evidence reproduces.** Each transcript starts with the exact commands, environment and preconditions. Each asset is listed in `audit.json` with `bytes` and `sha256`:
  `stat -c %s FILE; sha256sum FILE`
- **When the engagement ends**, your access is removed. Delete any local copy.

## Lab flow

1. **Brief.** Fill in `brief/AUDITOR-BRIEF.md`: pinned commits, scope, forbidden traffic, coverage areas.
2. **Audit.** The auditor works in `sandbox/` and delivers `audit/` and `report/report.md` by pull request.
3. **Report.** The lab typesets `report/report.md` with TeXForge and points `deliverables.report` at the PDF.
4. **Private page.** From a univerlab checkout: `node scripts/audit.ts push <this repo>/audit --slug {{name}}`. The client reads it behind an Access PIN sent to `access.emails`.
5. **Delivery.** `meta.status` becomes `delivered`, and the client's chosen GitHub accounts are invited with read access.
6. **Zenodo draft.** `node scripts/audit.ts deposit <this repo>/audit --draft --prod`: a draft with a reserved DOI, visible only to the lab.
7. **Fixes.** Findings move from `open` to `fixed` (with the fixing commit), `accepted` or `wont-fix`, each re-tested or justified. Disputes and re-test requests arrive as issues.
8. **Publication**, only with the client's written consent (`deposit.consent: true`) and no critical or high finding `open`: `visibility` `"public"`, `meta.status` `"final"`, then `node scripts/audit.ts deposit <this repo>/audit --prod` publishes the draft and mints the DOI. A re-audit is a new version of the same record.
