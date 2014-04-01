package week1

object session {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(379); 
		
		def	sqrt(x: Double) = {

     	def sqrtIter(guess: Double) : Double =
        	 if (isGoodEnough(guess)) guess
      	   else sqrtIter(improve(guess))

    	def isGoodEnough(guess: Double) =
      	  Math.abs(guess * guess - x) < 0.001

    	def improve(guess: Double) =
  	      (guess + x / guess) / 2
        
	    sqrtIter(1.0)
    
    };System.out.println("""sqrt: (x: Double)Double""");$skip(159); 
    
    // Calls itself.. So tail recursive call so uses
    // constant stack frame
    def gcd(a: Int, b: Int): Int =
    	if (b == 0) a else gcd(b, a % b);System.out.println("""gcd: (a: Int, b: Int)Int""");$skip(97); 

		// Not tail-recursive
		def factorial(n: Int): Int =
			if (n == 0) 1 else n * factorial(n-1);System.out.println("""factorial: (n: Int)Int""");$skip(17); val res$0 = 
				
    sqrt(4);System.out.println("""res0: Double = """ + $show(res$0));$skip(20); val res$1 = 
    
    gcd(14,21);System.out.println("""res1: Int = """ + $show(res$1));$skip(22); val res$2 = 
    
    factorial(5);System.out.println("""res2: Int = """ + $show(res$2))}
    
}
