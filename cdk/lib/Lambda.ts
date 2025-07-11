import { Architecture, Runtime } from "aws-cdk-lib/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python-alpha";
import { Construct } from "constructs";
import * as path from 'path';

export class Lambda extends PythonFunction {
    constructor(scope: Construct, fileName: string) {
        super(scope, fileName, {
            architecture: Architecture.ARM_64,
            runtime: Runtime.PYTHON_3_13,
            entry: path.join(__dirname, `../../src/lambda/${fileName}`),
            functionName: fileName,
            environment: {
                OPENAI_API_KEY: process.env.OPENAI_API_KEY || ''
            }
        })
    }
}