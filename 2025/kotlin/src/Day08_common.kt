import utils.readInputToLines
import java.util.PriorityQueue
import kotlin.math.pow
import kotlin.math.sqrt

data class Junction(
    val x: Long,
    val y: Long,
    val z: Long,
)

class Connection(
    val junction1: Junction,
    val junction2: Junction,
) {
    val distance = sqrt(
        (junction1.x.toDouble() - junction2.x.toDouble()).pow(2) +
                (junction1.y.toDouble() - junction2.y.toDouble()).pow(2) +
                (junction1.z.toDouble() - junction2.z.toDouble()).pow(2)
    )

    override fun toString(): String {
        return "$junction1 to $junction2"
    }

    override fun hashCode(): Int {
        return junction1.hashCode() + junction2.hashCode()
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Connection

        if (junction1 == other.junction1 && junction2 == other.junction2) {
            return true
        }

        // Same connection, opposite order of junctions
        if (junction1 == other.junction2 && junction2 == other.junction1) {
            return true
        }

        return false
    }
}

fun List<Long>.toJunction(): Junction {
    assert(this.size == 3) { "A junction must contain 3 points." }

    return Junction(
        x = this[0],
        y = this[1],
        z = this[2]
    )
}