class Dial(startingValue: Int = 50, maxRotationValue: Int = 99) {
    var value = startingValue
        private set

    private val dialPositionsAmount = maxRotationValue + 1
    private val finalPositionsCounter = mutableMapOf<Int, Int>()
    private val positionsCounter = mutableMapOf<Int, Int>()

    private fun incrementPositionsCounter() {
        positionsCounter[value] = positionsCounter.getOrDefault(value, 0) + 1
    }

    private fun incrementFinalPositionsCounter() {
        finalPositionsCounter[value] = finalPositionsCounter.getOrDefault(value, 0) + 1
    }

    fun printState() {
        println("=== Dial State ==")
        println("Total dial positions: ${this.positionsCounter.toSortedMap()}")
        println("Final dial positions: ${this.finalPositionsCounter.toSortedMap()}")
    }

    private fun rotateLeft() {
        value = (value - 1).fmod(dialPositionsAmount)
        incrementPositionsCounter()
    }

    private fun rotateRight() {
        value = (value + 1) % dialPositionsAmount
        incrementPositionsCounter()
    }


    fun rotate(direction: String, rotationValue: Int) {
        when (direction) {
            "L" -> repeat(rotationValue) { rotateLeft() }
            "R" -> repeat(rotationValue) { rotateRight() }
            else -> throw IllegalArgumentException("direction must be 'L' or 'R'")
        }
        incrementFinalPositionsCounter()
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

        dial.printState()
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


    val testInput = readInputLines("Day01_test")
    val input = readInputLines("Day01")

    println(part1(testInput))
    println(part1(input))

    part2(testInput)
    part2(input)
}
