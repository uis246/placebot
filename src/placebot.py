from Placer import Placer, Color

username = "KirellaGamma"
password = "pw3osunlockRed"

placer = Placer()
placer.login(username, password)

if placer.logged_in:
    placer.place_tile(5, 5, Color.WHITE)