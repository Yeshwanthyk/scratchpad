factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n   = n * factorial(n-1)

length' :: (Num b) => [a] -> b
length'[]   = 0
length'(_:xs) = 1 + length' xs
