//编写一个观察者模式的样例

#include <string>
#include <iostream>
#include <vector>

//观察者接口
class Observer {
public:
	virtual void update(const std::string &name) = 0;
};

//集体观察者
class ConcreteObserver: public Observer {
public:
	ConcreteObserver(const std::string &_name) : name(_name) {}
	void update(const std::string &message) override {
		std::cout << name << "received message: " << message << std::endl;
	}

private:
	std::string name;
};

//主题接口
class Subject {
public:
	virtual void attach(Observer *observer) = 0;
	virtual void detach(Observer *observer) = 0;
	virtual void notify(const std::string &message) = 0;
};

//具体主题
class ConcreteSubject : public Subject {
public:
	void attach(Observer *observer) override {
		vc.push_back(observer);
	}

	void detach(Observer *observer) override {
		//std::find,since c++20
		auto it = std::find(vc.begin(), vc.end(), observer);
		if (it != vc.end()) {
			vc.erase(it);
		}
	}

	void notify(const std::string &message) override {
		for (auto ob : vc) {
			ob->update(message);
		}
	}

private:
	std::vector<Observer*> vc;
};

int main(int argc, char const *argv[])
{
	ConcreteObserver ob1("ob1"), ob2("ob2");
	ConcreteSubject sub;
    //将观察者注册到主题
	sub.attach(&ob1);
	sub.attach(&ob2);
    //发送消息给所有观察者
	sub.notify("hello, world!");
    //将观察者从主题中移除
	sub.detach(&ob1);
    //再次发送消息给剩下的观察者
	sub.notify("Good Bye.");
	return 0;
}

