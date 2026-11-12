# {{name}}

{{description}}.

This repository is one of the audit's deliverables. It holds everything the audit rests on, so that anyone you give access to can check each finding for themselves:

```
report/                  the written report and its PDF
audit/audit.json         every finding, its evidence and its sources (the univerlab.audit/1 contract)
audit/assets/            the evidence: transcripts, screenshots and data, each with its sha256
brief/AUDITOR-BRIEF.md   what was audited, at which versions, and what was off limits
sandbox/                 the local environment the tests ran in, to reproduce them
```

The same audit is published as a private page at `https://univerlab.org/audits/{{name}}/`, behind a PIN sent to the addresses you gave us.

## Reading a finding

Each finding has a severity (`critical`, `high`, `medium`, `low`, `info`), a likelihood and an impact from 1 to 5, the effort to fix it, and a status:

- `open`: not fixed yet.
- `fixed`: fixed, with the commit or version that fixed it, and re-tested.
- `accepted`: you decided to live with it, and the reason is recorded.
- `wont-fix`: it will not be fixed, and the reason is recorded.

Every finding links to its evidence in `audit/assets/`. A transcript starts with the exact commands, so you can run them again in `sandbox/`.

## Access

Access is by invitation only: tell us the GitHub accounts of the people who should see this repository. They get read access, which is enough to read everything and to open issues. Nobody outside that list and the auditors of this engagement has access.

## Questions, disputes and re-tests

Open an issue: one per finding you want to question or have re-tested after a fix. When a fix is confirmed the finding moves to `fixed` and a new version of the report is issued.

## Publication

Nothing here is published without your written consent. If you consent, once no critical or high finding is `open` the audit can be deposited in Zenodo with a DOI and shown at `https://univerlab.org/workbench/audits/{{name}}/`. This repository stays private unless you ask otherwise.
