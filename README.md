# NTLM-Brute-Forcer
Python Script to brute force HTTP NTLM Logins

Written during an engagement in which usernames and passwords were obtain from breach data and I required an automated way to test these credentials against multiple HTTP NTLM logins. 

## How to use
1. In its current form, the script requires a 'usernames.txt' and 'passwords.txt' files. These files should contain the respective usernames and passwords you wish to test. Create the files in the same location as ntlmbrute.py
2. If you know there is a domain login that needs to be included add the domain in the .py file e.g. domain = "DOMAIN\\". If there is no domain there is no requirement to modify the python script.
3. Include the URL you wish to test argument one to the script.

To Run - python ntlmbrute.py http://domain.com/directory

Feel free to modify to suit your needs (i.e brute force multple passwords against a single logon)
