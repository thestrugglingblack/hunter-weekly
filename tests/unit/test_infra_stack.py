import aws_cdk as core
import aws_cdk.assertions as assertions

from infra.infra_stack import HunterWeeklyStack

import unittest
import aws_cdk as cdk
from aws_cdk.assertions import Template
from infra.infra_stack import HunterWeeklyStack

class TestHunterWeeklyStack(unittest.TestCase):

    def setUp(self):
        self.app = cdk.App()
        self.stack = HunterWeeklyStack(self.app, "TestStack")
        self.template = Template.from_stack(self.stack)

    def test_stack_initialization(self):
        self.assertIsNotNone(self.stack, "Stack initialization failed.")

    def test_lambda_function_created(self):
        self.assertTrue(self.template.has_resource("AWS::Lambda::Function", {}),
                        "Lambda function resource not found in the stack.")

    def test_event_rule_created(self):
        self.assertTrue(self.template.has_resource("AWS::Events::Rule", {}),
                        "Event rule resource not found in the stack.")

if __name__ == '__main__':
    unittest.main()