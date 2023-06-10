'''def  fun1(n):
    i = 0 
    if (n >1):
        fun1(n - 1) 
    for i in range(n):
        print(" * ",end="")
    print()
n=int(input())
fun1(n)'''
# Assume that n is greater than or equal to 0 */
def fun2(n):
    if(n == 0):
        return
     
    fun2(n // 2)
    print(n % 2, end="")
n=int(input())
fun2(n)
