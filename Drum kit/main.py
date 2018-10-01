from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config



Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')



class MyApp(App):
	def build(self):
		bl = GridLayout(cols=3, padding = 10, spacing=10)
		bl.add_widget(Button(text='Kick', on_press=self.kick))
		bl.add_widget(Button(text='Snare', on_press=self.snare))
		bl.add_widget(Button(text='Crash', on_press=self.crash))
		
		return bl


	def kick(self, instance):
		sound = SoundLoader.load('kick.wav')
		sound.play()

	def snare(self, instance):
		sound = SoundLoader.load('snare.wav')
		sound.play()

	def crash(self, instance):
		sound = SoundLoader.load('crash.wav')
		sound.play()



if __name__ == "__main__":
	MyApp().run()
