from twilio.rest import Client

# account_sid = "H+yPCEmgncmWi+ifH5Ufy6igkQtR4MS+dyGq9W6P"
account_sid = "AC4ead53b8cee05b2cf0d7b1e199c5cacf"
auth_token = "b567d46896909773d72260d01d51d3ab"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+8618623001528',
                        from_='+14694051528'
                    )

print(call.sid)
