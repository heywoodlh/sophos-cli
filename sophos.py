#!/usr/bin/env python3
import argparse
import requests

## argparse arguments
parser = argparse.ArgumentParser(description="Wrapper for Sophos Central's API")
parser.add_argument('--gateway', help='Sophos API URI', metavar='URI', default='https://api-us01.central.sophos.com')
parser.add_argument('--tenant-id', help='Sophos Central Tenant ID', metavar='ID', required=True)
parser.add_argument('--access-token', help='Sophos Central Access Token', metavar='TOKEN', required=True)
parser.add_argument('--page-size', help='Page Size of Retrieved Results', default=50, type=int)
subparsers = parser.add_subparsers(help='commands', dest='command')


## Endpoints subparser
parser_endpoints = subparsers.add_parser('endpoints', help='Retrieve sophos central endpoint info')

## Users subparser

## Groups subparser

## Add user subparser
parser_adduser = subparsers.add_parser('adduser', help='Add new user')
parser_adduser.add_argument('--first-name', help='User first name', metavar='NAME', required=True, type=str)
parser_adduser.add_argument('--last-name', help='User last name', metavar='NAME', required=True, type=str)
parser_adduser.add_argument('--email', help='User email address', metavar='NAME', required=True, type=str)
parser_adduser.add_argument('--sendmail', help='Send an onboarding email', action="store_true")

args = parser.parse_args()


def main():
    gateway = args.gateway
    tenant_id = args.tenant_id
    access_token = args.access_token
    page_size = args.page_size

    authorization_string = "Bearer " + access_token

    headers = {
        'Authorization': authorization_string,
        'X-Tenant-ID': tenant_id
    }

    params = {
        ('pageSize', page_size),
    }

    if args.command == 'endpoints':
        gateway = gateway + '/endpoint/v1/endpoints'
        response = requests.get(gateway, headers=headers, params=params)
        print(response.text)

    if args.command == 'adduser':
        gateway = gateway + '/common/v1/directory/users'




if __name__ == '__main__':
    main()
