def healthlake_handler(event, context):
    print(f"HealthLake handler has been executed: {event}")

    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }