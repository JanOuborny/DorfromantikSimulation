#include <world.h>
#include <position.h>

World::World() {
    _size = 100;

    _map = 
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