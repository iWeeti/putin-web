from django.http import HttpResponse
import random

def meme(request):
	memes  =[
		'https://media.discordapp.net/attachments/490209717214248963/490210033133682690/Rare_Roblox_nintendo_ds_box_art.jpg?width=308&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210142244306955/Ratatouille_4.gif',
		'https://media.discordapp.net/attachments/490209717214248963/490210143708119051/cry.jpg',
		'https://media.discordapp.net/attachments/490209717214248963/490210156148424739/thelook.jpg',
		'https://media.discordapp.net/attachments/490209717214248963/490210167175249920/dancing_dad.gif',
		'https://media.discordapp.net/attachments/490209717214248963/490210172015345671/2012ksi.PNG',
		'https://media.discordapp.net/attachments/490209717214248963/490210173856776239/trollface.jpg?width=225&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210173387014185/SLOB.png?width=306&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210214012911629/sooperangery.png?width=220&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210246036422656/hatt.PNG?width=320&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210253250625547/cat_boye.PNG?width=310&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210263065165834/death_himself.PNG?width=238&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210292505116673/KSI_HAS_C_e_n_s_e_r.jpg?width=400&height=225',
		'https://media.discordapp.net/attachments/490209717214248963/490210326328115201/Adippadibabas.png?width=373&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210371035070484/knife_cat.jpg?width=332&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210371982983168/LUL.PNG?width=363&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210381319372810/cat.jpg?width=304&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210404245438474/HECCIN_FUCCIN_OOF.jpg?width=301&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210428882780171/emoog.PNG',
		'https://media.discordapp.net/attachments/490209717214248963/490210453868380171/T.jpg?width=329&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210468011704330/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.jpg?width=300&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210485627518990/COOL_DOG.jpg?width=300&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210516619362319/PHAT_TIGER.jpg?width=318&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210543102066711/Dead.PNG?width=150&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210559925551115/giraffe.png?width=115&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210607027453952/bunnu.jpg?width=168&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490210664204468225/hot_WHAT_THE_HELL.jpg?width=238&height=301',
		'https://media.discordapp.net/attachments/490209717214248963/490210686387879936/Gordon_Pose.jpg?width=400&height=223',
		'https://media.discordapp.net/attachments/490209717214248963/490210749462085633/animegay.jpg?width=400&height=195',
		'https://media.discordapp.net/attachments/490209717214248963/490210776561483799/gta.PNG?width=400&height=277',
		'https://media.discordapp.net/attachments/490209717214248963/490210805187477509/n00b.png?width=170&height=300',
		'https://media.discordapp.net/attachments/490209717214248963/490213305214828555/big_gay.png?width=400&height=208',
		'',
	]
	_meme = random.choice(memes)
	return HttpResponse(f'\{"meme":"{_meme}"\}')
