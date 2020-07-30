#!/usr/bin/env python3
import argparse
import requests
import sys

## argparse arguments
parser = argparse.ArgumentParser(description="Wrapper for Sophos Central's API")
parser.add_argument('--gateway', help='Sophos API URI', metavar='URI', default='https://api-us01.central.sophos.com')
parser.add_argument('--tenant-id', help='Sophos Central Tenant ID', metavar='ID', required=True)
parser.add_argument('--access-token', help='Sophos Central Access Token', metavar='TOKEN', required=True)
subparsers = parser.add_subparsers(help='commands', dest='command')


## Endpoints subparser
parser_events = subparsers.add_parser('endpoints', help='Retrieve sophos central endpoint info')

args = parser.parse_args()


def main():
    gateway = args.gateway
    tenant_id = args.tenant_id
    access_token = args.access_token


    authorization_string = "Bearer " + access_token

    headers = {
    'Authorization': authorization_string,
    'X-Tenant-ID': tenant_id
    }


    if args.command == 'endpoints':
        gateway = gateway + '/endpoint/v1/endpoints'
    response = requests.get(gateway, headers=headers)
    print(response.text)



if __name__ == '__main__':
    main()
