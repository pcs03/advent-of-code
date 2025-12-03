import java.math.BigInteger
import java.security.MessageDigest
import kotlin.io.path.Path
import kotlin.io.path.readText
import kotlin.math.abs
import kotlin.math.log10
import kotlin.math.pow

/**
 * Reads lines from the given input txt file.
 */
fun readInputLines(name: String) = Path("src/$name.txt").readText().trim().lines()

/**
 * Reads text from the given input txt file.
 */
fun readInput(name: String) = Path("src/$name.txt").readText().trim()

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

/**
 * Takes the floored modulus of the integer.
 */
fun Int.fmod(other: Int) = ((this % other) + other) % other

/**
 * Counts the number of digits in an integer.
 */
fun Int.length() = when(this) {
    0 -> 1
    else -> log10(abs(this.toDouble())).toInt() + 1
}
/**
 * Counts the number of digits in a long.
 */
fun Long.length() = when(this) {
    0L -> 1
    else -> log10(abs(this.toDouble())).toInt() + 1
}

fun pow10(exp: Int): Long {
    return 10.0.pow(exp).toLong()
}