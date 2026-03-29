
# INET 4031 - User Creation Script

## Overview

This script automates creating users on a Linux system using a Python script and an input file. It creates accounts, sets passwords, and assigns groups.

## Files

* `create-users.py` – original script
* `create-users2.py` – version with dry-run option
* `create-users.input` – user data

## Input Format

```
username:password:last:first:groups
```

* `:` separates fields
* `,` separates groups
* `-` means no group
* `#` skips a line

## Run

Make executable:

```
chmod +x create-users2.py
```

Dry run:

```
./create-users2.py < create-users.input
```

Enter `Y`

Real run:

```
sudo ./create-users2.py < create-users.input
```

Enter `N`

## Verify

```
grep user0 /etc/passwd
grep user0 /etc/group
```

## Notes

* Use dry run first
* Invalid lines are skipped
* Script reads input line-by-line

## Summary

Automates user creation and reduces manual work.
