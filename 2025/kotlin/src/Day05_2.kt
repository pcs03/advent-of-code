import utils.readInputToString

fun main() {
    val input = readInputToString("Day05", test = false).split("\n\n").map { section ->
        section.lines()
    }

    val freshIngredientRanges = input[0].map { rangeText ->
        val numbers = rangeText.split("-").map { it.trim().toLong() }
        LongRange(start = numbers[0], endInclusive = numbers[1])
    }

    val exclusiveRanges = mutableListOf<LongRange>()

    for (range in freshIngredientRanges) {
        val newRanges = range.subtractRanges(exclusiveRanges)
        if (newRanges != null) {
            exclusiveRanges.addAll(newRanges)
        }
    }

    var sum = 0L
    exclusiveRanges.forEach {
        sum += (it.last - it.first + 1)
    }

    println(sum)
}

fun LongRange.subtractRanges(ranges: List<LongRange>): List<LongRange>? {
    val currentRanges = mutableListOf(this)

    for (range in ranges) {
        val newRanges = mutableListOf<LongRange>()
        while (currentRanges.isNotEmpty()) {
            val currentRange = currentRanges.removeFirst()
            newRanges.addAll(currentRange.subtractRange(range))
        }
        currentRanges.addAll(newRanges)
    }

    return currentRanges
}

fun LongRange.subtractRange(range: LongRange): List<LongRange> {
    if (this.first >= range.first && this.last <= range.last) {
        return emptyList()
    }
    if (this.first > range.last || this.last < range.first) {
        return listOf(this)
    }

    if (this.first < range.first && this.last > range.last) {
        return listOf(
            LongRange(this.first, range.first - 1),
            LongRange(range.last + 1, this.last),
        )
    }

    val first = when {
        this.first < range.first -> this.first
        else -> range.last + 1
    }
    val last = when {
        this.last > range.last -> this.last
        else -> range.first - 1
    }

    return listOf(
        LongRange(
            start = first,
            endInclusive = last,
        )
    )
}