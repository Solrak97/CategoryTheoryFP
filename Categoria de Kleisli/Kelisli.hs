module Main where


safe_reciprocal :: Double -> Maybe Double
safe_reciprocal x
    | x == 0    =   Nothing
    | otherwise =   Just (x ** (-1)) 


safe_root :: Double -> Maybe Double
safe_root x 
    | x < 0     =   Nothing
    | otherwise   =   Just (sqrt(x))


safe_root_reciprocal :: Double -> Maybe Double
safe_root_reciprocal x = case ( safe_reciprocal x ) of
    Nothing -> Nothing
    Just y -> case ( safe_root y ) of 
        Nothing -> Nothing
        Just z -> Just z


main = do
    print (safe_reciprocal 0)
    print (safe_reciprocal 1)

    print (safe_root (-1))
    print (safe_root 4)

    print (safe_root_reciprocal 0)
    print (safe_root_reciprocal 8)