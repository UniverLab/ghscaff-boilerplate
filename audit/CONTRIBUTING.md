# Working on this audit

You were given access to this repository, and only this one, for one engagement.

- **Confidential.** Nothing here leaves this repository: no copies to other repositories, chats, AI tools outside the agreed environment, or personal storage.
- **No production.** Test only in `sandbox/`. Any traffic to the client's production systems, accounts or users is forbidden unless the brief allows it in writing.
- **No real secrets.** Credentials, tokens, keys and personal data are redacted before they are committed. If one slips in, tell the lab at once: rewriting history is not enough, the secret has to be rotated.
- **Pull requests only.** Work on a branch and open a pull request. CI must pass: the `univerlab.audit/1` validator and the credential scan.
- **Evidence reproduces.** Each transcript starts with the exact commands, environment and preconditions. Each asset is listed in `audit.json` with `bytes` and `sha256`:
  `stat -c %s FILE; sha256sum FILE`
- **When the engagement ends**, your access is removed. Delete any local copy.
