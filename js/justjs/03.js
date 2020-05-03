//# Just Javascript by Dan Abromov

//# Recap
//# There are only 7 primitive types in JS - number, string, boolean, null, undefined, Symbol, BigInt
//# The other values are - Objects and Functions

console.log(typeof(2))
//# "number"
//# types are always of type string

console.log(typeof(null))
//# "object"
//#old bug in js that is too late to be fixed

//# 03

let reaction = "yikes"
reaction[0] = 1
console.log(reaction)
//# yikes

//# primitive values in js are immutable
//# a string might feel similar to an array but its immutable

let pet = "dog"
pet = "cat"
console.log(pet)
//# "cat"

//# This may seem like a contradiction but it is not. String are immutable but
//# variables are not values. variables POINT to values

//# Variables is a WIRE. with two ends and a direction
//# The right side of the assignment MUST be an EXPRESSION

//# Variables ALWAYS points to values. Variables ARE NOT Values.
let x = 10
y = x
x = 0

//# x ------- 10
//#           |
//# y --------|

//# x --------0

//# So, finally variable x point to the value 0 and variable y points to the value 10

let s = "Tom and Jerry"
feed(s)
console.log(s[0])
//I made a mistake here thinking the variable s can be changed but of course it can't be. Because we are
//passing in the value which is immutable and not the variable in to a function.



