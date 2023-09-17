import os
from abcli import file
import abcli
from abcli.plugins import markdown
from kamangir import NAME, VERSION
from kamangir.content import content
from functools import reduce
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def update():
    logger.info("kamangir.update")

    abcli_path_git = os.getenv("abcli_path_git", "")
    if not abcli_path_git:
        logger.error("-bracket: build: abcli_path_git: variable not found.")
        return False

    success, home_md = file.load_text(
        os.path.join(
            abcli_path_git,
            "kamangir/assets/home.md",
        )
    )
    if not success:
        return success

    items = [
        "[![image]({})]({})".format(item["image"], item["url"])
        for name, item in content["items"].items()
        if name != "template"
    ]
    logger.info(
        "{} item(s) loaded: {}".format(
            len(content["items"]),
            ", ".join(list(content["items"].keys())),
        )
    )

    table = markdown.generate_table(items, content["cols"])

    home_md = reduce(
        lambda x, y: x + y,
        [
            table
            if "--table--" in line
            else [
                "---",
                "built by [`{}`](https://github.com/kamangir/awesome-bash-cli), based on `{}-{}`.".format(
                    abcli.fullname(),
                    NAME,
                    VERSION,
                ),
            ]
            if "--signature--" in line
            else [line]
            for line in home_md
        ],
        [],
    )

    return file.save_text(
        os.path.join(
            abcli_path_git,
            "kamangir/README.md",
        ),
        home_md,
    )
