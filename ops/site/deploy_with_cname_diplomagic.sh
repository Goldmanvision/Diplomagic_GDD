#!/usr/bin/env bash
set -euo pipefail
bash ops/site/bin/build.sh
CNAME=diplomagic.goldmanvision.com bash ops/site/bin/deploy_ghpages.sh
