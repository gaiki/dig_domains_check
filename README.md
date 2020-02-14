# dig_domains_check

## About
Verifying the archive list of expired domains provided by nask (e.g. for SEO purposes):


http://web.archive.org/web/20170101000000*/https://www.dns.pl/deleted_domains.txt

I found that it's a good idea to automate the task.

## Script
The script allows mass checking of domain availability.
Data are loaded from a file: one domain on one line.

Then the A record is checked - if it is not set I assume that the domain does not exist. 
This is a simplification, but in very few cases when the user mixes up and e.g. removes a zone, this data is not returned.
For reasons of whois limits, on the part of nask, this is a compromise solution

I set a limit by default: one domain per second

## Python Libray

- subprocess
- re
- time
