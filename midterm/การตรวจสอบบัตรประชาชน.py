"""2988"""
def main():
    """การตรวจสอบบัตรประชาชน"""
    id_card = input()
    if len(id_card) == 13:
        print("yes")
    else:
        print("no")
main()
