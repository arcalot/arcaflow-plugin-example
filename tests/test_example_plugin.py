#!/usr/bin/env python3
import unittest
from arcaflow_plugin_example import example_plugin
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            example_plugin.InputParams("Arca Lot")
        )

        plugin.test_object_serialization(
            example_plugin.SuccessOutput("Hello, world!")
        )

    def test_functional(self):
        input = example_plugin.InputParams(name="Arca Lot")

        output_id, output_data = example_plugin.hello_world(input)

        # The example plugin always returns a success:
        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data, example_plugin.SuccessOutput("Hello, Arca Lot!")
        )


if __name__ == "__main__":
    unittest.main()
