import utils.readInputToLines
import java.util.PriorityQueue
import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    val input = readInputToLines("Day08", test = false).map { line ->
        line.trim().split(",").map { num -> num.trim().toLong() }.toJunction()
    }

    val connections = mutableSetOf<Connection>()

    for (i in 0..<input.size) {
        for (j in i + 1..<input.size) {
            connections.add(Connection(input[i], input[j]))
        }
    }

    val circuits = input.associateWith { setOf(it) }.toMutableMap()

    val expectedConnectionsAmount = input.size * (input.size - 1) / 2
    assert(connections.size == expectedConnectionsAmount) { "Incorrect number of connections. Expected: $expectedConnectionsAmount, got: ${connections.size}" }

    val orderedConnections = connections.sortedBy { it.distance }

    (0..<1000).forEach {
        val connection = orderedConnections[it]

        val junction1Circuit = circuits[connection.junction1] ?: setOf(connection.junction1)
        val junction2Circuit = circuits[connection.junction2] ?: setOf(connection.junction2)

        val newCircuit = junction1Circuit + junction2Circuit

        newCircuit.forEach { junction ->
            circuits[junction] = newCircuit
        }
    }

    val distinctCircuits = circuits.map { it.value.toSet() }.toSet()
    val distinctCircuitsSizes = distinctCircuits.map { it.size }.sortedDescending()

    assert(distinctCircuitsSizes.sum() == input.size) { "The total amount of junctions in the distinct circuits must be equal to the junctions in the input. Expected size: ${input.size}, Actual size: ${distinctCircuitsSizes.sum()}" }

    assert(distinctCircuits.size >= 3) { "Need to take the first three values of circuits, but amount of circuits is ${distinctCircuits.size}" }
    println(distinctCircuitsSizes.take(3).reduce { acc, size -> acc * size })
}
