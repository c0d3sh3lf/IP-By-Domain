#!/usr/bin/python

import socket, optparse, sys


def get_ip(domain_name=""):
    try:
        ip_addr = socket.gethostbyname(domain_name)
        print "[+] Processed '%s'" % (domain_name)
    except:
        ip_addr = ""
        print "[-] Error processing '%s'" % (domain_name)
    return ip_addr


def generate_csv_data(inputfile=""):
    domains = open(inputfile, "r").readlines()
    ip_addresses = {}
    for domain in domains:
        domain = domain.strip()
        ip_addresses[domain] = get_ip(domain)
    return ip_addresses


def write_to_csv(csvfile="", data={}):
    csv = open(csvfile, "w")
    csv_data = "DOMAIN,IP ADDRESS\n"
    for domain in data.keys():
        csv_data += domain + "," + str(data[domain]) +"\n"
    csv.write(csv_data)
    csv.flush()
    csv.close()


def main():
    parser = optparse.OptionParser(
        "python ip_by_domain.py -i INPUTFILE -o CSVFILE\n\r\n\rIf CSVFILE not provided, CSV filename will be same as that of INPUTFILE")
    parser.add_option("-i", "--input", dest="inputfile", help="Input File contain one domain per line")
    parser.add_option("-o", "--output", dest="csvfile", help="Output CSV filename")
    options, args = parser.parse_args()
    if not (options.inputfile):
        print "[-] XML file is required"
        parser.print_help()
        sys.exit(1)
    else:
        if not (options.csvfile):
            options.csvfile = options.inputfile.split(".")[0] + ".csv"
        else:
            if not (options.csvfile.split(".")[len(options.csvfile.split(".")) - 1] == "csv"):
                options.csvfile = options.csvfile + ".csv"
    write_to_csv(options.csvfile, generate_csv_data(options.inputfile))


if __name__ == "__main__":
    main()
