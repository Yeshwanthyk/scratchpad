The main difference between a definition and a
val is that the definition is call by name and
the val is call-by-value

    def loop: Boolean = loop

    def x = loop // Runs fine

    val x = loop // Stuck in a infinite loop

We write the and(x,y) method::

    def and(x: Boolean, y: Boolean) =
        | if (x) y else false

If we pass in a non-terminating value. The function get
stuck in a infinite loop::

    and(false, loop)

To fix this we change the second parameter to call-by-name::

    def and(x: Boolean,y: => Boolean) =
        | if (x) y else false
