from reverse import reverse


def test(string, rev):
    if(string == rev):
        return True
    else:
        return False


''' Test cases '''
print(test("tseet", reverse("teest")))
print(test("olleh", reverse("hello")))
print(test("eciuj elppa @1", reverse("1@ apple juice")))
