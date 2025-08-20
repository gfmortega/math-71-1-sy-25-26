gender = input()
tense = input()

if gender == 'male':
    subj = 'He'
elif gender == 'female':
    subj = 'She'
elif gender == 'other':
    subj = 'They'

if tense == 'past':
    if subj == 'They':
        verb = 'were'
    else:
        verb = 'was'
elif tense == 'present':
    if subj == 'They':
        verb = 'are'
    else:
        verb = 'is'
elif tense == 'future':
    verb = 'will be'

print(f'{subj} {verb} happy.')