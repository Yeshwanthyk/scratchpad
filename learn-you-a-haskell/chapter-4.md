* Pattern matching is shown with the example in **factorial.hs**
* We should always try to have a catch-all pattern in order to avoid errors.
* Catch-all examples:

        first :: (a,b,c) -> a
        first(x,_,_)    = x

        second :: (a,b,c) -> b
        first(_,y,_)    = y
* We can pattern match in list comprehensions. If a match fails, it ignores and moves to the next one:

        let xs = [(1,3), (4,5), (7,8)]
        [a+b | (a,b) <- xs]
* You can write patterns for breaking up something into names whilst still keeping a reference to the whole thing:

        capital :: String -> String
        capital "" = "Empty string"
        capital all@(x:xs) = "The first letter of" ++ all ++ "is" ++ x
* Pipes **|** in functions which are akin to if statements:

        bmiTell :: (RealFloat a) => a -> String
        bmiTell weight height
            | weight / height ^ 2<= 18.5 = "You're underweight"
            | weight / height ^ 2<= 28 = "Normal"
            | otherwie = "You're are a whale."
* There is no **=** after the function name and its parameters before the first guard.
* Instead of repeating across the code base we can use **where**:

        bmiTell :: (RealFloat a) => a -> String
        bmiTell bmi
            | bmi <= skinny = "You're underweight"
            | bmi <= normal = "Normal"
            | otherwie = "You're are a whale."
            where bmi = weight / height ^ 2
                  skinny = 18.5
                  normal = 25.0
