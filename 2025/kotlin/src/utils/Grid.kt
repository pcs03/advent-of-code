package utils

class AocGrid(
    private val grid: List<MutableList<Char>>
) {
    val rows = grid.size
    val cols = grid[0].size

    override fun toString(): String {
        return grid.joinToString("\n") { row ->
            row.joinToString("")
        }
    }

    /**
     * Returns the character in the grid at the given index. Returns null if index does not exist.
     */
    fun index(row: Int, col: Int): Char? {
        return try {
            grid[row][col]
        } catch (e: IndexOutOfBoundsException) {
            return null
        }
    }

    /**
     * Sets the character in the grid at the given index to the given char.
     */
    fun setIndex(row: Int, col: Int, char: Char) {
        val charAtIndex = index(row, col)

        when(charAtIndex) {
            null, char -> return
            else -> {
                grid[row][col] = char
            }
        }
    }

    fun getAdjacentChars(row: Int, col: Int): List<Char> {
        val chars = mutableListOf<Char>()

        for (i in row - 1..row + 1) {
            for (j in col - 1..col + 1) {
                if (i == row && j == col) {
                    continue
                }
                index(i, j)?.let { chars.add(it) }
            }
        }

        return chars
    }
}