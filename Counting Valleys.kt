/*
HackerRank - Counting Valleys
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly 'n' steps. 
For every step he took, he noted if it was an uphill, 'U', or a downhill, 'D' step. 
Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

Example:

Sample Input:
8
UDDDUDUU

Sample Output:
1

Explanation:
If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:
_/\      _
   \    /
    \/\/
He enters and leaves one valley.
 */

fun main() {

    val n = readLine()!!.trim().toInt()
    val str = readLine!!.trim()

    var level = 0
    var valleys = 0
    
    for (i in 0 until n) {
        if (str[i] == 'U') {
            level += 1
            if (level == 0)
                valleys += 1
        } else {
            level -= 1
        }
    }

    println("Number of valleys: $valleys")

}