;;;; The following is the code for guess the number wherein we basically
;;; write a binary search in order guess the number

(defparameter *small* 1)

(defparameter *big* 100)

;; defun is defined as :
;; (defun fn_name (args)
;;  ...)

;; ash here is the arthimetic shift operator
;; Basically, (ash 11 1) -> 22 because binary of 22 is 10110
;; but by passing in (ash 11 -1) -> 5 which has a binary of 101
(defun guess-my-number ()
  (ash (*small* *big*) -1))
