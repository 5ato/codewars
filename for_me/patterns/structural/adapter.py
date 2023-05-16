class Target:
    def request(self):
        return 'Any request from Target'


class Adaptee:
    def specific_request(self):
        return 'eetpadA eht fo roivaheb laicepS'


class Adapter(Adaptee, Target):
    def request(self):
        return f'Adapter: {self.specific_request()[::-1]}'
    

def client_code(target: Target):
    print(target.request())
