//编写一个shared_ptr

#include <iostream>

template <typename T>
class SharedPtr {
private:
    T *data;            //指向共享对象
    int *refCount;      //引用计数

public:
    //构造函数
    //explicit可以避免隐式类型转换或其他意外类型转换，提高代码可读性和可维护性
    explicit SharedPtr(T *ptr = nullptr) : data(ptr), refCount(new int(1)) {
        std::cout << "Shared pointer created. Ref count: " << *refCount << std::endl;
    }
    //拷贝构造函数
    SharedPtr(const SharedPtr<T> &other) : data(other.data), refCount(other.refCount) {
        ++(*refCount);
        std::cout << "Shared pointer copied. Ref count: " << *refCount << std::endl;
    }
    //赋值运算符
    SharedPtr<T> &operator=(const SharedPtr<T> &other) {
        if (this != &other) {
            release();
            data = other.data;
            refCount = other.refCount;
            ++(*refCount);
            std::cout << "Shared pointer assigned. Ref count: " << *refCount << std::endl;
        }
        return *this;
    }
    //获取共享对象的资源
    T *get() const {
        return data;
    }
    //获取引用计数
    int user_count() const {
        return *refCount;
    }
    //析构函数
    ~SharedPtr() {
        release();
    }
private:
    //释放资源
    void release() {
        --(*refCount);
        std::cout << "Shared pointer released. Ref count: " << *refCount << std::endl;
        if (*refCount == 0) {
            delete data;
            delete refCount;
            std::cout << "Shared pointer resources freed." << std::endl;
        }
    }
};

int main(int argc, char const *argv[])
{
    //构造函数
    SharedPtr<int> ptr1(new int(123));
    std::cout << "Use Count: " << ptr1.user_count() << std::endl;

    //拷贝构造
    // SharedPtr<int> ptr2(ptr1);
    SharedPtr<int> ptr2 = ptr1;
    std::cout << "Use Count: " << ptr2.user_count() << std::endl;
    
    //重载赋值运算符
    SharedPtr<int> ptr3(new int(124));
    ptr3 = ptr1;
    std::cout << "Use Count: " << ptr3.user_count() << std::endl;

    return 0;
}