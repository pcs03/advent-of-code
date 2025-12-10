import utils.splitOnWhitespace
import java.util.PriorityQueue

data class Machine(
    val lights: List<Boolean>,
    val buttons: List<Set<Int>>,
    val joltages: List<Int>,
)

fun String.inputToMachine(): Machine {
    val lightSequenceEndIndex = this.indexOf(']') + 1
    val joltageSequenceStartIndex = this.indexOf('{')

    val lights = this.substring(startIndex = 0, endIndex = lightSequenceEndIndex)
        .trim()
        .filterNot { it == '[' || it == ']' }
        .map {
            when (it) {
                '.' -> false
                '#' -> true
                else -> throw IllegalArgumentException("Character $it is not a valid character for light sequence.")
            }
        }
    val buttons = this.substring(lightSequenceEndIndex, joltageSequenceStartIndex)
        .trim()
        .splitOnWhitespace()
        .map { button ->
            button.filterNot { it == '(' || it == ')' }.split(',').map { it.trim().toInt() }.toSet()
        }

    val joltages = this.substring(joltageSequenceStartIndex, this.length)
        .trim()
        .filterNot { it == '{' || it == '}' }
        .split(',')
        .map { it.trim().toInt() }

    return Machine(
        lights,
        buttons,
        joltages
    )
}

data class MachineState(
    val lights: List<Boolean>,
    val joltages: List<Int>,
    val parent: MachineState?,
    val buttonPressAmount: Int,
)
