//单例模式（线程安全、内存安全）

#include <iostream>

class Singleton {
public:
    static Singleton &getInstance() {
        static Singleton instance;
        return instance;
    }

    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;
    void doSomething() {
        std::cout << "do something." << std::endl;
    }

private:
    Singleton() {
        std::cout << "constructor." << std::endl;
    }

    ~Singleton() {
        std::cout << "destructor." << std::endl;
    }
};

int main(int argc, char const *argv[])
{
    static Singleton &instance = Singleton::getInstance();
    instance.doSomething();
    return 0;
}