#include <iostream>
#include <vector>

// 观察者接口
class Observer {
public:
    virtual void update(const std::string& message) = 0;
};

// 具体观察者
class ConcreteObserver : public Observer {
public:
    ConcreteObserver(const std::string& name) : name(name) {}

    void update(const std::string& message) override {
        std::cout << name << " 收到消息: " << message << std::endl;
    }

private:
    std::string name;
};

// 主题接口
class Subject {
public:
    virtual void attach(Observer* observer) = 0;
    virtual void detach(Observer* observer) = 0;
    virtual void notify(const std::string& message) = 0;
};

// 具体主题
class ConcreteSubject : public Subject {
public:
    void attach(Observer* observer) override {
        observers.push_back(observer);
    }

    void detach(Observer* observer) override {
        auto it = std::find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
        }
    }

    void notify(const std::string& message) override {
        for (auto observer : observers) {
            observer->update(message);
        }
    }

private:
    std::vector<Observer*> observers;
};

int main() {
    ConcreteSubject subject;

    ConcreteObserver observer1("Observer 1");
    ConcreteObserver observer2("Observer 2");

    // 将观察者注册到主题
    subject.attach(&observer1);
    subject.attach(&observer2);

    // 发送消息给所有观察者
    subject.notify("Hello, observers!");

    // 将观察者从主题中移除
    subject.detach(&observer1);

    // 再次发送消息给剩下的观察者
    subject.notify("Second message!");

    return 0;
}
