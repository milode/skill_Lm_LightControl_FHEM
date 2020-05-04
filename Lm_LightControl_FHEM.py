from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_LightControl_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Steuert das licht ueber fhem
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
