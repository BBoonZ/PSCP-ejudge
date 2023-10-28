"""[Recommended] Music Lover"""
def main(val):
    """หน้าร้อน"""
    artist = [input().strip() for _ in range(val)]
    artist_dict = {}
    for i in artist:
        for j in range(len(i)):
            if i[j] == '-':
                artist_dict[i[:j]] = artist_dict.get(i[:j], '') + i[j+1:] + '\n'
    for i in artist_dict.keys():
        print(i)
        print(artist_dict[i][:-1])
main(int(input()))
