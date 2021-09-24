#!/usr/bin/env python3
import os

headerPath = "header.html"
footerPath = "footer.html"
source = "source"
output = "output"

if not os.path.exists("."):
    os.mkdir(output)
files = os.listdir(source)

headerData = ""
with open(headerPath) as headerFile:
    for line in headerFile:
        headerData += line
footerData = ""
with open(footerPath) as footerFile:
    for line in footerFile:
        footerData += line

for inputPath in files:
    newInputPath = source + "/" + inputPath
    with open(newInputPath) as inputFile:
        outputPath = output + "/" + inputPath
        with open(outputPath, "wt") as outputFile:
            for line in inputFile:
                if '<!--NAV-->' in line:
                    outputFile.write(line.replace('<!--NAV-->', headerData))
                elif '<!--FOOTER-->' in line:
                    outputFile.write(line.replace('<!--FOOTER-->', footerData))
                else:
                    outputFile.write(line)
