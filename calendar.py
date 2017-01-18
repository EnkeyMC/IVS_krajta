"""
Author: Martin Omacht
Interpreter used: 3.6.0
Date: 18.1.2017
"""

import datetime
import argparse
import locale


def init_arg_parser():
    """
    Initialize new ArgumentParser object with the program arguments.

    Arguments:
    -y  show calendar for specific year (0..9999)
    -m  show calendar for specific month (1..12)

    :return: ArgumentParser instance
    """
    parser = argparse.ArgumentParser(description='Print calendar for the current or specified month and year.')
    parser.add_argument('-y', type=int, help='show calendar for specific year (1..9999)')
    parser.add_argument('-m', type=int, help='show calendar for specific month (1..12)')

    return parser


def print_calendar(year=None, month=None):
    """
    Print calendar for the current or specified month and year to standard output.
    :param year:    (optional) specify year (1..9999)
    :param month:   (optional) specify month (1..12)

    :raises ValueError, OverflowError
    """

    date = datetime.datetime.now().date()  # Get current date

    # if year is specified, change the current date to specified year
    if year is not None:
        date = date.replace(year=year)  # throws ValueError if specified year is out of range (1..9999)

    # if month is specified, change the current date to specified month
    if month is not None:
        date = date.replace(month=month)  # throws ValueError if specified month is out of range (1..12)

    date = date.replace(day=1)  # start at the first day of the month

    print('{:^28}'.format(date.strftime('%B %Y')))  # print name of the month and year

    # print weekday names
    for i in range(1, 8):
        print('{:>4s}'.format(datetime.date(1, 1, i).strftime("%a")), end="")
    print('')  # new line

    month = date.month  # store the month for further checking
    while date.month == month:  # loop until you overflow to next month
        for weekday in range(7):  # loop for one line of calendar
            if weekday < date.weekday() or date.month != month:
                # if the month does not start on monday or does not end on sunday print spaces
                print('{:4s}'.format(' '), end='')
            else:
                print('{:4d}'.format(date.day), end='')  # print day of the month
                date += datetime.timedelta(days=1)  # add 1 day
        print('')  # new line


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')  # set default locale
    parse = init_arg_parser()  # get ArgumentParser
    args = parse.parse_args()  # parse arguments (prints help if -h/--help is given from the command line and exits)

    try:
        print_calendar(year=args.y, month=args.m)
    except (ValueError, OverflowError) as err:
        print(err)
        parse.print_help()
