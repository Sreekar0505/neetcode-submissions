class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stk = []
        for (let i=0; i<s.length; i++) {
            if (s[i] === '(' || s[i] === '{' || s[i] === '[') {
                stk.push(s[i])
            } else {
                if (s[i] === ')' && stk[stk.length-1] === '(') stk.pop()
                else if (s[i] === '}' && stk[stk.length-1] === '{') stk.pop()
                else if (s[i] === ']' && stk[stk.length-1] === '[') stk.pop()
                else stk.push(s[i])
            }
        }
        return stk.length === 0 ? true : false
    }
}
