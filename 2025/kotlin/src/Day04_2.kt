import utils.readInputToGrid

fun main() {
    val grid = readInputToGrid("Day04", test = false)
    println(grid)

    var totalRollsRemoved = 0


    while (true) {
        var rollsRemovedOnIteration = 0

        for (r in 0..<grid.rows) {
            for (c in 0..<grid.cols) {
                val charAtIndex = grid.getCharacter(r, c)
                if (charAtIndex == null || charAtIndex == '.') {
                    continue
                }

                val adjacentChars = grid.getAdjacentChars(r, c)
                val occupiedGridSpaces = adjacentChars.count { it == '@' }
                if (occupiedGridSpaces < 4) {
                    grid.setIndex(r, c, '.')
                    rollsRemovedOnIteration += 1
                }
            }
        }

        if (rollsRemovedOnIteration == 0) {
            break
        }
        totalRollsRemoved += rollsRemovedOnIteration
    }

    println(totalRollsRemoved)

}