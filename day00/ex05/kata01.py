languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

def creators(dic):
	for lang in dic.keys():
		print(lang, "was created by", dic[lang])

creators(languages)
