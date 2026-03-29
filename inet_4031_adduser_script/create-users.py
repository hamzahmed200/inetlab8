#!/usr/bin/python3

# INET4031
# Hamza Ahmed


# os is used to run Linux commands
# re is used for pattern matching
# sys is used to read input from stdin
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if the line starts with # (used to skip/comment out lines)
        match = re.match("^#", line)

        # Split the line into fields using ':' as delimiter
        fields = line.strip().split(':')

        # Skip the line if it’s a comment or doesn’t have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Assign values from the input line
        # gecos stores the user’s full name info for the passwd file
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group list so each group can be processed
        groups = fields[4].split(',')

        # Show which user is being created
        print("==> Creating account for %s..." % (username))

        # Build the adduser command
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # print(cmd)
        # os.system(cmd)

        # Show password is being set
        print("==> Setting the password for %s..." % (username))

        # Build command to set the user password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # print(cmd)
        # os.system(cmd)

        for group in groups:
            # If group is not '-', add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()
