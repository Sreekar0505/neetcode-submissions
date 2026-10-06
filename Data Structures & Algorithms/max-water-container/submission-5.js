class Solution {
    /**
     * @param {number[]} h
     * @return {number}
     */
    maxArea(h) {
        const n = h.length;
        if (n===0) return 0;
        const prev = new Array(n).fill(0);
        prev[0] = h[0]
        const next = new Array(n).fill(0)
        next[n-1] = h[n-1]
        for (let i=1; i<n; i++) {
            prev[i] = Math.max(prev[i-1],h[i])
        }
        for (let j=n-2; j>=0; j--) {
            next[j] = Math.max(next[j+1],h[j])
        }

        let res = 0;
        let l=0, r=n-1;

        while (l<r) {
            const area = Math.min(prev[l],next[r]) * (r-l)
            res = Math.max(res,area)
            if (prev[l] < next[r]) l++;
            else r--;
        }

        return res
    }
}
