import utils.readInputToGrid

fun main() {
    val grid = readInputToGrid("Day04", test = false)
    println(grid)

    var sum = 0
    for (r in 0..<grid.rows) {
        for (c in 0..<grid.cols) {
            val charAtIndex = grid.getCharacter(r, c)
            if (charAtIndex == null || charAtIndex == '.') {
                continue
            }

            val adjacentChars = grid.getAdjacentChars(r, c)
            val occupiedGridSpaces = adjacentChars.count { it == '@' }
            if (occupiedGridSpaces < 4) {
                sum += 1
            }
        }
    }
    println(sum)

}