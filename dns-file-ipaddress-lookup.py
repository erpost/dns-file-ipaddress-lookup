import requests as rq
import time
import csv

# get input file (use: dns-test-file.txt for testing)
infile = input('Input filename: ')
if len(infile) < 1:
    print('\nNo file supplied!')
    exit()

dict = {}
# open input file and parse into dictionary
with open(infile) as f:
    for line in f.readlines():
        line = line.rstrip()
        if not line.startswith('CNAME'):
            if 'IN A' in line or 'CNAME' in line:
                splitline = line.split(' ')
                dict[splitline[0]] = splitline[-1]

# create output CSV and begin writing
outfile = infile.split('.')[0] + '.csv'
with open(outfile, 'w', newline='') as outfile:
    out_file = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    out_file.writerow(['Domain Name'] + ['Status'] + ['IP or CNAME'] + ['Organization Name'] + ['ISP'] +
                      ['AS Number'] + ['City'] + ['State'] + ['Country'] + ['Zip Code'])

    url = 'http://ip-api.com/json/'
    # pull API and decode
    for key, value in dict.items():
        resp = rq.get(url + value)
        js = resp.json()
        print(resp.json())

        # parse JSON into output CSV
        if js['status'] == 'success':
            out_file.writerow([key] + [js['status']] + [value] + [js['org']] + [js['isp']] + [js['as']] +
                              [js['city']] + [js['regionName']] + [js['country']] + [js['zip']])
        else:
            out_file.writerow([key] + [js['status']] + [value])

        time.sleep(1)

outfile.close()
