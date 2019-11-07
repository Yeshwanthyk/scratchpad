"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


def decode_string(s):

    if not s:
        return s

    stack = []

    for i in s:

        if i == "[":
            continue

        stack.append(i)

        if i == ']':
            # remove `]` that gets pushed into the stack
            stack.pop()
            str = ""
            while True:
                popped = stack.pop()

                if popped.isdigit():

                    dig = popped
                    if len(stack) > 0:
                        while True:
                            if not stack:
                                break

                            if stack[-1].isdigit():
                                dig = stack.pop() + dig
                            else:
                                break

                        str = int(dig) * str
                        stack.append(str)
                        break
                else:
                    str = popped + str

    return ''.join(stack)


s = "2[20[xy]]pq"
ans = decode_string(s)
print(ans)
