package week1

object session {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(172); 
     def sqrtIter(guess: Double, x: Double): Double =
         if (isGoodEnough(guess,x)) guess
         else sqrtIter(improve(guess, x), x);System.out.println("""sqrtIter: (guess: Double, x: Double)Double""");$skip(94); 

    def isGoodEnough(guess: Double, x: Double) =
        Math.abs(guess * guess - x) < 0.001;System.out.println("""isGoodEnough: (guess: Double, x: Double)Boolean""");$skip(77); 

    def improve(guess: Double, x: Double) =
        (guess + x / guess) / 2;System.out.println("""improve: (guess: Double, x: Double)Double""");$skip(52); 
        
    def sqrt(x: Double) = sqrtIter(1.0, x);System.out.println("""sqrt: (x: Double)Double""");$skip(17); val res$0 = 
    
    sqrt(4);System.out.println("""res0: Double = """ + $show(res$0))}
    
}
