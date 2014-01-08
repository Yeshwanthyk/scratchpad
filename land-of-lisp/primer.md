## Notes

### Late chapter 3 and 4

* *flet* is the command for setting local functions:

        (flet ((function_name (arguments)
                ...function body...))
            ...body...)

    Example:

        (flet ((f (n)
                    (+ n 10))
               ((g (n)
                    (- n 3)))
            (g (f 5))))         ;; 12

* *labels* works pretty similar to *flet* except when using labels we
can make recursive calls within the local functions. For example:

        (labels ((f (n)
                    (+ n 10))
               ((g (n)
                    (- (a n) 3)))
            (g  5)))                ;; 12

* *cons* is used for concatination

* *car* gets the first element of a list:

        (car '(pork beef chicken))')    ;; PORK

* *cdr* gets the first element of a list:

        (cdr '(pork beef chicken))')    ;; (BEEF CHICKEN)
