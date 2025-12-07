import utils.readInputToLines
import utils.splitOnWhitespace
import utils.transpose
import java.util.Collections.max

fun main() {
    val input = readInputToLines("Day06", test = true)

    var sum = 0L

    val amountOfNumbers = input.size - 1
    var operationRowIndex = input.lastIndex
    var problemStartIndex = 0
    var currentOperation = input[operationRowIndex][problemStartIndex]

    val mathProblems = mutableListOf<Pair<List<String>, MathOperation>>()

    for (i in 1..<input[0].length) {
        val mathOperationCharacter = input[operationRowIndex][i]
        when(mathOperationCharacter) {
            '*', '+' -> {
                val numbers = (0..<amountOfNumbers).map { numberIdx ->
                    input[numberIdx].substring(problemStartIndex, i - 1)
                }

                mathProblems.add(Pair(numbers, mathOperationCharacter.toMathOperation()))
            }
            else -> continue
        }
    }

//    input.forEach { (numbers, operation) ->
//        val result = when (operation) {
//            is MathOperation.Add -> {
//                numbers.sum()
//            }
//
//            is MathOperation.Multiply -> {
//                numbers.reduce(Long::times)
//            }
//        }
//
//        sum += result
//    }

    println(sum)

}

//private fun List<String>.parseMathProblem(numberDirection: NumberDirection): Pair<List<Long>, MathOperation> {
//    println("$this, $numberDirection")
//    val mathOperation = when (this.last()) {
//        "+" -> MathOperation.Add
//        "*" -> MathOperation.Multiply
//        else -> throw IllegalArgumentException("Last value in list '${this.last()}' is not a valid math operation.")
//    }
//
//    val numbers = when(numberDirection) {
//        is NumberDirection.Left -> this.subList(0, this.size - 1).parseMathProblemNumbersFromLeft()
//        is NumberDirection.Right -> this.subList(0, this.size - 1).parseMathProblemNumbersFromRight()
//    }
//
//    return Pair(numbers, mathOperation)
//}
