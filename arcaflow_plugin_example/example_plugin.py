#!/usr/bin/env python3

import sys
import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import plugin, validation


@dataclass
class InputParams:
    name: typing.Annotated[str, validation.min(1)]


@dataclass
class SuccessOutput:
    message: str


@plugin.step(
    id="hello-world",
    name="Hello world!",
    description="Says hello :)",
    outputs={"success": SuccessOutput},
)
def hello_world(params: InputParams) -> typing.Tuple[str, SuccessOutput]:
    return "success", SuccessOutput("Hello, {}!".format(params.name))


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                hello_world,
            )
        )
    )
