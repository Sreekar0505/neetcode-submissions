class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.join('$,%') + `#${strs.length}`
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let len = ""
        let i = str.length - 1;

        while (str.charAt(i) !== '#') {
            len = str.charAt(i) + len;
            str = str.slice(0,i);
            i--;
        }

        str = str.slice(0,i);

        if (parseInt(len) === 0) return [];
        return str.split('$,%')
    }
}
