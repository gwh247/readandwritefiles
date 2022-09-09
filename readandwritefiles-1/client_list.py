def main():
    client_file = open('clients.txt','r')
    
    for j in client_file:
        client = j.rstrip('\n')

        print(client)

    client_file.close()

main()