#include <tile.h>
#include <vector>
#include <position.h>

#ifndef WORLD_H
#define WORLD_H

class World {
    private:
        int _size;
        
        std::vector<position> _possiblePlacements;
        
        std::vector<std::vector<Tile>> _map;

        /*
            Checks if every adjacent tile of the provided position (and the tile at this position) is perfectly surrounded by tiles, i.e. every edge has matching type.
        */
        int calculateBonusTilesAt(position *position);

        /*
            Calculates the score with the adjacent tiles of the provided position and the given tile.
            Note that the given tile doesn't need to correspond with the actual tile at the provided position.
        */
        int calculateScoreForTileAt(Tile *tile, position  *position);

    public:
        World();

        Tile* getTileAt(position *position);
        std::vector<position> getPossiblePlacements(Tile *tile);
        int insertTileAt(Tile *tile);
        /*
            Returns the adjacent positios in the hexagonal grid. In clockwise order, starting with Up-Right.
        */
        std::vector<position> getAdjacentPositionsAt(position *position);
        /*
            Returns the adjacent tiles in the hexagonal grid. In clockwise order, starting with Up-Right. 
            Empty positions are filled with None.
        */
        std::vector<position> getAdjacentTilesAt(position *position);
};

#endif /* WORLD_H */