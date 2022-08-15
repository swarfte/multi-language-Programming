def 斐波那契數列(起點:int )->int :
    if 起點 == 1 or 起點 == 2:
        return 1
    return 斐波那契數列(起點 - 1)+斐波那契數列(起點 - 2)
