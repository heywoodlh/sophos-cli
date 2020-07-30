#!/usr/bin/env python3
import argparse
import requests
import json

## argparse arguments
parser = argparse.ArgumentParser(description="Tool to retrieve access token and tenant ID from Sophos")
parser.add_argument('--client-id', help='Sophos Central API Client ID', metavar='ID', required=True)
parser.add_argument('--client-secret', help='Sophos Central API Secret', metavar='SECRET', required=True)

args = parser.parse_args()


def main():
    client_id = args.client_id
    client_secret = args.client_secret

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'token'
    }
    response = requests.post('https://id.sophos.com/api/v2/oauth2/token', headers=headers, data=data)
    data = json.loads(response.text)
    access_token = str(data['access_token'])

    headers = {
    'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('https://api.central.sophos.com/whoami/v1', headers=headers)
    data = json.loads(response.text)
    tenant_id = data['id']

    print("Access token: " + access_token)
    print("Tenant ID: " + tenant_id)


if __name__ == '__main__':
    main()
