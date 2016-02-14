
package tools

import scala.collection.mutable.Map

object json_tools {
  def vars2json(fName: String, args: Map[String, Any]) {
    
  }

  def main (args: Array[String]) {
    var A: Map[String, Any] = Map()
    val a = 12
    val b = 42
    A += ("a" -> a)
    A += ("b" -> b)
    vars2json("test.json", A)
  }
}
