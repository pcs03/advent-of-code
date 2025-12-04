import utils.readInputToLines

// const val MAX_BUFFER_SIZE = 2 // Part 1
const val MAX_BUFFER_SIZE = 12 // Part 2

fun main() {
    val banks = readInputToLines("Day03", test = false).map { line ->
        line.toList().map { it.digitToInt() }
    }

    var sum = 0L
    banks.forEach { bank ->
        sum += getMaxJoltage(bank)
    }

    println(sum)
}

fun getMaxJoltage(bank: List<Int>): Long {
    var buffer: List<Int> = List(MAX_BUFFER_SIZE) { 0 }
    for (bankIndex in 0..bank.size - MAX_BUFFER_SIZE) {
        for (bufferIndex in 0..<MAX_BUFFER_SIZE) {
            if (bank[bankIndex + bufferIndex] > buffer[bufferIndex]) {
                buffer = buffer.subList(0, bufferIndex) + bank.subList(bankIndex + bufferIndex, bankIndex + MAX_BUFFER_SIZE)
                break
            }
        }
    }

    return buffer.joinToString("").toLong()
}