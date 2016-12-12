# This code was adapted by Robert Sirois from:
'''
Lee, Michael and Samet, Hanan. (April 2000). Navigating through Triangle Meshes Implemented as Linear Quadtrees.
    ACM Transactions on Graphics, Vol. 19, No. 2.
    Retrieved from
    https://pdfs.semanticscholar.org/a5c8/8b53174405e5ff512ff5ffa8a56df3c8e2df.pdf
'''


class IcosIndexer:
    def __init__( self ):
        # neighbor direction
        # left = 0, right = 1, vert = 2
        self.STOPTAB = {
            '00': [ False, False, True  ],
            '01': [ False, True,  False ],
            '10': [ True,  True,  True  ],
            '11': [ True,  False, False ]
        }

        '''
               /\\        \\--------------/
              /  \\        \\ 01  /\\ 11 /
             / 00 \\        \\   /  \\  /
            /------\\        \\ / 10 \\/
           /\\ 10 / \\        \\------/
          /  \\  /   \\        \\ 00 /
         / 01 \\/ 11  \\        \\  /
        /--------------\\        \\/
        '''

        # neighbor type
        # left = 0, right = 1, vert = 2
        self.NEXTTAB = {
            '00': [ '11', '01', '10' ],
            '01': [ '00', '10', '01' ],
            '10': [ '01', '11', '00' ],
            '11': [ '10', '00', '11' ]
        }

        '''
          /\\    /\\    /\\    /\\    /\\
         /  \\  /  \\  /  \\  /  \\  /  \\
        / 00 \\/ 01 \\/ 02 \\/ 03 \\/ 04 \\
        -----------------------------------
        \\ 05 /\\ 06 /\\ 07 /\\ 08 /\\ 09 /\\
         \\  /  \\  /  \\  /  \\  /  \\  /  \\
          \\/ 10 \\/ 11 \\/ 12 \\/ 13 \\/ 14 \\
           ------------------------------------
            \\ 15 /\\ 16 /\\ 17 /\\ 18 /\\ 19 /
             \\  /  \\  /  \\  /  \\  /  \\  /
              \\/    \\/    \\/    \\/    \\/
        '''

        # top level neighbor
        # left = 0, right = 1, vert = 2
        self.NEXTTOP = {
            '00': [ '04', '01', '05' ],
            '01': [ '00', '02', '06' ],
            '02': [ '01', '03', '07' ],
            '03': [ '02', '04', '08' ],
            '04': [ '03', '00', '09' ],
            '05': [ '14', '10', '00' ],
            '06': [ '10', '11', '01' ],
            '07': [ '11', '12', '02' ],
            '08': [ '12', '13', '03' ],
            '09': [ '13', '14', '04' ],
            '10': [ '05', '06', '15' ],
            '11': [ '06', '07', '16' ],
            '12': [ '07', '08', '17' ],
            '13': [ '08', '09', '18' ],
            '14': [ '09', '05', '19' ],
            '15': [ '19', '16', '10' ],
            '16': [ '15', '17', '11' ],
            '17': [ '16', '18', '12' ],
            '18': [ '17', '19', '13' ],
            '19': [ '18', '15', '14' ]
        }

        # top level reflection
        # special case for nodes 0-4 and 15-19
        # left = 0, right = 1, vert = 2
        self.REFLTOP = {
            '00': [ '00', '00', '10' ],
            '01': [ '11', None, '01' ],
            '10': [ None, None, '00' ],
            '11': [ None, '01', '11' ]
        }


    # Helper Functions
    def getDepth( self ): return len( self.initialCode ) - 1

    def parseCode( self, p ): return [ i + j for i, j in zip( p[::2], p[1::2] ) ]

    def setCode( self, newCode ):
        self.initialCode = self.parseCode( newCode )
        self.code = self.initialCode


    # Algorithm 1
    # get nearest common ancestor (nca)
    def step_one( self, direction, initDepth ):
        ncaChildType = self.code[ initDepth ]
        ncaDepth = initDepth

        while ncaDepth > 0 and not self.STOPTAB[ ncaChildType ][ direction ]:
            ncaDepth = ncaDepth - 1
            ncaChildType = self.code[ ncaDepth ]

        return ( ncaChildType, ncaDepth )


    # Algorithm 2
    # set path and to child in nca and its type
    def step_two( self, direction, childType, depth ):
        if depth > 0:
            self.code[ depth ] = self.NEXTTAB[ childType ][ direction ]
        else:
            self.code[ 0 ] = self.NEXTTOP[ childType ][ direction ]


    # Algorithm 3
    # path from step 2 to neighbor
    def step_three( self, direction, depth, ncaChildType, ncaDepth ):
        tab = self.NEXTTAB if ncaDepth > 0 or ( 4 < int(ncaChildType) and int(ncaChildType) < 15 ) else self.REFLTOP

        while ncaDepth < depth:
            ncaDepth = ncaDepth + 1
            ncaChildType = self.code[ ncaDepth ]
            self.code[ ncaDepth ] = tab[ ncaChildType ][ direction ]


    # Algorithm 4
    # find the actual neighbor
    def find_neighbor( self, direction ):
        depth = self.getDepth()

        ncaChildTypeAndDepth = self.step_one( direction, depth )
        self.step_two( direction, *ncaChildTypeAndDepth )
        self.step_three( direction, depth, *ncaChildTypeAndDepth )
        return ''.join( self.code )
