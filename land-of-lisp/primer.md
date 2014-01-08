## Notes

### Late chapter 2 and 3, 4

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

* We can use both *cdr* and *car* on a list:

        (car (cdr '((peas carrots chicken))))    ;;CARROTS

    Can also be written as:

        (cadr '((peas carrots chicken)))    ;;CARROTS
