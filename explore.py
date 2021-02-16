from twilio.rest import Client

client = Client("ACc17a00d0a73936e0ac1deae70b3c4dc9", "568c7be1e1138bacd2b5dadaa85c7b9d")

#for msg in client.messages.list():
 #   print(msg.body)

msg = client.messages.create(
     to = "+353894602240",
     from_ = "+17692077456",
     body = "Hello from Python",
 )

print(f"Created a New Message: {msg.sid}")
