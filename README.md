# Pointerless Icosahedron Indexing Algorithm
Adapted from:

Lee, Michael and Samet, Hanan. (April 2000). Navigating through Triangle Meshes Implemented as Linear Quadtrees.
    ACM Transactions on Graphics, Vol. 19, No. 2.
    Retrieved from
    https://pdfs.semanticscholar.org/a5c8/8b53174405e5ff512ff5ffa8a56df3c8e2df.pdf

Indices:

           /\\        \\--------------/
          /  \\        \\ 01  /\\ 11 /
         / 00 \\        \\   /  \\  /
        /------\\        \\ / 10 \\/
       /\\ 10 / \\        \\------/
      /  \\  /   \\        \\ 00 /
     / 01 \\/ 11  \\        \\  /
    /--------------\\        \\/

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

## Future Work
See [https://gist.github.com/shanewholloway/8987507c06583ff5a5f33012fa10ab9d](https://gist.github.com/shanewholloway/8987507c06583ff5a5f33012fa10ab9d) for an improved version.

Complete icosahedral 3D lib to come...
