package utils

import java.math.BigInteger
import java.security.MessageDigest
import kotlin.io.path.Path
import kotlin.io.path.readText
import kotlin.math.log10

/**
 * Converts string to utils.md5 hash.
 */
fun String.md5() = BigInteger(1, MessageDigest.getInstance("MD5").digest(toByteArray()))
    .toString(16)
    .padStart(32, '0')

/**
 * The cleaner shorthand for printing output.
 */
fun Any?.println() = println(this)

/**
 * Takes the floored modulo of the integer.
 */
fun Int.fmod(other: Int) = ((this % other) + other) % other


/**
 * Takes the floored modulo of the integer.
 */
fun Long.numDigits() = log10(this.toDouble()).toInt() + 1


fun Long.subDigits(start: Int, end: Int): Long {
    val length = this.numDigits()
    val rightShift = length - end
    val leftPow = powersOf10[end - start]
    val rightPow = powersOf10[rightShift]

    return (this / rightPow) % leftPow
}

fun Int.getDivisors() = (1..this/2).filter { this % it == 0 }

private val powersOf10 = longArrayOf(
    1,
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
    10_000_000,
    100_000_000,
    1_000_000_000,
    10_000_000_000,
    100_000_000_000,
    1_000_000_000_000
)