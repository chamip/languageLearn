#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main() {
    // 创建客户端套接字
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        std::cerr << "Error creating client socket." << std::endl;
        return -1;
    }

    // 设置服务器地址信息
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);  // 使用8080端口
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");  // 服务器地址

    // 连接到服务器
    if (connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        std::cerr << "Error connecting to server." << std::endl;
        close(clientSocket);
        return -1;
    }

    std::cout << "Connected to server." << std::endl;

    while (true) {
        // 接收服务器发送的数据
        char buffer[1024] = {0};
        recv(clientSocket, buffer, sizeof(buffer), 0);
        std::cout << "Server says: " << buffer << std::endl;

        std::string m(buffer);
        if (m == "quit") {
            break;
        }
    }
    // 关闭套接字
    close(clientSocket);

    return 0;
}
