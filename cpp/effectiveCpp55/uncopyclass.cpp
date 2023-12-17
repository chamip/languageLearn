/*
 * 若不想编译器自动生成copy构造、copy assignment，应该明确拒绝；
 * 1. 可以在类中声明为private；
 * 2. 编写基类，派生类中私有继承，参考uncopyable类；
 */

#include <iostream>

class uncopyable {
    protected:
        uncopyable() {};
        ~uncopyable() {};
    private:
        uncopyable(const uncopyable&);
        uncopyable& operator=(const uncopyable&);
};

class c1 : private uncopyable {
    private:
        int a;
        float b;
    public:
        c1() : a(-1), b(-1.0) {};
        c1(int _a, float _b) : a(_a), b(_b) {};
        void c1_func() {
            std::cout << "a: " << a << std::endl << "b: " << b << std::endl;
        }
        ~c1() {};
};
class Base1 {
    private:
        int a;
        float b;
    public:
        void base1_func() {
            std::cout << a << ", " << b << std::endl;
        }
};

class Derived1 : private Base1 {
    public:
        //报错，私有成员只在生命它的类中能直接访问，派生类是不能直接访问的
        // Derived1() { a = 2; };

        void derived1_func() {
            base1_func();
        }
};



int main(int argc, char *const argv[]) 
{
    c1 c(1, 2.0);
    c.c1_func();
    
    //copy assignment失败
    // c1 c0;
    // c.c1_func();
    // c = c0;
    
    //copy 构造失败
    // c1 c0 = c1(1, 2);
    // c0.c1_func();

    Derived1 d1 = Derived1();
    d1.derived1_func();
    return 0;
}