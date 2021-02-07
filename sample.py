import fingerPrint as fp

if __name__ == "__main__":

    fingerPrint = fp.FingerPrint('/dev/ttyAMA1', 57600, 1.0, 27)

    listname = list(range(10))
    listfinger = b''
    count = 0
    result = 100
    while True:

        print("1:登録　2:認証")
        selectNum = input()
        if int(selectNum) == 1:
            fingerPrint.enroll()
            fingerPrint.regModel()
            print("IDを入力")
            listname.insert(count,input())
            listfinger = fingerPrint.upImage1()
            print("登録完了")
            count = count + 1
        
        elif int(selectNum) == 2:
            print("IDを入力")
            idname = input()
            i = 0
            while i < 6:
                if idname == listname[i]:
                    break
                i = i + 1
            
            if idname == listname[i]:

                fingerPrint.loginFinger()
                fingerPrint.downLoadImage2(listfinger)
                result = fingerPrint.match()
                if result == 1:
                    print(listname[i] + "さんの指紋と一致しました")
                elif result == 2:
                    print(listname[i] + "さんの指紋と一致しませんでした")
                elif result == 100:
                    print("認証失敗。もう一度お願い")
                else:
                    print("エラー")
            else:
                print("IDが違います")
        else:
            print("数値を入力")