from Hologram.HologramCloud import HologramCloud

hologram = HologramCloud(dict(), network='cellular')

result = hologram.network.connect()
if result == False:
    print ' Failed to connect to cell network'

response_code = hologram.sendMessage("hello, world 1!")
print hologram.getResultString(response_code) # Prints 'Message sent successfully'.
response_code = hologram.sendMessage("hello, world 2!",
                                topics=["example-topic"])

hologram.network.disconnect()