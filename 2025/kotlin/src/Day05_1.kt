import utils.readInputToGrid
import utils.readInputToString

fun main() {
    val input = readInputToString("Day05", test = false).split("\n\n").map { section ->
        section.lines()
    }

    val freshIngredientRanges = input[0].map { rangeText ->
        val numbers = rangeText.split("-").map { it.trim().toLong() }
        LongRange(start = numbers[0], endInclusive = numbers[1])
    }
    val availableIngredients = input[1].map { it.trim().toLong() }.toSet()

    val freshAvailableIngredients = mutableSetOf<Long>()

    availableIngredients.forEach { ingredient ->
        freshIngredientRanges.forEach { range ->
            if (ingredient in range) {
                freshAvailableIngredients.add(ingredient)
            }
        }
    }

    println(freshAvailableIngredients)
    println(freshAvailableIngredients.size)
}