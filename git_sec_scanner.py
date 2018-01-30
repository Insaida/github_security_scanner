#!/usr/bin/env python

import doctest
import sys
import os


import octohub
from octohub.connection import Connection

token = os.environ.get("GITHUB_ACCESS_TOKEN")
c = Connection(token)
team_id = []
team_mates = []


def mfa_checker():
    """
    checks for users with 2FA not enabled.abs
    By querying the org members endpoint
    GET '/orgs/:org/member'
    using the filter object: "2fa-disabled"
    """

    uri = "/orgs/" + sys.argv[1] + "/members"
    r = c.send('GET', uri, params={"filter": "2fa-disabled"})
    print "The Following users do not have 2FA NOT ENABLED"
    print ("*" * 25)
    print "   "
    for user in r.parsed:
        print user.login
        print "   "
        


def commit_sig_verification():
    uri = "/repos/insaida/core/git/commits/0fd06d9fb279b1fd2daba28accd94b8e73bf5ded"
    r = c.send('GET', uri, data="Verification")
    print r.parsed
    for verification in r.parsed:
        print verification['verification']


def list_Team():
    uri = "/orgs/" + sys.argv[1] + "/teams"
    r = c.send('GET', uri)
    print ("Existing Teams")
    for name in r.parsed:
        team_mates = name['name']
        print (team_mates)


def create_team():
    uri = "/orgs" + sys.argv[1] + "/teams"
    r = c.send('POST', uri, params={
        "name": "Quarantine",
        "description": "No MFA teammates",
        "permission": "pull",
        "repo_names": [
            ""
        ]
    })
    if response == '201':

        print ('Newly Added Team: ')
        print r.parsed
        for id in r.parsed:
            team_id = id['id']
            print team_id
    else:
        log = octohub.response.get_logger()
        list_Team()
    return True


def add_to_team():
    uri = "/teams" + team_id + "/members" + team_mates
    r = c.send('PUT', uri)
    yield r.parsed
    if response == '201':
        print ("Successfully added teammates to new team")


#def notify_security_team():

"""
Check for recently installed webhooks
"""



def main():
    mfa_checker()
    commit_sig_verification()
    list_Team()
    create_team()
    pass


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
