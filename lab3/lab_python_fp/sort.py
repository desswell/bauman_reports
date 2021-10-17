data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
result = sorted(data, key=abs, reverse=True)
result_with_lambda = sorted(data, key=lambda x: x if x >= 0 else -x, reverse=True)

if __name__ == '__main__':
    print(result)
    print(result_with_lambda)