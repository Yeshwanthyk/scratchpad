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

--Replicate

replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
    | n <= 0    = []
    | otherwise = x:replicate' (n-1) x

-- Take
take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
    | n <= 0    = []
take' _ []      = []
take' n (x:xs) = x : take' (n-1) xs

-- Reverse
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

--zip
zip' :: [a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x,y) : zip' xs ys

--Elem
elem' :: (Eq a) => a -> [a] -> Bool
elem' a [] = False
elem' a (x:xs)
    | a == x    = True
    | otherwise = a `elem'` xs

-- Quicksort
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
    let smallerSort = quicksort [a | a <- xs, a <= x]
        biggerSort  = quicksort [a | a<- xs, a > x]
    in smallerSort ++ [x] ++ biggerSort
