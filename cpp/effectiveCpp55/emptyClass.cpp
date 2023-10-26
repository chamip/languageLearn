#include <iostream>
#include <string>

class Empty {
public:
    Empty(): _id(0), _name() {}
    Empty(int id, std::string name): _id(id), _name(name) {}
    ~Empty() {}
private:
    int _id;
    std::string _name;
};

int main(int argc, char const *argv[])
{
    std::cout << "123" << std::endl;
    Empty e1;
    Empty e2(e1);
    Empty e3 = e1;
    return 0;
}