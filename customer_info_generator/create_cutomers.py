#!/usr/bin/env python

import argparse
import sys
import os
import csv

from customer import Customer, get_list_order


def get_arguments():
    parser = argparse.ArgumentParser(description='create a file with random customer data')
    parser.add_argument('--customers', '-c', metavar='C', type=int, nargs=1, default=1, required=True, help='The number of customers to generate', dest='amount')
    parser.add_argument('--output', '-o', metavar='file.csv', type=str, nargs=1, default=['customers.csv'], help='The file to write to', dest='output')
    return parser.parse_args()


def main():
    args = get_arguments()

    times = args.amount[0]
    output = args.output[0]

    if not output.endswith('.csv'):
        print('Please provide a csv file')
        sys.exit()
    i = 1
    while os.path.isfile(output):
        output = output.replace('.csv', '_{0}.csv'.format(i))
        i += 1

    with open(output, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONE)
        writer.writerow(get_list_order())
        for n in range(1, times):
            customer = Customer()
            writer.writerow(customer.get_customer_as_list())


if __name__ == "__main__":
    main()

