# Performs Lookup on [CNAME-formatted](https://en.wikipedia.org/wiki/CNAME_record) file and Outputs a CSV File #

Sample input:

NAME                    TYPE    VALUE

bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23


Sample output:

|Domain Name|Status|IP or CNAME|Organization Name|ISP|AS Number|City|State|Country|Zip Code|
|-----------|------|-----------|-----------------|---|---------|----|-----|-------|--------|
|www.gmail.com.|success|172.217.7.133|Google|Google|AS15169 Google LLC|McDonough|Georgia|United States|30253|
|www.yahoo.com.|success|fo-ds-ats.member.g02.yahoodns.net.|Yahoo|Inktomi Corporation|AS36647 Yahoo|Sunnyvale|California|United States|	
|mail.google.com.|fail|smail.google.com|						
|mail.yahoo.com|success|2001:4998:58:2201::50|Yahoo!|Yahoo!|AS26101 Yahoo!|Sunnyvale|California|United States|
