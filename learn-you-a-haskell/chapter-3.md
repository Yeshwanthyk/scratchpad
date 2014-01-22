* Haskell has ***type inference***. This just means that haskell can infer on its own without us explicitly telling it what the type of a function or a expression is.
* We can use **:t** in GHCI to find out the type:

        > :t "Hello!" -- "Hello!" :: [Char]
* A string is a **[Char]** type because it is a list of characters:

        > : "a" -- "a" :: Char
