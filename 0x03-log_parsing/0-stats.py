#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer, don't print
anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value -
it's normal to not have the same output as this one.
"""
import re


def parse_line(line: str):
    """reads and parses line"""
    r = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    return_dict = {
        'status_code': 0,
        'file_size': 0,
    }
    format = '{}\\-{}{}{}{}\\s*'.format(r[0], r[1], r[2], r[3], r[4])

    matches = re.fullmatch(format, line)
    if matches is not None:
        status = matches.group('status_code')
        size = int(matches.group('file_size'))

        return_dict['status_code'] = status
        return_dict['file_size'] = size
    return return_dict


def print_data(file_size, code_stats):
    """Prints stats of the HTTP request log."""
    print('File size: {:d}'.format(file_size), flush=True)
    for status_code in sorted(code_stats.keys()):
        num = code_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_stats(line, file_size, code_stats):
    """Updates statistics"""
    line_dict = parse_line(line)
    status_code = line_dict.get('status_code', '0')
    if status_code in code_stats.keys():
        code_stats[status_code] += 1
    return file_size + line_dict['file_size']


def main():
    """script entrypoint"""
    n = 0
    file_size = 0
    code_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_size = update_stats(
                line,
                file_size,
                code_stats,
            )
            n += 1
            if n % 10 == 0:
                print_data(file_size, code_stats)
    except (KeyboardInterrupt, EOFError):
        print_data(file_size, code_stats)


if __name__ == '__main__':
    main()
