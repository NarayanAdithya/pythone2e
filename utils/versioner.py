import toml
import argparse


parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument("--major", dest="major", action='store_true', help="Major Update")
parser.add_argument("--minor", dest="minor", action='store_true', help="Minor Update")
parser.add_argument("--patch", dest="patch", action='store_true', help="Patch Update")
args = parser.parse_args()


data: dict = toml.load('version.toml')
version = data['version'].split('.')
if args.major:
    version[0] = str(int(version[0])+1)
if args.minor:
    version[1] = str(int(version[1])+1)
if args.patch:
    version[2] = str(int(version[2])+1)
data["version"] = '.'.join(version)
with open('version.toml', 'r+') as f:
    toml.dump(data, f)
