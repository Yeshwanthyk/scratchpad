* Can't mix various types in lists
* An **If** function should always have an else block
* List can be joined together using ***++***; but have to noted that when we do
  that haskell has to traverse the whole list on the left hand side.
* we can use **":"** which is the **cons** operator:

        5:[1,2,3] -- [5,1,2,3]
* We can use ***"!!"*** to get the index of a list. (Strings are basically lists!!)
* Lists
    - **head** takes a list and returns the first element.
    - **tail** takes a list and returns the all the element except the first one.
    - **last** takes a list and returns the last element.
    - **init** takes a list and returns everything except the last element.
    - **reverse** reverses the list
    - **take** takes an number and a list and returns that mn=any elemnts from the list. If index doesn't exist throws an error.
    - **drop** does what take does but gives all elements minus what the index given:

            drop 3 [1,2,3,4,5,6] -- [4,5,6]

            drop 100 [1,2,3] -- []
* **null** gives wheather is list is null or not
* **minimum**, **maximum**, **product** and **sum** work on lists.

