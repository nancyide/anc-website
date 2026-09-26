# Preserve old dataset download URLs

Status: configuration prepared and validated locally; not deployed. DNS and the live ANC server have not been changed.

The 59 public archive assets are mapped to their verified GitHub Release URLs. The map contains 172 exact hostname/path entries: both `anc.org` and `www.anc.org`, plus the `/oanc/` and `/masc/` aliases confirmed on the original server. Source URLs omit the scheme so each entry covers both HTTP and HTTPS (344 URL variants).

## Import files

- `cloudflare-test-302.csv`: temporary redirects for initial validation.
- `cloudflare-permanent-301.csv`: permanent redirects after the live checks pass.
- `coverage.json`: scope and matching settings.

Both CSVs intentionally omit a header row, as required by Cloudflare. Import only one version at a time into the same dedicated list. Each row has: source URL, destination URL, status code, preserve query string, include subdomains, subpath matching, preserve path suffix. All four options are false. This avoids capturing unrelated subdomains or URLs below an archive filename. Query parameters such as `?download=1` are dropped when redirecting to the exact release file.

These redirects cover the migrated archives, not all files from the approximately 80 GiB original directory. Public small files included in `site/` keep their paths and do not need archive redirects. Other unlinked downloads, application URLs, and files not yet migrated need further inventory before the old server can be retired.

## Selected approach

Use Cloudflare Bulk Redirects in front of GitHub Pages. Cloudflare's Free plan currently includes 10,000 redirect entries, which is sufficient for this map. Redirects require the relevant website DNS records to be proxied through Cloudflare. A standard free setup moves authoritative DNS from Hover to Cloudflare; domain registration does not need to move.

## Account setup and cutover sequence

1. Create/sign in to a Cloudflare account. If creating an account requires accepting terms, the account owner completes that step.
2. Add `anc.org` on the Free plan. Keep the assigned nameservers recorded but do not apply them until the DNS zone has been checked against the complete Hover record list.
3. Copy and compare the full Hover zone, including email, verification, subdomain, and any DNSSEC settings. Public DNS queries are not a complete zone export. Keep a private backup of the existing configuration outside this public repository. The known MX record points to `mail.cs.vassar.edu`; preserve it. Keep email and unrelated services DNS-only.
4. Create a dedicated Bulk Redirect List named `anc_downloads`, import the 302 CSV, and create its matching Bulk Redirect Rule using Cloudflare's default list expression and request URL key. Do not add a catch-all redirect to the GitHub homepage; it would lose page paths and could take priority over the download rules.
5. Plan activation in stages. Initially preserve the current origin records as DNS-only if activating Cloudflare's nameservers separately from the website cutover. Check DNSSEC delegation before changing nameservers. This phase does not activate the redirects.
6. Verify ownership of `anc.org` in GitHub Pages, then configure its custom domain before changing the website's origin records. Coordinate this step: adding the custom domain redirects the `github.io` site URL to that domain. Avoid disrupting the test link prematurely.
7. Set the website records to the documented GitHub Pages origin addresses, obtain the GitHub custom-domain certificate, and ensure Cloudflare's edge certificate is active. The old server's certificate is expired, so do not point a Full (strict) proxy at that origin or weaken TLS to work around it. Enable Cloudflare proxying for the website records once the new origin and certificates are ready; use Full (strict) TLS. Verify that the download rule is enabled when proxying starts.
8. Test real old URLs on both hostnames and both schemes, including HEAD requests and a legacy query string. Confirm page navigation and email DNS as well as redirects. Do not bypass certificate validation.
9. Replace the dedicated list contents with the 301 CSV after the temporary redirects pass. Do not append duplicate sources or overwrite unrelated lists. Re-run the live checks.
10. Keep the old server and DNS configuration available for rollback until the full migration scope has been agreed and checked. Remove the temporary rules or disable the dedicated rule for rollback; permanent redirects may remain cached by clients, which is why the initial stage uses 302.

The final DNS/Cloudflare account configuration still requires access and review. No account IDs, API tokens, private zone exports, or credentials belong in this repository.

## Rebuild and verify

```sh
python3 scripts/prepare_redirects.py
python3 scripts/check_redirects.py
```

After Cloudflare is serving the redirects:

```sh
python3 scripts/check_redirects.py --live
```

The live check validates HTTP status and the exact Location header without downloading archive bodies. It does not follow redirects, so an incorrect homepage redirect cannot be mistaken for success. Download destinations were already verified publicly in `migration/publication-verification.json`.

## Official references

- [Cloudflare redirect availability and proxy requirement](https://developers.cloudflare.com/rules/url-forwarding/)
- [Bulk Redirect CSV format](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/)
- [Redirect matching parameters](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/)
- [Create a Bulk Redirect List and Rule](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/)
- [GitHub Pages custom-domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
