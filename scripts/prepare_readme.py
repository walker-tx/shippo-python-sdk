"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import re
import shutil

try:
    with open("README.md", "r", encoding="utf-8") as rh:
        readme_contents = rh.read()
        GITHUB_URL = "https://github.com/goshippo/shippo-python-sdk.git"
        GITHUB_URL = (
            GITHUB_URL[: -len(".git")] if GITHUB_URL.endswith(".git") else GITHUB_URL
        )
        # links on PyPI should have absolute URLs
        readme_contents = re.sub(
            r"(\[[^\]]+\]\()((?!https?:)[^\)]+)(\))",
            lambda m: m.group(1)
            + GITHUB_URL
            + "/blob/master/"
            + m.group(2)
            + m.group(3),
            readme_contents,
        )

        with open("README-PYPI.md", "w", encoding="utf-8") as wh:
            wh.write(readme_contents)
except Exception as e:
    try:
        print("Failed to rewrite README.md to README-PYPI.md, copying original instead")
        print(e)
        shutil.copyfile("README.md", "README-PYPI.md")
    except Exception as ie:
        print("Failed to copy README.md to README-PYPI.md")
        print(ie)
