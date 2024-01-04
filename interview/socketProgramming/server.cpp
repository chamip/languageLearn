#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string>

int main() {
    // 创建服务器套接字
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        std::cerr << "Error creating server socket." << std::endl;
        return -1;
    }

    // 设置服务器地址信息
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);  // 使用8080端口
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    // 绑定套接字
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        std::cerr << "Error binding server socket." << std::endl;
        close(serverSocket);
        return -1;
    }

    // 监听连接
    if (listen(serverSocket, 5) == -1) {
        std::cerr << "Error listening for connections." << std::endl;
        close(serverSocket);
        return -1;
    }

    std::cout << "Server listening on port 8080..." << std::endl;

    // 接受连接
    struct sockaddr_in clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);
    int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
    if (clientSocket == -1) {
        std::cerr << "Error accepting connection." << std::endl;
        close(serverSocket);
        return -1;
    }

    std::cout << "Client connected." << std::endl;

    // 发送数据到客户端
    const char* message = "Hello from server!";
    send(clientSocket, message, strlen(message), 0);

    while (true) {
        std::string message;
        std::cin >> message;

        char* m = new char[message.size() + 1];
        strcpy(m, message.c_str());
        send(clientSocket, m, strlen(m), 0);
        
        if (message == "quit") {
            break;
        }
    }

    // 关闭套接字
    close(clientSocket);
    close(serverSocket);

    return 0;
}
