from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Dummy user data (replace with your own logic)
user = {'pin': 1234, 'name': 'Mr. John', 'balance': 3000}

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text='Welcome to the PythonATM', size_hint=(1, 0.5))
        self.pin_input = TextInput(hint_text='Please enter your four-digit PIN', password=True, size_hint=(1, 0.2))
        self.login_button = Button(text='Login', size_hint=(1, 0.2))
        self.login_button.bind(on_press=self.login)
        
        self.add_widget(self.label)
        self.add_widget(self.pin_input)
        self.add_widget(self.login_button)
    
    def login(self, instance):
        entered_pin = self.pin_input.text
        if entered_pin.isdigit() and int(entered_pin) == user['pin']:
            self.parent.current = 'menu'
        else:
            self.label.text = 'Invalid PIN. Please try again.'

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text=f'Welcome, {user["name"]}! Your balance is {user["balance"]} Rupees', size_hint=(1, 0.5))
        self.withdraw_button = Button(text='Withdraw Cash', size_hint=(1, 0.2))
        self.deposit_button = Button(text='Deposit Cash', size_hint=(1, 0.2))
        
        self.add_widget(self.label)
        self.add_widget(self.withdraw_button)
        self.add_widget(self.deposit_button)

class MyApp(App):
    def build(self):
        # Create a screen manager
        sm = ScreenManager()
        
        # Create and add screens to the screen manager
        login_screen = LoginScreen()
        menu_screen = MenuScreen()
        sm.add_widget(login_screen)
        sm.add_widget(menu_screen)
        
        return sm

if __name__ == '__main__':
    MyApp().run()
