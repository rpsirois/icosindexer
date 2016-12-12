import unittest

from icos_indexer import IcosIndexer

class TestIcosIndexer( unittest.TestCase ):
    def setUp( self ):
        self.indexer = IcosIndexer()

    def test_left_neighbor( self ):
        self.indexer.setCode( '101010' )
        self.assertEqual( self.indexer.find_neighbor( 0 ), '101001' )

    def test_right_neighbor( self ):
        self.indexer.setCode( '101010' )
        self.assertEqual( self.indexer.find_neighbor( 1 ), '101011' )

    def test_vert_neighbor( self ):
        self.indexer.setCode( '101010' )
        self.assertEqual( self.indexer.find_neighbor( 2 ), '101000' )

    def test_refl_top_right_edge( self ):
        self.indexer.setCode( '04001111' )
        self.assertEqual( self.indexer.find_neighbor( 1 ), '00000101' )


if __name__ == '__main__':
    unittest.main()
