import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')

class HelloWorldApp(App):
    def build(self):
        # Create a vertical box layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Create a button
        button = Button(text='Click Me')
        button.bind(on_press=self.on_button_click)
        
        # Create a label for displaying text
        self.label = Label(text='', size_hint_y=None, height=44)
        
        # Add the button and label to the layout
        layout.add_widget(button)
        layout.add_widget(self.label)
        
        return layout
    
    def on_button_click(self, instance):
        # Update the label's text when the button is clicked
        self.label.text = 'Hello, World!'
        
if __name__ == '__main__':
    HelloWorldApp().run()
