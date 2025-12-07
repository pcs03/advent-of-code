import utils.readInputToLines
import utils.splitOnWhitespace
import utils.transpose

fun main() {
    val input = readInputToLines("Day06", test = false)
        .map { line -> line.trim().splitOnWhitespace() }
        .transpose()
        .map { line -> line.parseMathProblem() }

    var sum = 0L

    input.forEach { (numbers, operation) ->
        val result = when(operation) {
            is MathOperation.Add -> { numbers.sum() }
            is MathOperation.Multiply -> { numbers.reduce(Long::times) }
        }

        sum += result
    }

    println(sum)

}

private fun List<String>.parseMathProblem(): Pair<List<Long>, MathOperation> {
    val mathOperation = when (this.last()) {
        "+" -> MathOperation.Add
        "*" -> MathOperation.Multiply
        else -> throw IllegalArgumentException("Last value in list '${this.last()}' is not a valid math operation.")
    }

    val numbers = this.subList(0, this.size - 1).map { it.toLong() }

    return Pair(numbers, mathOperation)
}