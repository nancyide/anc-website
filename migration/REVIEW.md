# Preview review notes

The static preview contains 150 HTML documents: 63 captured WordPress page/post views and 86 legacy HTML documents, plus a legacy-resource notice page. Its total file size is approximately 52 MB. All local HTML links, page asset references, and stylesheet image references passed the filesystem link check, including path casing. External destination websites and fragment identifiers are not comprehensively verified.

## Changes needed for static hosting

- Kept the original ANC theme and main navigation. Replaced the obsolete jQuery menu dependency with CSS hover/focus navigation and removed the old Facebook widget.
- Replaced n-gram search, document uploads, and the protected page's password form with explanatory notices. ANC2Go instructions are retained as historical documentation with links to full corpus downloads.
- Preserved published page paths and rewrote internal links to work both under a project-site prefix and on the final custom domain.
- Linked the 59 copied dataset/software archives to the planned release `datasets-2026-09-25`. These links will become public only when the repository/release access and publication are configured.
- Repaired verified legacy destinations, including the consortium and MASC structure links. The unavailable resources below link to an explicit archive notice instead of depending on the old server.
- Copied existing license/logo images locally. Replaced an Open Data badge whose image host no longer resolves with the text “Open Data,” keeping its surrounding link.
- Added a readable HTML shell to legacy fragments that depended on server-side include comments.
- Excluded private WordPress content, PHP, server settings, database dumps, credentials, and logs. The first-release parent page linked by WordPress returned 404; its children now link to existing public first-release documentation.

## Resources not recovered

- https://anc.org/html/style.css
- https://anc.org/html/registration.html
- http://www.anc.org/svn/project_anctool/trunk/
- http://www.anc.org/wiki/wiki/VerbChunks
- http://www.anc.org/wiki/wiki/NamedEntities
- http://www.anc.org/wiki/wiki/CoReference
- http://www.anc.org/MASC/texts/Re_JobOffer.txt
- https://anc.org/representing.html

## Required before switching the live domain

- Review the functional changes and decide whether any unavailable legacy resource must be recovered before launch.
- Confirm the scope of unlinked server data, applications, and downloads outside this captured site. This migration is not a full backup of the approximately 80 GiB website directory or other server data.
- Complete release upload/verification, publish it, and verify anonymous access.
- Enable Pages and decide repository visibility; private Pages source requires an eligible GitHub plan.
- Arrange redirects for old direct download URLs and obtain DNS access. GitHub Pages alone cannot issue arbitrary binary-path HTTP redirects to release assets.
- Test the final custom domain and valid HTTPS, retain a backup and rollback route, and only then retire the old host.
