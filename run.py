import pywhatkit as kit

number = input("please input german phone number without leading zero: ")
hour = int(input("when to send (hour): "))
minute = int(input("when to send (minute): "))
message = input("what do you want to say: ")

kit.sendwhatmsg("+49" + number, message, hour, minute)
