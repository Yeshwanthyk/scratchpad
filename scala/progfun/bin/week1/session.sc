package week1

object session {
		
		def	sqrt(x: Double) = {

     	def sqrtIter(guess: Double) : Double =
        	 if (isGoodEnough(guess)) guess
      	   else sqrtIter(improve(guess))

    	def isGoodEnough(guess: Double) =
      	  Math.abs(guess * guess - x) < 0.001

    	def improve(guess: Double) =
  	      (guess + x / guess) / 2
        
	    sqrtIter(1.0)
    
    }                                             //> sqrt: (x: Double)Double

    sqrt(4)                                       //> res0: Double = 2.0000000929222947
    
}