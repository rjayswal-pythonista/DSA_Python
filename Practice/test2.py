
class Solution:
    def suggestedProducts(self, products, searchWord):
        list_ = []
        products.sort()
        for i, v in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == v]
            list_.append(products[:3])
        return list_

sol = Solution()
products = ['mousepad', 'mobile', 'moneypot', 'monitor', 'mouse']
print(sol.suggestedProducts(products, "mouse"))