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

    for (connection in orderedConnections) {
        val junction1Circuit = circuits[connection.junction1] ?: setOf(connection.junction1)
        val junction2Circuit = circuits[connection.junction2] ?: setOf(connection.junction2)

        val newCircuit = junction1Circuit + junction2Circuit

        newCircuit.forEach { junction ->
            circuits[junction] = newCircuit
        }

        if (newCircuit.size == input.size) {
            println(connection)
            println("Result: ${connection.junction1.x * connection.junction2.x}")
            break
        }
    }
}