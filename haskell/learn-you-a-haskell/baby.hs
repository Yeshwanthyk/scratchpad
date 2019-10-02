doubleMe x = x + x

doubleUs x y = x*2 + y*2

-- removeUpperCase :: [Char] -> [Char]
removeUpperCase :: String -> String
removeUpperCase st = [c | c <- st, elem c ['A'..'Z']]
