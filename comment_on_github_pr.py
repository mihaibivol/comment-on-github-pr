#!/usr/bin/env python

import sys

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from github import Github

def parse_args():
    """Parse arguments"""
    arg_parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

    arg_parser.add_argument('-r', '--repo',
            nargs = 1,
            required = True,
            type = str,
            help = 'Repository of the Pull Request')

    arg_parser.add_argument('-n', '--pull-number',
            nargs = 1,
            required = True,
            type = int,
            help = 'Pull Request number')

    arg_parser.add_argument('-l', '--login-or-token',
            nargs = 1,
            required = True,
            type = str,
            help = 'Github login or token')

    arg_parser.add_argument('-p', '--password',
            nargs = 1,
            required = False,
            type = str,
            help = ('Github password.'
                   'Required if using username/password login'))

    arg_parser.add_argument('-m', '--message',
            nargs = 1,
            required = True,
            type = str,
            help = 'Comment message body')

    return arg_parser.parse_args(sys.argv[1:])

if __name__ == '__main__':
    args = vars(parse_args())
    pull_number = args['pull_number'][0]
    repo = args['repo'][0]
    login_or_token = args['login_or_token'][0]
    password = args['password'][0] if args['password'] else None
    message = args['message'][0]

    github = Github(login_or_token=login_or_token, password=password)
    pr = github.get_repo(repo).get_pull(pull_number)
    pr.create_issue_comment(message)
