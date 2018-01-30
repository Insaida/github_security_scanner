# gisecscan

In trying to make sure that our GitHub organization is safe and follows certain rules we use this script to automate our routine checks. gisecscan will check for best practices and alert the in-house security team when something is not as it should be. 

# Features
Check GitHub for best practices:

[+] 2FA enabled for all users (for arbitrary reasons it can't enforced)

[+] Check for signed commits check on missing or invalid commit signatures https://developer.github.com/v3/git/commits/

[+] Users that don't comply are moved into an isolated GitHub team with least privelges and with no access to any repository. 

Once non-compliance is noticed, an alert is sent to the security team.

# Dependencies

``` code
    octohub
```


# How To Use

1. Clone the Repository,

```bash
$ git clone https:github.com/insaida/github_security_scanner.git
```

2. 
``` bash
$ cd github_security_scanner
``` 

3. 
Get your Github Token from you dashboard, and then export it to enviromental variables.

```bash

$ export GITHUB_ACCESS_TOKEN="your-personal-github-access-token"

```
4. run the python script, with the name of the github organization you are scanning. For example,

``` bash
$ python github_security_scanner.py github-org-name
```

# Features Extensions

Installed webhooks (repo/organizations): Are new webhooks present since the last run?

Teams + Members: Have they been changed since the last run?

# Issues.

Please report issues for quick triaging

