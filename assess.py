def chessBoard(inputNum):
    for i in range(inputNum):
        for j in range(inputNum):
            if(j+i) % 2 == 0:
                #N = ' W '
                N = print("W", end=" ")
                
            else: 
                #N = ' B '
                N = print("B", end=" ")

                
        print()
    return N

def main():
    inputNum = int(input())
    if inputNum > 0 and inputNum < 1000:
        result = chessBoard(inputNum)
        return result
    else:
        pass

if __name__ == "__main__":
    main()