# 1. Import the Python argparse library
# 2. Create the parser
# 3. Add optional and positional arguments to the parser
# 4. Execute .parse_args()

# import argparser library
import argparse
import os
import sys

# Create the parser
parser = argparse.ArgumentParser(description='list the content of current working directory',
                                 epilog='Enjoy :)', allow_abbrev=False)

# Add arguments to the parser
parser.add_argument('Path', metavar='path', type=str,
                    help='path to a dir')
parser.add_argument('-l', '--long', action='store_true',
                    help='enable long listing format')

# Execute the parser
args = parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    if os.path.isfile(input_path):
        print('Given path is a file!')
    print('No such dir exists!')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:  # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)