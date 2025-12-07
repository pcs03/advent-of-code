
sealed interface MathOperation {
    data object Add : MathOperation
    data object Multiply : MathOperation
}

fun Char.toMathOperation(): MathOperation {
    return when(this) {
        '+' -> MathOperation.Add
        '*' -> MathOperation.Multiply
        else -> throw IllegalArgumentException("Character '$this' is not a valid math operation.")
    }
}

sealed interface NumberDirection {
    data object Right : NumberDirection
    data object Left : NumberDirection
}