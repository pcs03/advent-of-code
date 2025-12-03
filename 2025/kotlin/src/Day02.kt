fun main() {
    fun part1(input: List<LongRange>): Long {
        var sum = 0L
        input.forEach { range ->
            range.forEach { number ->
                if (!number.isValidId(listOf(2))) {
                    sum += number
                }
            }
        }

        return sum
    }

    fun part2(input: List<LongRange>): Long {
        var sum = 0L
        input.forEach { range ->
            range.forEach { number ->
                val factors = getFactors(number.length())
                if (!number.isValidId(factors)) {
                    sum += number
                }
            }
        }

        return sum
    }


    val testInput = readInput("Day02_test").parseInput()
    val input = readInput("Day02").parseInput()

//    println(part1(testInput))
//    println(part1(input))
//
//    println(part2(testInput))
    println(part2(input))
}

fun Long.isValidId(factors: List<Int>): Boolean {
    val length = this.length()

    val splitNumberSets = factors.map { factor ->
        if (length % factor != 0) return@map emptySet<Int>()

        val splitNumbers = mutableSetOf<Long>()

        val indexStep = length / factor

        for (i in 0..<length step indexStep) {
            splitNumbers.add(this.subDigits(i, i + indexStep))
        }
        splitNumbers
    }

    return !splitNumberSets.any { it.size == 1 }
}

fun getFactors(numberLength: Int): List<Int> {
    val factors = (2..numberLength).filter { numberLength % it == 0 }
    return factors
}

fun Long.subDigits(start: Int, end: Int): Long {
    require(start in 0..end) { "Invalid indices" }

    val length = this.length()

    if (start >= length) return 0L
    val actualEnd = minOf(end, length)

    val numberToActualEnd = this / pow10(length - actualEnd)
    return numberToActualEnd % pow10(actualEnd - start)
}

fun String.parseInput(): List<LongRange> {
    return this.split(",").map { stringRange ->
        val numbers = stringRange.trim().split("-").map { text ->
            text.trim().toLong()
        }
        LongRange(
            start = numbers[0],
            endInclusive = numbers[1]
        )
    }
}