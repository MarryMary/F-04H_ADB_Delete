import sys
import os
import subprocess

print("富士通社製タブレット・ドコモ arrows Tab(アローズ・タブ） F-04H デフォルト搭載アプリケーション削除スクリプトへようこそ")
print("本アプリケーションは純正ROMを搭載、root化も行っていない純粋なシステムに対してのみ動作を確認しています。")
print("対応OSは Android 6.0, Android7.1バージョンです。")
print("メニューから実行したい削除シークエンスの番号を入力してください。")

menu_array = ["[1] ドコモデフォルトアプリケーション強制削除", "[2] 富士通デフォルトアプリケーション強制削除", "[3] ドコモ・富士通デフォルトアプリケーション両削除", "[4] スクリプト終了"]
d_app = {"アプリクラッシュレポート": "com.nttdocomo.android.bugreport", "あんしんスキャン": "com.mcafee.vsm_android_dcm", "エリアメール": "com.nttdocomo.android.areamail", "オートGPS": "com.nttdocomo.android.atf", "おすすめ使い方ヒント": "com.nttdocomo.android.devicehelp", "おまかせロック": "com.nttdocomo.android.remotelock", "しゃべってコンシェル": "com.nttdocomo.android.mascot", "スケジュールメモ・トルカ同期": "com.nttdocomo.android.databackup", "スケジュール&メモ": "com.nttdocomo.android.schedulememo", "スマホ診断": "jp.co.nttdocomo.chkapl", "データ保管BOX": "com.nttdocomo.android.cloudstorageservice", "デコメ絵文字マネージャー": "jp.co.omronsoft.android.decoemojimanager_docomo", "ドコモクラウド設定": "com.nttdocomo.android.cloudset", "ドコモサービス": "com.nttdocomo.android.docomoset", "ドコモバックアップ": "com.nttdocomo.android.sdcardbackup", "ドコモメール": "jp.co.nttdocomo.carriermail", "ドコモ位置情報": "jp.co.nttdocomo.lcsapp", "ドコモ位置情報SUB": "jp.co.nttdocomo.lcsappsub", "ドコモ音声入力": "com.nttdocomo.android.dcmvoicerecognition", "ドコモ電話帳": "com.android.contacts", "ドコモ文字編集": "com.nttdocomo.android.voiceeditor", "トルカ": "com.nttdocomo.android.toruca", "マネレコ": "com.nttdocomo.android.moneyrecord", "メディアプレイヤー": "com.nttdocomo.android.mediaplayer", "遠隔サポート": "com.rsupport.rs.activity.ntt", "遠隔初期化": "com.nttdocomo.android.wipe", "災害用キット": "jp.co.nttdocomo.saigaiban", "端末エラー情報送信": "com.nttdocomo.android.settings.lac", "地図アプリダウンローダ": "jp.dmapnavi.navi02", " 電話帳サービス": "com.nttdocomo.android.socialphonebook", "Contents Headline": "jp.co.nttdocomo.contentsheadline", "dアカウント設定": "com.nttdocomo.android.idmanager", "dフォト": "com.nttdocomo.android.photocollection", "dブックマイ本棚": "jp.co.nttdocomo.dbook", "dポイントクラブ": "com.nttdocomo.android.dpoint", "dマーケット": "com.nttdocomo.android.store", "dメニュー": "com.nttdocomo.android.dmenu2", "DcmAccountWipeService": "com.nttdocomo.android.accountwipe", "DcmIpPushAhgregator": "com.nttdocomo.android.pf.dcmippushaggregator", "DcmWapPushHelper": "com.nttdocomo.android.pf.dcmwappush", "docomo Application manager": "com.nttdocomo.android.applicationmanager", "docomo Authenticator": "com.nttdocomo.android.accountauthenticator", "DOCOMO Initialization": "com.nttdocomo.android.initialization", "Docomo Lac": "com.nttdocomo.android.lac", "docomo LIVE UX": "com.nttdocomo.android.dhome", "docomo LIVE UX バックアップ": "com.nextbit.app", "iコンシェル": "com.nttdocomo.android.iconcier", "iコンシェルコンテンツ": "com.nttdocomo.android.iconcier_contents", "ICタグ・バーコードリーダー": "com.nttdocomo.android.ictrw", "てがき翻訳": "com.nttdocomo.android.writingtranslation"}

