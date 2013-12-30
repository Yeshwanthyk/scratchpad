;;;; The following is the code for guess the number wherein we basically
;;;; write a binary search in order guess the number.

;;; The way this works is we type (guess-my-number), if the number in our
;;; mind is higher we type (bigger) else we type (smaller)

(defparameter *small* 1)

(defparameter *big* 100)

;; defun is defined as :
;; (defun fn_name (args)
;;  ...)

;; ash here is the arthimetic shift operator
;; Basically, (ash 11 1) -> 22 because binary of 22 is 10110
;; but by passing in (ash 11 -1) -> 5 which has a binary of 101
(defun guess-my-number ()
  (ash (+ *small* *big*) -1))

(defun smaller ()
  (setf *big* (1- (guess-my-number)))
  (guess-my-number))

(defun bigger ()
  (setf *small* (1+ (guess-my-number)))
  (guess-my-number))

;; To reset the values again
(defun start-over ()
  (defparameter *small* 1)
  (defparameter *big* 100)
  (guess-my-number))