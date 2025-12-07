package utils

fun String.splitOnWhitespace(): List<String> {
    return this.split("\\s+".toRegex())
}