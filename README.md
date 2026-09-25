# American National Corpus — static migration

Private staging copy of the ANC website. The live domain has not been moved.

The `site/` directory contains static pages, the original theme assets, public documents, and small corpus text files. Dataset/software archives are kept as release assets rather than in Git history. Their original paths, sizes, SHA-256 checksums, and intended release URLs are listed in `migration/download-manifest.json`.

## Preview

From this repository, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8765/. Internal links use relative paths so the preview also works under a GitHub project-site prefix.

## Verify

```sh
python3 scripts/check_site.py
```

The report is written to `migration/link-check.json`. Missing local links fail the check. References to the original host and external image dependencies are reported separately and must be reviewed before launch. This does not validate every external website or fragment identifier.

## Publishing is pending

This repository and its dataset release are private staging resources. Draft release downloads are not available to public visitors. Do not switch DNS or retire the original server until the remaining checklist is complete.

- Review the static preview and migration notices for former interactive features.
- Confirm the final dataset scope; the full server directory is approximately 80 GiB, substantially larger than the files linked from the captured pages. Unlinked datasets and services have not been migrated.
- Publish the reviewed dataset release and confirm its assets can be downloaded anonymously.
- Decide repository visibility, enable GitHub Pages with GitHub Actions as its source, then run the manual `Publish static website` workflow. The workflow refuses to deploy while the dataset release remains a draft.
- Validate navigation, download checksums, legacy redirects, and the custom domain's HTTPS certificate.
- Arrange DNS access for `anc.org` and `www.anc.org`, retain a private backup, and plan rollback before cutover.

WordPress administration, its database, private content, credentials, plugin logs, CGI programs, and the server configuration are not included. Existing copyright and dataset license statements remain in force; this repository does not relicense the source material.

See [the preview review notes](migration/REVIEW.md) for migration changes and unresolved legacy resources.
