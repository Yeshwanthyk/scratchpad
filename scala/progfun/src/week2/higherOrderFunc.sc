package week2

object higherOrderFunc {

	def cube(a: Int) = a * a * a              //> cube: (a: Int)Int
	
	def sumInts(a: Int, b: Int): Int =
		if (a > b) 0 else a + sumInts(a + 1, b)
                                                  //> sumInts: (a: Int, b: Int)Int
		
	def sumCubes(a: Int, b: Int): Int=
		if (a > b) 0 else cube(a) + sumCubes(a + 1, b)
                                                  //> sumCubes: (a: Int, b: Int)Int
                                                  
	// Using Higher Order Functions
	
	def sum(f: Int => Int, a: Int, b: Int): Int =
		if (a > b) 0
		else f(a) + sum(f, a+1, b)        //> sum: (f: Int => Int, a: Int, b: Int)Int
	
	
	sum(x => x * x * x, 2,4)                  //> res0: Int = 99
	
	sumCubes(2,4)                             //> res1: Int = 99
                                                  
}