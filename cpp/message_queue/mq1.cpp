/*
* 首先，我们需要设计一个基本的步骤来实现这个功能：
* 安装并启动 Redis 服务器。
* 安装 C++ 的 Redis 客户端库，例如 hiredis。
* 创建一个生产者，将消息推送到 Redis 的列表中。
* 创建一个消费者，从 Redis 的列表中弹出消息并处理。
*/
#include <iostream>
#include "hiredis/hiredis.h"

// 生产者
void producer(redisContext* c, const std::string& message) {
    redisReply* reply = (redisReply*)redisCommand(c, "LPUSH message_queue %s", message.c_str());
    freeReplyObject(reply);
}

// 消费者
void consumer(redisContext* c) {
    redisReply* reply = (redisReply*)redisCommand(c, "BRPOP message_queue 0");
    if (reply->type == REDIS_REPLY_ARRAY) {
        for (int j = 0; j < reply->elements; j++) {
            printf("%u) %s\n", j, reply->element[j]->str);
        }
    }
    freeReplyObject(reply);
}

int main() {
    // 连接到 Redis 服务器
    redisContext* c = redisConnect("127.0.0.1", 6379);
    if (c == NULL || c->err) {
        if (c) {
            printf("Error: %s\n", c->errstr);
        } else {
            printf("Can't allocate redis context\n");
        }
        exit(1);
    }

    // 生产者发送消息
    producer(c, "Hello, World!");

    // 消费者接收并处理消息
    consumer(c);

    // 断开连接
    redisFree(c);

    return 0;
}