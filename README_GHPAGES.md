# DIPLOMAGIC — GitHub Pages Custom Domain

Generated: 2025-08-18 06:28 ET

## DNS (GoDaddy)
- CNAME `diplomagic` → `goldmanvision.github.io`

## Build and publish from this repo root
```bash
bash ops/site/bin/build.sh
CNAME=diplomagic.goldmanvision.com bash ops/site/bin/deploy_ghpages.sh
bash ops/site/bin/verify.sh
```

## GitHub Pages
- Settings → Pages → Source: `gh-pages` / `root`
- Custom domain: `diplomagic.goldmanvision.com`
- Enforce HTTPS: on

## Domain verification
In this repo's Pages settings, add the TXT record GitHub shows:
- Host: `_github-pages-challenge-goldmanvision.diplomagic`
- Value: `<PASTE_CODE_FROM_GITHUB>`
Then click **Verify** when DNS propagates.
