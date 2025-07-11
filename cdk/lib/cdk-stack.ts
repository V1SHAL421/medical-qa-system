import {Stack, StackProps} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { ApiGateway } from './ApiGateway';
import { Lambda } from './Lambda';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const api = new ApiGateway(this);

    const healthLakeLambda = new Lambda(this, "handle_healthlake_requests.py")

    api.addIntegration("GET", "/healthlake", healthLakeLambda)
  }
}
