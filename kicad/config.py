
class footprint():
    '''Footprint configuration'''

    # Footprint
    EXTENSION = '.kicad_mod'
    #FOOTPRINT_PRECISION = 3

    #REFERENCE_LAYER = 'F.SilkS'
    REFERENCE_FONT_SIZE = 1.0
    REFERENCE_FONT_THICKNESS = 0.15

    #VALUE_LAYER = 'F.Fab'
    VALUE_FONT_SIZE = 1.0
    VALUE_FONT_THICKNESS = 0.15

    #PACKAGE_LAYER = 'F.SilkS'
    #PACKAGE_LINE_WIDTH = 0.15
    PACKAGE_LINE_WIDTH = 0.3

    # Scale line with and font size depending on device area
    SMALL_DEVICE = 5.0
    MEDIUM_DEVICE = 20.0
    BIG_DEVICE = 100.0

    SMD_LAYERS = 'F.Cu F.Paste F.Mask'
    THD_LAYERS = '*.Cu *.Mask F.SilkS'

    # http://www.leiton.de/technologie-starre-leiterplatten.html
    # http://www.multi-circuit-boards.eu/leiterplatten-design-hilfe/design-parameter/restring.html
    DRILL = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
    ANNULAR_RING = 0.15

"""Configuration parsing module, which generate a python namespace"""
'''
__all__ = ("Config")

from collections import Mapping, Sequence

class Config(object):
    """A dict subclass that exposes its items as attributes.

    Warning: Namespace instances do not have direct access to the
    dict methods.

    """

    def __init__(self, configFile):
        for line in open(configFile,"r"):
            parts = line.rstrip().split("=",1)
            if len(parts) > 1:
                # Strip enclosing double quotes
                if parts[1].startswith('"') and parts[1].endswith('"'):
                    parts[1] = parts[1][1:-1]

                try:
                    numVal = float(parts[1])
                    setattr(self,parts[0],numVal)
                except:
                    setattr(self,parts[0],parts[1])

    __hash__ = None

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return not (self == other)

    def __contains__(self, key):
        return key in self.__dict__

    def dict(self):
        return self.__dict__
'''
