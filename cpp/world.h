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

    public:
        World();

        std::vector<position> getPossiblePlacements(Tile *tile);
        int insertTileAt(Tile *tile);
        std::vector<position> getAdjacentPositionsAt(position *position);
};

#endif /* WORLD_H */