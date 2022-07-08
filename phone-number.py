import vonage


client = vonage.Client(key="06534d3d", secret="bHOgSQ9BXduToxdV")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "RayyanDevelopers",
        "to": "998917377985",
        "text": "Login kodi: 15222. Bu kodni hech kimga bermang, hatto u Spiska.uz dan ekanligini aytsa ham!"
"Bu koddan Spiska.uz hisobingizga kirish uchun foydalanilishi mumkin. Biz hech qachon uni boshqa maqsadda so'ramaymiz."
"Agar boshqa qurilmadan kirish uchun bu kodni so'ramagan bo'lsangiz, shunchaki ushbu xabarni e'tiborsiz qoldiring.",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")