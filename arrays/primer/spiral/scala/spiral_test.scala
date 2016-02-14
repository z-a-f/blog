
package spiral

import Array._

// import spiral._

object Main extends App {
  // TODO: Need more cases
  val <> = Array
  val sp = new Spiral

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
  assert (exp.deep == sp.spiralOrder(inp).deep)
}
