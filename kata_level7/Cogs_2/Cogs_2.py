def cog_RPM(cogs, n):
    result = [0, 0]

    def compute_rpm(target):
        rpm = 1
        sign = 1

        if target < n:
            for i in range(n, target, -1):
                rpm *= cogs[i] / cogs[i - 1]
                sign *= -1
        elif target > n:
            for i in range(n, target):
                rpm *= cogs[i] / cogs[i + 1]
                sign *= -1

        return rpm * sign

    result[0] = compute_rpm(0)
    result[1] = compute_rpm(len(cogs) - 1)

    return result
