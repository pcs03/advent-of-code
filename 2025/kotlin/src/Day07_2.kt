import utils.AocGrid
import utils.readInputToGrid

fun main() {
    val grid = readInputToGrid("Day07", test = false)

    val start = grid.findCharacterIndices('S')[0]

    println(grid)
    println(start)

    val activeTimelines = grid.dfs(start)

    println(activeTimelines)
}

val dfsCache = mutableMapOf<Pair<Int, Int>, Long>()

fun AocGrid.dfs(index: Pair<Int, Int>): Long {
    println(index)
    val character = this.getCharacter(index)
    val characterBelow = this.getCharacter(Pair(index.first + 1, index.second))

    if (character == '.' && characterBelow == null) return 1

    val edges = when(character) {
        '.', 'S' -> { listOf(Pair(index.first + 1, index.second)) }
        '^' -> {
            listOf(Pair(index.first, index.second - 1), Pair(index.first, index.second + 1))
        }
        else -> throw IllegalArgumentException("Character '$character' does not have valid edges.")
    }

    var sum = 0L
    edges.forEach { edge ->
        val characterAtEdge = this.getCharacter(edge)
        if (characterAtEdge != null) {
            val cachedDfsResult = dfsCache[edge]

            if (cachedDfsResult != null) {
                sum += cachedDfsResult
            } else {
                val dfsResult = this.dfs(edge)
                dfsCache[edge] = dfsResult
                sum += dfsResult
            }
        }
    }

    return sum
}