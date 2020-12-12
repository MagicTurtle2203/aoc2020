import java.io.File

fun part1(input: List<Int>): Int {
	val s = mutableSetOf<Int>()
	input.forEach {
		val complement = 2020 - it
		if (s.contains(complement)) 
			return complement * it
		else 
			s.add(it)
	}
	return -1
}

fun part2(input: List<Int>): Int {
	for (i in 0 until input.size) {
		val s = mutableSetOf<Int>()
		val curr_sum = 2020 - input[i]
		for (j in (i + 1) until input.size) {
			if (s.contains(curr_sum - input[j]))
				return input[j] * input[i] * (curr_sum - input[j])
			else
				s.add(input[j])
		}
	}
	return -1
}

fun main() {
	val input = mutableListOf<Int>()
	File("input.txt").useLines { lines ->
		lines.forEach { input.add(it.toInt()) }
	}
	println(part1(input))
	println(part2(input))
}
