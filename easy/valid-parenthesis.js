function isValidParenthesis(s = '{}') {
    // return early if it's odd, must be missing a matching pair
    if (s.length % 2 !== 0) return false

    const stack = []
    const pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for (let i = 0; i < s.length; i++) {
        const o = s[i] // the current bracket

        if (o in pairs) { // found an opening bracket, so add closing beacket to stack
            stack.push(pairs[o])
        } else { // found the closing bracket,
            if (o !== stack.pop()) { // match to continue or return false to exit from the loop
                return false
            }
        }
    }

    return stack.length === 0
};

// positive tests
console.log(isValidParenthesis('(]') === false) // incr +2 -> check isNextValid
console.log(isValidParenthesis('()({}[])') === true)
console.log(isValidParenthesis('{[([])]}') === true)
console.log(isValidParenthesis('({{{{}}}))') === false)
// console.log('isNs', isNestedValid('({{{{}}}))'));

// console.log(isValidParenthesis('({[]})') === true) // inside -> nested -> slice -> check isNestedValid
// console.log(isValidParenthesis('({[]})[]') === true)
// console.log(isValidParenthesis('({[]})[]{}') === true)
// // negative tests
// console.log(isValidParenthesis('(]') === false)
// console.log(isValidParenthesis('({[]})[]{]') === false)
// console.log(isValidParenthesis('({[]])[]{}') === false)
// console.log(isValidParenthesis('({[][)})') === false)