"""Compare a reviewed manifest with GitHub's metadata for the tagged release."""

import json
import sys
from pathlib import Path

manifest = json.loads(Path("release-manifest.json").read_text(encoding="utf-8"))
release = json.load(sys.stdin)
tag = manifest["tag"]
if release["tag_name"] != tag or release["draft"] or release["prerelease"]:
    raise SystemExit("Expected the tagged, published release.")
assets = release["assets"]
if len(assets) != len(manifest["assets"]):
    raise SystemExit("Published assets differ from the reviewed manifest.")
for asset in assets:
    name = asset["name"]
    expected = manifest["assets"].get(name)
    expected_url = f"https://github.com/Katmai-Computing/katmai-desktop/releases/download/{tag}/{name}"
    if not expected or asset["size"] != expected["bytes"] or (
        asset.get("digest") != f"sha256:{expected['sha256']}"
    ) or asset["browser_download_url"] != expected_url:
        raise SystemExit(f"Asset metadata differs from the reviewed manifest: {name}")
if len({asset["name"] for asset in assets}) != len(assets):
    raise SystemExit("Published asset names are not unique.")
print(f"Verified {len(assets)} published asset records for {tag}.")
