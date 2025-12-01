import java.math.BigInteger
import java.security.MessageDigest
import kotlin.io.path.Path
import kotlin.io.path.readText

/**
 * Reads lines from the given input txt file.
 */
fun readInput(name: String) = Path("src/$name.txt").readText().trim().lines()

/**
 * Converts string to md5 hash.
 */
fun String.md5() = BigInteger(1, MessageDigest.getInstance("MD5").digest(toByteArray()))
    .toString(16)
    .padStart(32, '0')

/**
 * The cleaner shorthand for printing output.
 */
fun Any?.println() = println(this)

fun Int.quotientAndRemainder(other: Int): Pair<Int, Int> {
    return this / other to this % other
}

fun Int.flooredQuotientAndRemainder(other: Int): Pair<Int, Int> {
    val (q, r) = this.quotientAndRemainder(other)
    val (q2, r2) = (r + other).quotientAndRemainder(other)

    return q + q2 to r2
}

fun Int.fmod(other: Int) = ((this % other) + other) % other

fun getQuotientAndRemainder(dividend: Int, divisor: Int): Pair<Int, Int> {
    return dividend / divisor to dividend % divisor
}