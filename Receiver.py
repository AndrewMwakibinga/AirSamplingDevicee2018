from Hologram.HologramCloud import HologramCloud
 
hologram = HologramCloud(dict(), network='cellular')
result = hologram.network.connect()
if result == False:
    print ' Failed to connect to cell network'
hologram.openReceiveSocket()
time.sleep(20) # sleep for 20 seconds
hologram.closeReceiveSocket()
recv = hologram.popReceivedMessage()
print 'Receive buffer: ' + str(recv)
hologram.network.disconnect()