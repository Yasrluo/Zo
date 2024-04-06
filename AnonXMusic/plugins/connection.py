from pyrogram import Client

# استبدال "API_ID" و "API_HASH" بالقيم الخاصة بك
api_id = "11359665"
api_hash = "df66bc5f7f80d04aecd20ebae3708c4d"

# إنشاء عميل Pyrogram
app = Client("my_session", api_id=api_id, api_hash=api_hash)

# دالة للتعامل مع فتح الاتصال
async def on_connected(client, app):
    print("تم فتح الاتصال بواسطة")

# تسجيل الدالة للتشغيل عندما يتم فتح الاتصال
app.on_connect(on_connected)

# تشغيل العميل
app.run()
