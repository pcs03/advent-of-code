import utils.readInputToLines
import java.util.*

fun main() {
    val machines = readInputToLines("Day10", test = false).map { line ->
        line.inputToMachine()
    }

    val result = machines.sumOf { machine ->
        machine.getMinimumButtonPressesWithJoltage()
    }

    println("Result: $result")

}

fun Machine.getMinimumButtonPressesWithJoltage(): Int {
    val initialMachineState = MachineState(
        lights = List(this.lights.size) { false },
        joltages = List(this.joltages.size) { 0 },
        parent = null,
        buttonPressAmount = 0
    )

    val pq = PriorityQueue<MachineState>(compareBy { it.buttonPressAmount })
    val buttonPressAmounts = mutableMapOf(initialMachineState.joltages to 0)

    pq.add(initialMachineState)

    while (pq.isNotEmpty()) {
        val machineState = pq.poll()

        if (machineState.joltages.areJoltagesAtRequiredLevels(this.joltages)) {
            return machineState.buttonPressAmount
        }

        for (button in this.buttons) {
            val newLightSequence = machineState.lights.getNewLightSequence(button)
            val newJoltageLevels = machineState.joltages.getNewJoltageLevels(button)
            val newButtonPressAmount = machineState.buttonPressAmount + 1
            val currentButtonPressAmount = buttonPressAmounts[newJoltageLevels]

            if (!newJoltageLevels.areJoltagesWithinLimits(this.joltages)) continue

            if (currentButtonPressAmount == null || newButtonPressAmount < currentButtonPressAmount) {
                buttonPressAmounts[newJoltageLevels] = newButtonPressAmount
                pq.add(
                    MachineState(
                        lights = newLightSequence,
                        joltages = newJoltageLevels,
                        parent = machineState,
                        buttonPressAmount = newButtonPressAmount
                    )
                )
            }
        }
    }

    throw RuntimeException("No solution found for $this")
}

fun List<Boolean>.getNewLightSequence(button: Set<Int>): List<Boolean> {
    return this.mapIndexed { idx, light ->
        if (idx in button) {
            !light
        } else {
            light
        }
    }
}

fun List<Int>.getNewJoltageLevels(button: Set<Int>): List<Int> {
    return this.mapIndexed { idx, joltage ->
        if (idx in button) {
            joltage + 1
        } else {
            joltage
        }
    }
}

fun List<Int>.areJoltagesWithinLimits(requiredLevels: List<Int>): Boolean {
    for (i in 0..<this.size) {
        if (this[i] > requiredLevels[i] ) {
            return false
        }
    }

    return true
}
fun List<Int>.areJoltagesAtRequiredLevels(requiredLevels: List<Int>): Boolean {
    for (i in 0..<this.size) {
        if (this[i] != requiredLevels[i] ) {
            return false
        }
    }

    return true
}
