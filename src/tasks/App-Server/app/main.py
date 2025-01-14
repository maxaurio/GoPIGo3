 
import socket

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.clock import Clock

from functools import partial

#from kivy.garden.joystick import Joystick

class MainWindow(Screen):
	pass

class ButtonWindow(Screen):
	pass

class JoystickWindow(Screen):
	'''
	self.joystick_instance.bind(pad=self._update_pad_display)

	def _update_pad_display(self, instance, pad):
		x, y = pad
		x, y = (str(x)[0:5], str(y)[0:5])
		x, y = (('x: ' + x), ('\ny: ' + y))
		r = "radians: " + str(instance.radians)[0:5]
		m = "\nmagnitude: " + str(instance.magnitude)[0:5]
		a = "\nangle: " + str(instance.angle)[0:5]
		#self.root.ids.pad_display_xy.text = "".join([x, y])
		print("".join([x, y]))
		#self.root.ids.pad_display_rma.text = "".join([r, m, a])
		print("".join([r, m, a]))
	'''
	pass

class SendCommands():
	def startClient(self, host_name, port_name):
		try:
			HOST = '127.0.0.1'  # The server's hostname or IP address (this is the default)
			HOST = host_name
			PORT = 65433  # The port used by the server (this is the default)
			PORT = int(port_name)
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.connect((HOST, PORT))
			print("Connected")
			successPopup()
		except:
			print("Could not connect")
			errorPopup()

	def sendMessage(self,command):
		try:
			print("Sent:",command)
			self.s.sendall(bytes(str(command), 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

class SliderWindow(Screen):
	
	active = False
	prev_left = "#"
	prev_right = "#"

	def send_values(self,left,right):
		print("l",int(self.left_slider.value),"r",int(self.right_slider.value))
		MyRaspberryApp.send_commands.sendMessage("l"+str(int(self.left_slider.value))+"r"+str(int(self.right_slider.value)))

	pass

class WindowManager(ScreenManager):
	pass

class popupConnectionError(FloatLayout):
	pass
class popupConnectionSuccess(FloatLayout):
	pass

class errorPopup(Popup):
    def __init__(self, **kwargs):
        self.popup = Popup(title = "Error", content = popupConnectionError(), size_hint = (None, None), size = (400,150))
        self.popup.open()
        Clock.schedule_once(self.dismiss_popup, 4)

    def dismiss_popup(self, dt):
        self.popup.dismiss()

class successPopup(Popup):
    def __init__(self, **kwargs):
        self.popup = Popup(title = "Success", content = popupConnectionSuccess(), size_hint = (None, None), size = (400,150))
        self.popup.open()
        Clock.schedule_once(self.dismiss_popup, 2)

    def dismiss_popup(self, dt):
        self.popup.dismiss()



kv = Builder.load_file("main.kv")

class MyRaspberryApp(App):
	send_commands = SendCommands()
	slider_window = SliderWindow()
	main_window = MainWindow()

	def build(self):
		return kv

if __name__=="__main__":
	MyRaspberryApp().run()