f_app = {"@Fケータイ応援団": "com.fujitsu.mobile_phone.atfsite", "かんたんインターネット": "com.fujitsu.mobile_phone.fbrowser", "かんたん（ATOK関連）": "com.atok.mobile.im.fujitsu.theme.basic", "キッズ（低学年）（ATOK関連）": "com.atok.mobile.im.fujitsu.theme.kids1", "じかんわり": "com.fujitsu.mobile_phone.timetablewidget", "スタンダード・ブラック": "com.atok.mobile.im.fujitsu.theme.black", "スタンダード・ホワイト": "com.atok.mobile.im.fujitsu.theme.white", "できたよカレンダー": "com.fujitsu.mobile_phone.stumpcalendar", "らくらくコミュニティ": "com.fujitsu.mobile_phone.rakurakucommunity", "虹彩認証体験": "com.fujitsu.mobile_phone.irisdemo", "WPS Office": "cn.wps.moffice_eng", "ULTIAS自動辞書切り替え定義": "com.atok.mobile.im.fujitsu.dictionary", "Super ATOK ULTIAS": "com.atok.mobile.im.fujitsu.service", "NX!Input韓国語": "com.fujitsu.nxinput.korea", "NX!Input中国語（簡体字）": "com.fujitsu.nxinput.chinese", "NX!メール": "com.fujitsu.mobile_phone.nxmail", "NX!ホーム（かんたん）": "com.fujitsu.mobile_phone.simple_home", "LAWSON": "jp.co.lawson.activity", "KSfilemanager": "jp.co.tshworld.ksfilemanager.pi", "Kindle": "com.amazon.kindle", "アプリ電池診断": "com.fujitsu.mobile_phone.batterydoctor", "キッズスタイルデータベース": "com.fujitsu.mobile_phone.kidsstyleusageprovider"}

for menu in menu_array:
    print(menu)
choose = input('Select: ')
if(choose == "1"):
    print("ドコモ製純正アプリの消去を選択しました。")
    print("削除内容を確認しながら削除しますか？[[y]/n]")
    yorn = input("Select:")
    if(yorn.lower() == "n"):
        for k, v in d_app.items():
            print(k,"の削除を試行中・・・")
            subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
    else:
        for k, v in d_app.items():
            print(k,"を削除しますか？[[y]/ n]")
            final_check = input("Select:")
            if(final_check.lower() == "y"):
                if(v == "com.nttdocomo.android.remotelock" or v == "com.nttdocomo.android.wipe"):
                    print(k,"はデバイス管理者アプリケーションです。デバイス管理者設定の解除を試行中です・・・")
                    subprocess.call("adb shell dpm remove-active-admin "+str(v))
                subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
                

elif(choose == "2"):
    print("富士通製純正アプリの消去を選択しました。")
    print("削除内容を確認しながら削除しますか？[[y]/n]")
    yorn = input("Select:")
    if(yorn.lower() == "n"):
        for k, v in f_app.items():
            print(k,"の削除を試行中・・・")
            subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
    else:
        for k, v in f_app.items():
            print(k,"を削除しますか？[[y]/ n]")
            final_check = input("Select:")
            if(final_check.lower() == "y"):
                subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
elif(choose == "3"):
    print("両デフォルトアプリケーションの消去を選択しました。")
    print("削除内容を確認しながら削除しますか？[[y]/n]")
    yorn = input("Select:")
    if(yorn.lower() == "n"):
        for k, v in d_app.items():
            print(k,"の削除を試行中・・・")
            subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
        for k, v in f_app.items():
            print(k,"の削除を試行中・・・")
            subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
    else:
        for k, v in d_app.items():
            print(k,"を削除しますか？[[y]/ n]")
            final_check = input("Select:")
            if(final_check.lower() == "y"):
                subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
        for k, v in f_app.items():
            print(k,"を削除しますか？[[y]/ n]")
            final_check = input("Select:")
            if(final_check.lower() == "y"):
                subprocess.call("adb shell pm uninstall -k --user 0 "+str(v))
elif(choose == "4"):
    print("Good Bye!")
    exit()