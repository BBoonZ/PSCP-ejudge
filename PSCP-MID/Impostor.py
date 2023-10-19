"""Impostor"""
import json
def main():
    """amon gus"""
    apollo = {}
    dead = {}
    count = 0
    output = ''
    while True:
        name = input()
        if name == 'Start':
            break
        apollo.update(json.loads(name))
    while True:
        name = input()
        if name == 'End':
            break
        dead.update(json.loads('{"%s": "%s"}' %(name, apollo.pop(name))))
    apollo = dict(sorted(apollo.items()))
    dead = dict(sorted(dead.items()))
 
    for i in apollo.values():
        if i == 'Impostor':
            count += 1
    output += str(count) + ' Impostor Remains\n'
 
    output += '***Alive***\n'
    for i in apollo:
        output += i + ' : ' + apollo.get(i) + '\n'
 
    output += '***Dead***\n'
    for i in dead:
        output += i + ' : ' + dead.get(i) + '\n'
 
    print(output)
main()
