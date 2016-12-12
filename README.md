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
What does section 5 mean?

- Mesh builder
- Pathfinder
- Entity horizon searches within structure?
    - Other query shapes? Quads, spheres, frustums, etc.
- Measure distance? How do arcs work, if at all?
