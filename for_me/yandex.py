def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        server_data = data[0]
        n, m, q = int(server_data[0]), int(server_data[2]), int(server_data[4:6:])
        servers = []
        for i in range(n):
            temp = []
            for j in range(1, m+1):
                temp.append(1)
            servers.append((temp, {'reset_count': 0}))

    for i in data[1::]:
        if 'DISABLE' in i:
            datacenter = int(i[-3])-1
            server = int(i[-1])-1
            servers[datacenter][0][server] = 0
        elif 'GETMAX' in i:
            temp = []
            for j in servers:
                temp.append(j[0].count(1) * j[1]['reset_count'])
            answer = temp.index(max(temp))+1
            print(answer)
        elif 'GETMIN' in i:
            temp = []
            for j in servers:
                temp.append(j[0].count(1) * j[1]['reset_count'])
            answer = temp.index(min(temp)) + 1
            print(answer)
        elif 'RESET' in i:
            server_for_reset = int(i[-1]) - 1
            for j in range(len(servers[server_for_reset][0])):
                servers[server_for_reset][0][j] = 1
            servers[server_for_reset][1]['reset_count'] += 1

    return servers


if __name__ == '__main__':
    print(main())
