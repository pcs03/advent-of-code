import utils.readInputToLines

fun main() {
    val input = readInputToLines("Day06", test = false)
    println(input)

    val mathProblems = input.parseMathProblems()
    println(mathProblems)

    val sum = mathProblems.sumOf { it.solve() }
    println(sum)
}

fun List<String>.parseMathProblems(): List<Pair<List<String>, MathOperation>> {
    val mathProblems = mutableListOf<Pair<List<String>, MathOperation>>()

    var currentProblemStartIndex = 0

    for (i in 1..<this[0].length) {
        val currentMathOperationCharacter = this.last()[i]
        if (currentMathOperationCharacter == '+' || currentMathOperationCharacter == '*') {
            mathProblems.add(this.extractMathProblem(currentProblemStartIndex, i - 1))
            currentProblemStartIndex = i
        }
    }

    mathProblems.add(this.extractMathProblem(currentProblemStartIndex, this[0].length))
    return mathProblems
}

fun List<String>.extractMathProblem(
    problemStartIndex: Int,
    problemEndIndexExclusive: Int
): Pair<List<String>, MathOperation> {
    val numberRows = this.subList(0, this.size - 1)
    val mathOperation = this.last()[problemStartIndex].toMathOperation()

    val numbers = numberRows.map { row ->
        row.substring(startIndex = problemStartIndex, endIndex = problemEndIndexExclusive)
    }

    return Pair(numbers, mathOperation)
}

fun Pair<List<String>, MathOperation>.solve(): Long {
    val (inputNumbers, mathOperation) = this
    val amountOfNumbers = inputNumbers[0].length

    val numbers = mutableListOf<Long>()

    for (numberIdx in 0..<amountOfNumbers) {
        val buffer = mutableListOf<Char>()
        for (inputNumber in inputNumbers) {
            val char = inputNumber[numberIdx]

            if (char.isDigit()) {
                buffer.add(char)
            }
        }

        numbers.add(buffer.joinToString("").toLong())
    }

    return when (mathOperation) {
        is MathOperation.Add -> numbers.sum()
        is MathOperation.Multiply -> numbers.reduce { acc, num -> acc * num }
    }
}