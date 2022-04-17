#include <iostream>
#include <game.h>
#include <world.h>

int main() {
    std::cout << "Hello World! \n";
    Game *game = new Game;
    game->test();

    World *world = new World;

    return 0;
}