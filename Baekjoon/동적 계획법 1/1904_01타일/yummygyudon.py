N = int(input())
def tile_case(n) :
    tile_basic = [0,1,2]
    if n >=3 :
        for i in range(3, n+1):
            tile_basic.append((tile_basic[i-1]+tile_basic[i-2])%15746)
    print(tile_basic[n])

tile_case(N)