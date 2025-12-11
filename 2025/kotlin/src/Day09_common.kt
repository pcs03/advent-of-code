import kotlin.math.absoluteValue

fun String.toCoord(): Coord {
    val numbers = this.trim().split(",").map { it.trim().toLong() }
    assert(numbers.size == 2) { "Input '${this} must contain two numbers" }
    return Coord(numbers[0], numbers[1])
}

data class Coord(
    val x: Long,
    val y: Long,
)

data class Rectangle(
    val coord1: Coord,
    val coord2: Coord,
) {
    val surface = (( coord1.x - coord2.x + 1) * (coord1.y - coord2.y + 1)).absoluteValue
}