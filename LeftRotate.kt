/*
Hackerrank - Arrays: Left Rotation
Given an array 'a' of 'n' integers and a number, 'd', perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.

Sample Input:
5 4
1 2 3 4 5

Sample Output:
5 1 2 3 4
*/

fun main(args: Array<String>) {

    val nd = readLine().split(" ")

    val n = nd[0].trim().toInt()

    val d = nd[1].trim().toInt()

    val a = readLine().split(" ").map{ it.trim().toInt() }.toTypedArray()

    var arr = a.copyOf()
    val t = d%n

    for (i in 0 until t) {
        arr[n+i-t] = a[i]
    }
    for (i in t until n) {
        arr[i-t] = a[i]
    }

    println(arr.joinToString(" "))
}
