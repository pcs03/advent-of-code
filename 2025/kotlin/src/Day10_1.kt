import utils.readInputToLines
import utils.splitOnWhitespace
import java.util.PriorityQueue

fun main() {
    val machines = readInputToLines("Day10", test = false).map { line ->
        line.inputToMachine()
    }

    val result = machines.sumOf { machine ->
        machine.getMinimumButtonPresses()
    }

    println("Result: $result")

}

fun Machine.getMinimumButtonPresses(): Int {
    val initialMachineState = MachineState(
        lights = List(this.lights.size) { false },
        joltages = List(this.joltages.size) { 0 },
        parent = null,
        buttonPressAmount = 0
    )

    val pq = PriorityQueue<MachineState>(compareBy { it.buttonPressAmount })
    val buttonPressAmounts = mutableMapOf(initialMachineState.lights to 0)

    pq.add(initialMachineState)

    while (pq.isNotEmpty()) {
        val machineState = pq.poll()

        if (machineState.lights == this.lights) {
            return machineState.buttonPressAmount
        }

        for (button in this.buttons) {
            val newLightSequence = machineState.lights.pressButton(button)
            val buttonPressAmountForLightSequence = machineState.buttonPressAmount + 1
            val currentButtonPressesForLightSequence = buttonPressAmounts[newLightSequence]

            if (currentButtonPressesForLightSequence == null || buttonPressAmountForLightSequence < currentButtonPressesForLightSequence) {
                buttonPressAmounts[newLightSequence] = buttonPressAmountForLightSequence
                pq.add(
                    MachineState(
                        lights = newLightSequence,
                        joltages = machineState.joltages,
                        parent = machineState,
                        buttonPressAmount = buttonPressAmountForLightSequence
                    )
                )
            }
        }
    }
    return -1
}

fun List<Boolean>.pressButton(button: Set<Int>): List<Boolean> {
    return this.mapIndexed { idx, light ->
        if (idx in button) {
            !light
        } else {
            light
        }
    }
}


