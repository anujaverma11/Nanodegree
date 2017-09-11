from twilio.rest import Client

account_sid = "AC8e94d448e9d1b0eb746bb868ad9a6182" # Your Account SID from www.twilio.com/console
auth_token  = "0a377c0c96742f7824ebd025cb19ad55"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Anuja using Twilio <3",
    to="+14156063776",    # Replace with your phone number
    from_="+14154981890") # Replace with your Twilio number

print(message.sid)