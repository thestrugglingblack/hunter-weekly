import os
from dotenv import load_dotenv

from aws_cdk import (
    Stack,
    Duration,
    aws_iam as iam,
    aws_sns as sns,
    aws_lambda as _lambda,
    aws_lambda_destinations as destinations,
    aws_sns_subscriptions as subscriptions,
    aws_events as events,
    aws_events_targets as targets,
    aws_ec2 as ec2
)

from constructs import Construct

load_dotenv()

class HunterWeeklyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "HunterWeeklyVPC",
                      max_azs=2,
                      nat_gateways=1,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                              subnet_type=ec2.SubnetType.PUBLIC,
                              name="PublicSubnet"
                          ),
                          ec2.SubnetConfiguration(
                              subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                              name="PrivateSubnet"
                          )
                      ]
                    )

        role = iam.Role(self, "HunterWeeklyRole",
                        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
                        )

        lambda_execution_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            resources=["*"]
        )

        secrets_manager_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "secretsmanager:GetSecretValue"
            ],
            resources=["*"]
        )

        sns_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "sns:Publish",
                "cloudwatch:*",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            resources=["*"]
        )

        event_bridge_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "events:PutEvents",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "events:DescribeRule",
            ],
            resources=["*"]
        )

        ssm_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "ssm:GetParameter"
            ],
            resources=["*"]
        )

        lambda_vpc_policy = iam.PolicyStatement(effect=iam.Effect.ALLOW,
                                         actions=[
                                             "ec2:CreateNetworkInterface",
                                             "ec2:DescribeNetworkInterfaces",
                                             "ec2:DeleteNetworkInterface"
                                        ],
                                         resources=["*"]
                                         )

        role.add_to_policy(lambda_execution_policy)
        role.add_to_policy(ssm_policy)
        role.add_to_policy(sns_policy)
        role.add_to_policy(secrets_manager_policy)
        role.add_to_policy(event_bridge_policy)
        role.add_to_policy(lambda_vpc_policy)

        # Secrets Manager
        secret_arn = f'arn:aws:secretsmanager:{self.region}:{self.account}:secret:hunter-weekly-call-B4he8c'

        # SNS
        success_topic = sns.Topic(self, "HunterWeeklySuccessTopic")
        failure_topic = sns.Topic(self, "HunterWeeklyFailureTopic")
        email = os.getenv('EMAIL')

        success_topic.add_subscription(subscriptions.EmailSubscription(email))
        failure_topic.add_subscription(subscriptions.EmailSubscription(email))

        # Twilio Layer
        # TODO: Programmatically pull in path for layer.zip
        # TODO: Programmatically create zip function for layer.zip for updates.
        # Note: This is a manual process and the path for pulling dependencies for a lambda_func layer is /python/{NAME_OF_LIBRARIES

        twilio_layer = _lambda.LayerVersion(self, "TwilioLayer",
                                            code=_lambda.Code.from_asset(
                                                '/Users/zuri/Documents/Explore/hunter-weekly/infra/layer.zip'),
                                            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8]
                                            )
        # Lambda
        # TODO: Programmatically pull in path for lambda_func.zip
        # TODO: Programmatically create zip function for lambda_func.zip for updates.
        # Note: This is a manual process and to zip the contents for a lambda_func just include the __init__.py and send_message.py
        lambda_func = _lambda.Function(self, "HunterWeeklyLambda",
                                       runtime=_lambda.Runtime.PYTHON_3_8,
                                       handler="send_message.lambda_handler",  # Zip the contents and not the directory
                                       code=_lambda.Code.from_asset(
                                           '/Users/zuri/Documents/Explore/hunter-weekly/infra/lambda.zip'),
                                       environment={
                                           'SECRET_ARN': secret_arn
                                       },
                                       role=role,
                                       on_success=destinations.SnsDestination(success_topic),
                                       on_failure=destinations.SnsDestination(failure_topic),
                                       layers=[twilio_layer],
                                       vpc=vpc,
                                       vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
                                       timeout=Duration.minutes(5)

                                       )

        # EventBridge
        cron_rule = events.Rule(self, "HunterWeeklyRule",
                                schedule=events.Schedule.expression("cron(0 1 ? * THUR *)"),
                                )
        cron_rule.add_target(targets.LambdaFunction(lambda_func))
