import zope.interface
class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")
    def method(self,x):
        pass
    def method2(self):
        pass
@zope.interface.implementer(MyInterface)
class myclass:
    def method(self,x):
        return x**2
    def method2(self,x):
        return x
obj = myclass()
print(obj.method2("jsdgj"))