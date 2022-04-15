#ifndef TILE_H
#define TILE_H

const int c_tile_size = 6;

class Tile {
    public:
        Tile();
        Tile(int seed);

        int edges [c_tile_size];
        int getIndexOfOppositeSide(int index);
        /**
        * Rotates the tile clockwise by the provided number of steps.
        */
        void rotate(int steps); 
};


#endif /* TILE_H */