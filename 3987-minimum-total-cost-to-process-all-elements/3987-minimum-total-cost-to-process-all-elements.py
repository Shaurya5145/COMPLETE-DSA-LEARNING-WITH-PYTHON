class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:

        cost = 0
        operation_no = 1
        resources = k
        MOD = 10**9 + 7
        
        for i in range(len(nums)):
            if nums[i]>resources:
                
                resources_need = nums[i]-resources
                

                if resources_need>k:
                    floor_div = resources_need // k

                    modulo_div = resources_need % k

                    if modulo_div <= k and modulo_div!=0:
                        modulo_div = 1

                    operations_need = floor_div + modulo_div

                    resources += k*operations_need
                    resources -= nums[i]
                    

                    exp1 = 2*operation_no
                    exp2 = operations_need-1
                    exp3 = exp1 + exp2

                    cost += (operations_need*exp3)//2

                    operation_no += operations_need

                else:
                    resources+=k
                    resources-=nums[i]
                    cost += operation_no
                    operation_no += 1
            else:
                resources -= nums[i]

        return int(cost)%MOD

        