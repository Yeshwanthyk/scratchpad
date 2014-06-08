package week2

object higherOrderFunc {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(70); 

	def cube(a: Int) = a * a * a;System.out.println("""cube: (a: Int)Int""");$skip(80); 
	
	def sumInts(a: Int, b: Int): Int =
		if (a > b) 0 else a + sumInts(a + 1, b);System.out.println("""sumInts: (a: Int, b: Int)Int""");$skip(88); 
		
	def sumCubes(a: Int, b: Int): Int=
		if (a > b) 0 else cube(a) + sumCubes(a + 1, b);System.out.println("""sumCubes: (a: Int, b: Int)Int""");$skip(177); 
                                                  
	// Using Higher Order Functions
	
	def sum(f: Int => Int, a: Int, b: Int): Int =
		if (a > b) 0
		else f(a) + sum(f, a+1, b);System.out.println("""sum: (f: Int => Int, a: Int, b: Int)Int""");$skip(30); val res$0 = 
	
	
	sum(x => x * x * x, 2,4);System.out.println("""res0: Int = """ + $show(res$0));$skip(17); val res$1 = 
	
	sumCubes(2,4);System.out.println("""res1: Int = """ + $show(res$1))}
                                                  
}
