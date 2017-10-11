from flask import current_app, Flask, Response


class MIPYTResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_cookie('MI-PYT', 'best')


class GreeterApp(Flask):
    response_class = MIPYTResponse

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.greetings = 0

    def greet(self):
        self.greetings += 1
        return 'Hello!'


app = GreeterApp(__name__)


@app.route('/')
def greet():
    return current_app.greet()


@app.route('/number')
def greetings_number():
    return str(current_app.greetings)
