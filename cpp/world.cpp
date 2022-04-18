#include <world.h>
#include <position.h>

World::World() {
    _size = 100;
    _map = std::vector<std::vector<Tile>>;
    _map.reserve(_size);
    for (int i = 0; i < _size; i++) {
        std::vector<Tile> *row = row_map.at(i);
        row->reserve(_size);
    }
}

// std::vector<position> World::getAdjacentPositionsAt(position position) {
//     int x = pos[0];
//     int y = pos[1];
//     int result[6] = {};
//     result[0] = result.append((x+1, y-1)) // Up Right
//     result.append((x+1, y)) // Right
//     result.append((x, y+1)) // Down Right
//     result.append((x-1, y+1)) // Down Left
//     result.append((x-1, y)) // Left
//     result.append((x, y-1)) // Up Left
// }

Tile* World::getTileAt(position *position) {
    std::vector<Tile> *row = _map.at(position.y);
    row->.at
}