import re
for _ in range(int(input())):
    uid = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}',uid)
        assert re.search(r'\d\d\d',uid)
        assert not re.search(r'[^a-zA-Z0-9]',uid)
        assert not re.search(r'(.)\1',uid)
        assert len(uid)==10
    except:
        print('Invalid')
        
    else:
        print('Valid')