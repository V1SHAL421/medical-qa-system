import { RemovalPolicy } from "aws-cdk-lib";
import { LambdaIntegration, LogGroupLogDestination, RestApi } from "aws-cdk-lib/aws-apigateway";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { LogGroup } from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class ApiGateway extends RestApi {
    constructor(scope: Construct) {
        super(scope, 'ApiGateway', {
            restApiName: 'MedicalQASystem',
            description: 'This is a medical QA system',
            deployOptions: {
                stageName: 'dev',
                accessLogDestination: new LogGroupLogDestination(new LogGroup(scope, "ApiLogGroup", {
                    removalPolicy: RemovalPolicy.DESTROY,
                    logGroupName: 'api_gateway'
                }))
                
            },
        });
        }

    addIntegration(method: string, path: string, lambdaFunction: IFunction) {
        const resource = this.root.addResource(path);
        resource.addMethod(method, new LambdaIntegration(lambdaFunction));
        }
    }
