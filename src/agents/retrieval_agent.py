import requests
from langchain_core.tools import tool
import boto3

@tool
def call_healthlake_api():
    """Retrieve FIHR data from HealthLake data store"""
    client = boto3.client('healthlake')
    healthlake_data_store_endpoint = "https://healthlake.eu-west-2.amazonaws.com/datastore/2a25fb1ad9af364f7b88985f15e9f634/r4/"
    response = requests.get(healthlake_data_store_endpoint)
    fihr_data = response.json()
    return fihr_data