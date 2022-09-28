import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('-s', help='source file')
parser.add_argument('-o', help='output file')
args = parser.parse_args()

print(args.s)
src = open(args.s, 'r', encoding='utf-8')
out = open(args.o, 'r', encoding='utf-8')

src_lines = src.readlines()
out_lines = out.readlines()

src.close()
out.close()

out_headers = list(map(lambda x: x.split('=')[0], out_lines))

for i, line in enumerate(src_lines):
    header = line.split('=')[0]
    if header not in out_headers:
        out_lines.insert(i, line)


out = open(args.o, 'w', encoding='utf-8')
out.writelines(out_lines)
out.close()
