import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type = str, required = True)
args = parser.parse_args()

line = 0
read = 2

file = open(args.file, "rb")
rawContent = file.read()
strContent = str(rawContent)

for c in range(0, int(len(strContent)/16)):
    text = "{:#08x}".format(line) + " | "
    text += " ".join("{:02x}".format(ord(x)) \
        for x in strContent[read:read+16])
    text += " | " + strContent[read:read+32]
    line += 16
    read += 16

    print(text)
