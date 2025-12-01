class Dial(startingValue: Int = 50, maxRotationValue: Int = 99) {
    var value = startingValue
        private set

    private val dialPositionsAmount = maxRotationValue + 1
    private val positionsCounter = mutableMapOf<Int, Int>()
    private var zeroClickCounter = 0

    private fun incrementMapEntry(rotationValue: Int) {
        positionsCounter[rotationValue] = positionsCounter.getOrDefault(rotationValue, 0) + 1
    }

    fun printRotationPositionsCounter() {
        println("${positionsCounter.toSortedMap()}")
    }

    fun printState() {
        println("=== Dial State ==")
        println("Dial position: ${this.value}")
        println("Amount of times zero was clicked: ${this.zeroClickCounter}")
    }

    private fun rotateLeft(rotationValue: Int) {
        val rotationResult = value - rotationValue
        val newValue = rotationResult.fmod(dialPositionsAmount)

        if (newValue == 0 || newValue > value) {
            zeroClickCounter += 1
        }

        value = newValue
        incrementMapEntry(newValue)
    }

    private fun rotateRight(rotationValue: Int) {
        val newValue = (value + rotationValue) % dialPositionsAmount

        if (newValue == 0 || newValue < value) {
            zeroClickCounter += 1
        }

        value = newValue
        incrementMapEntry(newValue)
    }

    fun rotate(direction: String, rotationValue: Int) {
        when (direction) {
            "L" -> rotateLeft(rotationValue)
            "R" -> rotateRight(rotationValue)
            else -> throw IllegalArgumentException("direction must be 'L' or 'R'")
        }
    }
}

fun main() {
    fun part1(input: List<String>): Int {
        val dial = Dial()

        input.forEach { line ->
            val rotationDirection = line[0].toString()
            val rotationValue = line.substring(1).toInt()
            dial.rotate(rotationDirection, rotationValue)
        }

        dial.printRotationPositionsCounter()
        return dial.value
    }

    fun part2(input: List<String>): Int {
        val dial = Dial()

        input.forEach { line ->
            val rotationDirection = line[0].toString()
            val rotationValue = line.substring(1).toInt()
            dial.rotate(rotationDirection, rotationValue)
        }

        dial.printState()
        return dial.value
    }


    val testInput = readInput("Day01_test")
    val input = readInput("Day01")

    println(part1(testInput))
    println(part1(input))

    part2(testInput)
    part2(input)


    // Or read a large test input from the `src/Day01_test.txt` file:
//    val testInput = readInput("Day01_test")
//    check(part1(testInput) == 1)

    // Read the input from the `src/Day01.txt` file.
//    val input = readInput("Day01")
//    part1(input).println()
//    part2(input).println()
}
