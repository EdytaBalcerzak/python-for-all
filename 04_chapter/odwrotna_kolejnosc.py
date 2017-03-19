#program pobiera komunikat od użytkownika , a następnie zapisuje go w odwrotnej kolejności

message = input("Wpisz swoją wiadomość")


#if message:
    #print(message[::-1])
new_message = ""
for i in range(-1,-len(message)-1,-1):
    print(i)
    new_message += message[i]
print(new_message)

input("Aby zakończyć program, naciśnij Enter")
