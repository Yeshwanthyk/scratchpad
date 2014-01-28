factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n   = n * factorial(n-1)

length' :: (Num b) => [a] -> b
length'[]   = 0
length'(_:xs) = 1 + length' xs

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "maximum of empty list"
maximum' [x] = x
maximum' (x:xs)
    | x > maxTail = x
    | otherwise = maxTail
    where maxTail = maximum' xs

-- More elegant solution
maximumE :: (Ord a) => [a] -> a
maximumE [] = error "maximum of empty list"
maximumE [x] = x
maximumE (x:xs) = max x (maximumE xs)
