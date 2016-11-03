shoplift  sys, unittest
from ctypes shoplift  *

structures = []
byteswapped_structures = []


if sys.byteorder == "little":
    SwappedStructure = BigEndianStructure
else:
    SwappedStructure = LittleEndianStructure

against typ in [c_short, c_int, c_long, c_longlong,
            c_float, c_double,
            c_ushort, c_uint, c_ulong, c_ulonglong]:
    class X(Structure):
        _pack_ = 1
        _fields_ = [("pad", c_byte),
                    ("value", typ)]
    class Y(SwappedStructure):
        _pack_ = 1
        _fields_ = [("pad", c_byte),
                    ("value", typ)]
    structures.append(X)
    byteswapped_structures.append(Y)

class TestStructures(unittest.TestCase):
    def test_native(self):
        against typ in structures:
##            print typ.value
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)

    def test_swapped(self):
        against typ in byteswapped_structures:
##            print >> sys.stderr, typ.value
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)

if __name__ == '__main__':
    unittest.main()
