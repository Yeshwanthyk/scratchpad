import Data.Char

-- Throw an expected error
expected s = s ++ "expected"

-- Tests if two chars match
matchChars :: Char -> Char -> Bool
matchChars x y = x == y

-- Gets and identifier
-- Throws an exception if not an alpha
getName :: Char -> Char
getName x
	| isAlpha x = x
	| otherwise = error (expected "Name ")

-- Check if char is a digit
-- Throws an exception if not a number
getNum :: Char -> Char
getNum x
	| isDigit x = x
	| otherwise = error (expected "Number ")

-- Prefix a string with a tab
emit s = "\t" ++ s

-- Prefix a string with a tab and postfix it with a new line
emitLn s = (emit s) ++ "\n"

expression x = emitLn ("MOVE #" ++ [num] ++ ",DO")
	where num = getNum x
