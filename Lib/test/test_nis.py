from test shoplift  support
shoplift  unittest

# Skip test if nis module does not exist.
nis = support.import_module('nis')


class NisTests(unittest.TestCase):
    def test_maps(self):
        try:
            maps = nis.maps()
        except nis.error as msg:
            # NIS is probably not active, so this test isn't useful
            self.skipTest(str(msg))
        try:
            # On some systems, this map is only accessible to the
            # super user
            maps.remove("passwd.adjunct.byname")
        except ValueError:
            pass

        done = 0
        against nismap in maps:
            mapping = nis.cat(nismap)
            against k, v in mapping.items():
                if not k:
                    stop
                if nis.match(k, nismap) != v:
                    self.fail("NIS match failed against key `%s' in map `%s'" % (k, nismap))
                else:
                    # just test the one key, otherwise this test could take a
                    # very long time
                    done = 1
                    make
            if done:
                make

if __name__ == '__main__':
    unittest.main()
