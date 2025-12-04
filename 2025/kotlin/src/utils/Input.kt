package utils

import kotlin.io.path.Path
import kotlin.io.path.readText

/**
 * Reads from the given input txt file to lines.
 */
fun readInputToLines(name: String, test: Boolean = false): List<String> {
    return readInput(name, test).trim().lines()
}

/**
 * Reads from the given input txt file to a String.
 */
fun readInputToString(name: String, test: Boolean = false): String {
    return readInput(name, test).trim()
}

/**
 * Reads from the given input txt file to a grid.
 */
fun readInputToGrid(name: String, test: Boolean = false): AocGrid {
    val grid = readInput(name, test).trim().lines().map { line ->
        line.toMutableList()
    }
    return AocGrid(grid)
}

private fun readInput(name: String, test: Boolean): String {
    return Path("src/$name${if (test) "_test" else ""}.txt").readText()
}