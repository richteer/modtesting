from module import XMPPModule

class Eval(XMPPModule):
	
	def handleMessage(self, msg):
		if msg['body'].startswith("!eval"):
			if self.xmpp.isadmin(msg=msg):
				eval(msg['body'].split(" ",1)[1])
			else:
				self.xmpp.reply(msg, "Nice try.")
