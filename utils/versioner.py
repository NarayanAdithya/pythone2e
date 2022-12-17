import toml
import argparse


parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument("--main", dest="main", action='store_true', help="Major Update")
parser.add_argument("--stage", dest="stage", action='store_true', help="Minor Update")
parser.add_argument("--dev", dest="dev", action='store_true', help="Patch Update")
args = parser.parse_args()


data: dict = toml.load('version.toml')
version = data['version'].split('.')
if args.main:
    version[0] = str(int(version[0])+1)
if args.stage:
    version[1] = str(int(version[1])+1)
if args.dev:
    version[2] = str(int(version[2])+1)
data["version"] = '.'.join(version)
with open('version.toml', 'r+') as f:
    toml.dump(data, f)