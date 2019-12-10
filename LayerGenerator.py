#!/usr/bin/env python

#import relevant libraries
import subprocess
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Generate a pdf using certian layers of an inkscape pdf')

parser.add_argument('-i','--input', help='The input (svg) filename', required=True)
parser.add_argument('-o','--output',help='The output (pdf) filename', required=False)
parser.add_argument('-l','--layers', help='Print a list of layers in the input file', action='store_true', required=False)
parser.add_argument('-k','--keepLayers', nargs='+', help='Layers to include in output', required=False)

args = parser.parse_args()

#Open the input svg
tree  = ET.parse(args.input)
root = tree.getroot()

#check if output is set, if not generate an output filename
outfile=str(args.output).split('.', 1)[0]
if not args.output:
    outfile=str(args.input).split('.', 1)[0]+"_modified"

#If the layers argument is true, print the list of layers in the input file
if args.layers:
    for a in root:
        if 'None' not in str(a.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label')):
            print(a.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label'))
    exit()

layersList = []

#generate an error if no layers are specified
if not args.keepLayers:
    print("LayerGenerator.py: error: the following arguments are required: -k/--keepLayers")
    exit()

#Create the list of layers from the keeplayers argument
for layer in args.keepLayers:
    layersList.append(layer)

#Add the 'None' layer
layersList.append('None')

removeList = []

#Loop over all the layers and fill a list with the ones not in layerslist
for a in root:
    if str(a.attrib.get('{http://www.inkscape.org/namespaces/inkscape}label')) not in layersList:
        removeList.append(a)

#Remove the not included layers
for entry in removeList:
    root.remove(entry)

#write the output svg
tree.write(outfile+'.svg')

#convert to svg using inkscape
subprocess.call(['inkscape', outfile+'.svg', '--export-pdf='+outfile+'.pdf', '--export-ignore-filters'])
