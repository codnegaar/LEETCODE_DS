class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        Context = nums[:]
        n = len(nums)
        N = 1 << (n - 1).bit_length()
        size = 2 * N
        tree_prod = [1] * size
        tree_pref = [[0] * k for _ in range(size)]

        for i in range(n):
            v = nums[i] % k
            idx = N + i
            tree_prod[idx] = v
            cnt = [0] * k
            cnt[v] = 1
            tree_pref[idx] = cnt

        for i in range(N - 1, 0, -1):
            Lp, Lf = tree_prod[2*i], tree_pref[2*i]
            Rp, Rf = tree_prod[2*i+1], tree_pref[2*i+1]
            prod = (Lp * Rp) % k
            cnt = Lf[:] 
            for remR, c in enumerate(Rf):
                if c:
                    new_rem = (Lp * remR) % k
                    cnt[new_rem] += c
            tree_prod[i] = prod
            tree_pref[i] = cnt
        
        res = []

        for idx, value, start, x in queries:
            p = N + idx
            v_mod = value % k
            tree_prod[p] = v_mod
            cnt = [0] * k
            cnt[v_mod] = 1
            tree_pref[p] = cnt
            p //= 2
            while p:
                Lp, Lf = tree_prod[2*p], tree_pref[2*p]
                Rp, Rf = tree_prod[2*p+1], tree_pref[2*p+1]
                prod = (Lp * Rp) % k
                cnt = Lf[:]  
                for remR, c in enumerate(Rf):
                    if c:
                        new_rem = (Lp * remR) % k
                        cnt[new_rem] += c
                tree_prod[p] = prod
                tree_pref[p] = cnt
                p //= 2

            l, r = N + start, N + n - 1
            left_prod, left_cnt = 1, [0] * k
            right_prod, right_cnt = 1, [0] * k
            while l <= r:
                if (l & 1) == 1:
                    new_prod = (left_prod * tree_prod[l]) % k
                    new_cnt = left_cnt[:] 
                    for remR, c in enumerate(tree_pref[l]):
                        if c:
                            combined = (left_prod * remR) % k
                            new_cnt[combined] += c
                    left_prod, left_cnt = new_prod, new_cnt
                    l += 1
                if (r & 1) == 0:
                    new_prod = (tree_prod[r] * right_prod) % k
                    new_cnt = tree_pref[r][:]  
                    for remR, c in enumerate(right_cnt):
                        if c:
                            combined = (tree_prod[r] * remR) % k
                            new_cnt[combined] += c
                    right_prod, right_cnt = new_prod, new_cnt
                    r -= 1
                l //= 2
                r //= 2

            total_cnt = left_cnt[:] 
            for remR, c in enumerate(right_cnt):
                if c:
                    combined = (left_prod * remR) % k
                    total_cnt[combined] += c
            res.append(total_cnt[x])
        return res
