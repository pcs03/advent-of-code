import utils.readInputToGrid

fun main() {
    val grid = readInputToGrid("Day07", test = false)

    val start = grid.findCharacterIndices('S')[0]

    println(grid)
    println(start)

    var splits = 0

    val explored = mutableSetOf(start)
    val queue = mutableListOf(start)

    while(queue.isNotEmpty()) {
        val pos = queue.removeFirst()
        val character = grid.getCharacter(pos) ?: continue

        val edges = when(character) {
            '.', 'S' -> { listOf(Pair(pos.first + 1, pos.second)) }
            '^' -> {
                splits += 1
                listOf(Pair(pos.first, pos.second - 1), Pair(pos.first, pos.second + 1))
            }
            else -> throw IllegalArgumentException("Character '$character' does not have valid edges.")
        }

        edges.forEach { edge ->
            if (edge !in explored) {
                explored.add(edge)
                queue.add(edge)
            }
        }
    }

    println(splits)
}
