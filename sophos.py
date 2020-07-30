#!/usr/bin/env python3
import argparse
import requests

## argparse arguments
parser = argparse.ArgumentParser(description="Wrapper for Sophos Central's API")
parser.add_argument('--api', help='Sophos Central API token', metavar='TOKEN', required=True)
parser.add_argument('-g', '--gateway', help='Sophos Central API Gateway', metavar='GATEWAY', required=True)
parser.add_argument('--auth', help='Sophos Central Basic Auth Token', metavar='TOKEN', required=True)
subparsers = parser.add_subparsers(help='commands', dest='command')

## Events subparser
parser_events = subparsers.add_parser('events', help='Retrieve sophos central event info')

## Alerts subparser
parser_events = subparsers.add_parser('alerts', help='Retrieve sophos central alert info')

args = parser.parse_args()


def main():
    gateway = args.gateway
    apikey = args.api
    authtoken = args.auth

    headers = {
    'x-api-key': apikey,
    'Authorization': 'Basic ' + authtoken
    }

    if args.command == 'events':
        gateway = gateway + '/siem/v1/events'
    if args.command == 'alerts':
        gateway = gateway + '/siem/v1/alerts'
    response = requests.get(gateway, headers=headers)
    print(response.text)



if __name__ == '__main__':
    main()
