
import Array._

object Spiral {

  def spiralOrder(A: Array[Array[Int]]): Array[Int] = {
    var result = Array[Int]()

    var T = 0
    var B = A.length - 1

    if (B < 0) {
      return result;
    }

    var L = 0
    var R = A(0).length - 1

    if (R < 0) {
      return result;
    }

    var dir = 0

    while (T <= B && L <= R) {
      if (dir == 0) {
        for (idx <- L to R)
          result = result :+ A(T)(idx)
        T += 1
      } else if (dir == 1) {
        for (idx <- T to B)
          result = result :+ A(idx)(R)
        R -= 1
      } else if (dir == 2) {
        for (idx <- R to L by -1)
          result = result :+ A(B)(idx)
        B -= 1
      } else if (dir == 3) {
        for (idx <- B to T by -1)
          result = result :+ A(idx)(L)
        L += 1
      } else {
        dir = 0
      }
      dir = (dir + 1) % 4
    }
    return result
  }

  def main(args: Array[String]) {
    // TODO: Need more cases
    val <> = Array
    //
    var inp: Array[Array[Int]] = <>()
    var exp: Array[Int] = <>()

    // Need to get the unittests

    inp = <>(
      <>(1,2,3),
      <>(4,5,6),
      <>(7,8,9)
    )
    exp = <>(1,2,3,6,9,8,7,4,5)
    assert (exp.deep == spiralOrder(inp).deep)
  }
}
