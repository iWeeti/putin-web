

class BotRouter:
	def db_for_write(self, model, **hints):
		if model._meta.app_label == 'putin':
			return 'bot'
		return None

	def db_for_read(self, model, **hints):
		if model._meta.app_label == 'putin':
			return 'bot'
		return None