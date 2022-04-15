#include <tile.h>
#include <random>
#include <iostream>

Tile::Tile() {
    // Randomly init edges
}

Tile::Tile(int seed) {
    // Randomly init edges
    std::random_device rd; // obtain a random number from hardware
    std::mt19937 gen(rd()); // seed the generator
    std::uniform_int_distribution<> distr(0, 10); // define the inclusive range

    for (int i = 0; i < 6; i++) {
        edges[i] = distr(gen);
        std::cout << edges[i];
    }
}