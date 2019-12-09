# LayerGenerator

A python script which generates a pdf containing specified layers from an inkscape svg file.

Requires inkscape. Tested with Python 3 on Ubuntu 18.04.

## Usage

    usage: LayerGenerator.py [-h] -i INPUT [-o OUTPUT] [-l]
                             [-k KEEPLAYERS [KEEPLAYERS ...]]

    Generate a pdf using certian layers of an inkscape pdf

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            The input (svg) filename
      -o OUTPUT, --output OUTPUT
                            The output (pdf) filename
      -l, --layers          Print a list of layers in the input file
      -k KEEPLAYERS [KEEPLAYERS ...], --keepLayers KEEPLAYERS [KEEPLAYERS ...]
                            Layers to include in output
