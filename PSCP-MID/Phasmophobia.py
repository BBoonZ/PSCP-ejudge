"""Phasmophobia"""
def main(evidence_1, evidence_2, evidence_3):
    """phasmophobia ก็ไม่ค่อยน่ากลัว"""
    ghost_dict = {
        "EMF Level 5": {"Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"},
        "Ghost Writing": {"Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"},
        "Fingerprints": {"Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"},
        "Spirit Box": {"Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"},
        "Freezing Temperatures": {"Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"},
        "Ghost Orb": {"Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"},
        "No evidence": {"Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", "Poltergeist", \
            "Revenant", "Shade", "Spirit", "Wraith", "Yurei"}
        }
    ghost = sorted(ghost_dict[evidence_1].intersection(ghost_dict[evidence_2], \
    ghost_dict[evidence_3]))
    if ghost != []:
        return print(*ghost, sep='\n')
    print('Not yet discovered')
main(input(), input(), input())
