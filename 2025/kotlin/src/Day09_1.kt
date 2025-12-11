import utils.readInputToLines
import kotlin.math.absoluteValue

fun main() {
    val input = readInputToLines("Day09", test = false).map { line ->
        line.toCoord()
    }
    
    val rectangles = mutableSetOf<Rectangle>()
    
    var currentRectangle: Rectangle? = null
    
    for (i in 0..<input.size) {
        for (j in i + 1..<input.size) {
            val coord1 = input[i]
            val coord2 = input[j]
            val rectangle = Rectangle(coord1, coord2)
            
            if (currentRectangle == null || rectangle.surface > currentRectangle.surface) {
                currentRectangle = rectangle
            }
        }
    }
    
    println("Largest rectangle: $currentRectangle, with surface ${currentRectangle?.surface}")
}