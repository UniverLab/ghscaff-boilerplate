# Report

`report.md` is the auditor's full written report. The lab typesets it with TeXForge:

```sh
texforge new pdf          # once: creates the LaTeX project here
texforge build            # writes the PDF
```

Add the PDF to `audit/assets/`, catalogue it with `bytes` and `sha256`, and point `deliverables.report` at it in `audit/audit.json`. `deliverables.report` is required once `meta.status` is `delivered` or `final`.
