favorite_languages = {'Jonas': 'python',
                      'Maria': 'c',
                      'Marcos': 'ruby',
                      'Paula': 'python',
                      }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

for language in languages:
    print("\t" + language.title())