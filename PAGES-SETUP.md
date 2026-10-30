# Park Lab GitHub Pages

The `docs/` directory is a standalone static website based on the Park Lab reference pages: Home, Publications, Members, and Software. Shared styling and navigation work without a build step. Images and PDFs are included locally.

## Publish on GitHub Pages

After merging, open this repository's **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **master** and **/docs**, and save. GitHub currently reports Pages disabled for this repository; this setting must be enabled before a public site is available.

Expected URL after GitHub completes deployment: https://thejustpark.github.io/

The existing VuePress files remain available as an archive; Pages should serve only `docs/`.

## Edit and preview

Edit `docs/index.html`, `docs/publications.html`, `docs/members.html`, or `docs/software.html`. Common appearance lives in `docs/style.css`; mobile navigation lives in `docs/script.js`. Replace `docs/CV_HJPark_Publications.pdf` to update the publications document.

To preview locally, run `python -m http.server 8000 --directory docs` and open http://localhost:8000.
