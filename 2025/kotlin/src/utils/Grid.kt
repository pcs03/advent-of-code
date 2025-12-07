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
    fun getCharacter(row: Int, col: Int): Char? {
        return try {
            grid[row][col]
        } catch (e: IndexOutOfBoundsException) {
            return null
        }
    }

    /**
     * Returns the character in the grid at the index as a pair of indices of row,col. Returns null if index does not exist.
     */
    fun getCharacter(index: Pair<Int, Int>): Char? {
        val (row, col) = index
        return getCharacter(row, col)
    }

    /**
     * Sets the character in the grid at the given index to the given char.
     */
    fun setIndex(row: Int, col: Int, char: Char) {
        val charAtIndex = getCharacter(row, col)

        when(charAtIndex) {
            null, char -> return
            else -> {
                grid[row][col] = char
            }
        }
    }

    /**
     * Returns all adjacent chars to the given grid index. Can return up to 8 characters.
     */
    fun getAdjacentChars(row: Int, col: Int): List<Char> {
        val chars = mutableListOf<Char>()

        for (i in row - 1..row + 1) {
            for (j in col - 1..col + 1) {
                if (i == row && j == col) {
                    continue
                }
                getCharacter(i, j)?.let { chars.add(it) }
            }
        }

        return chars
    }

    /**
     * Finds the indices of the given character in the grid.
     */
    fun findCharacterIndices(character: Char): List<Pair<Int, Int>> {
        val indices = mutableListOf<Pair<Int, Int>>()

        for (row in 0..<this.rows) {
            for (col in 0..<this.cols) {
                val characterAtIndex = getCharacter(row, col)
                if (characterAtIndex != null && characterAtIndex == character) {
                    indices.add(Pair(row, col))
                }
            }
        }

        return indices
    }
}